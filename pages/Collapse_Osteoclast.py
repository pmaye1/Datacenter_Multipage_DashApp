import dash
from dash import dcc, html,callback,Input,Output
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


OSTC=html.Div([
    html.P("TRAP/BS = Fraction of bone surface with TRAP label. This scores for TRAP activity irrespective of the cell size or"
           " the number of nuclei per cell."),
    html.P("TRAP-L/BS = Proportion of mineralizing surface that is covered with a TRAP label."),
    html.P("TRAP-NL/BS = Proportion of non-mineralizing surface that is covered with a TRAP label."),
    html.P("APL-TRAPL/BS = Proportion of bone surface where the AP, TRAP and mineralization signals are co-localized."
           " We assume that the close proximity of osteoclastic and osteoblastic activity identifies a region of high bone remodeling."),
    html.P("TRAP-BS/TRAP = Proportion of total TRAP within the bone (marrow included) that is on the bone surface."),
    html.P("TRAP-L/TRAP-BS = The fraction of the bone surface associated TRAP positive signal that overlies a mineralizing surface."),
    html.P("TRAP-NL/TRAP-BS = The fraction of the bone surface associated TRAP positive signal that overlies a non-mineralizing "
           "(metabolically inactive) surface. "),
], style={'font-family':'Arial', 'font-size':16})

CT={'background-color':'#1464b3',
    'color':'white',
    'text-align':'center',
    # 'display':'block',
    'font-size':12,
    'border-radius':12,
    # 'border':'white',
    'padding':7,
    'margin':2,
    'font-family':'arial',
    'position': 'absolute',
    "z-index": 2}

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "right": 0,
    "bottom": 0,
    "width": "25rem",
    "height": "85%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    "background-color": "#f8f9fa",
}

SIDEBAR_HIDEN = {
    "position": "fixed",
    "top": 0,
    "right": "-25rem",
    "bottom": 0,
    "width": "25rem",
    "height": "85%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#f8f9fa",
}
button = dbc.Button("Measurement Definitions", outline=False, color="dark", className="mr-1", id="btn_sidebar4", style=CT)

sidebar = html.Div(
    [
        html.H4("Measurement Definitions", className="display-6"),
        html.Hr(),
        # html.P("A simple sidebar layout with navigation links", className="lead"),
        dbc.Nav(dbc.NavItem(OSTC, id="navitem", className='lead'),
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar4",
    style=SIDEBAR_HIDEN,
)


def layout_OC():
    return html.Div(
    [
        dcc.Store(id='side_click4'),
        sidebar,
        dbc.Row(
            dbc.Col([button], width={'size': 2, 'offset': 8}, style={'margin-right': 0, 'margin-top': -40})
            # justify='end', style={'margin-right':-75, 'margin-top':-60}
        )
    ],
)


@callback(
    [   Output("sidebar4", "style"),
        Output("side_click4", "data"),
    ],

    [Input("btn_sidebar4", "n_clicks")],
    [State("side_click4", "data")]
)
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_STYLE
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_HIDEN
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_HIDEN
        cur_nclick = 'SHOW'

    return sidebar_style, cur_nclick



# if __name__ == "__main__":
#     app.run_server(debug=True, port=8086)