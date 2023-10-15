import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

CORT=html.Div([
    html.P("Ct.Mask = Cortical Mask is the area between periosteal and endocortical surfaces; including porosity."),
    html.P("Ma.Ar = Marrow Area is the area enclosed by the endocortical perimeter."),
    html.P("Tt.Ar = Total Area is the area enclosed by the periosteal perimeter. It includes all bone, marrow, and porosity."),
    html.P("Ct.Ar/Tt.Ar = Cortical Bone Area over Total Area"),
    html.P("Ct.Ar = Cortical Bone Area is the cortical mask minus porosity"),
    html.P("Ps.Pm = Periosteal Perimeter: Length measurement of the outer cortical bone perimeter."),
    html.P("Ec.Pm = Endosteal Perimeter: Length measurement of the inner cortical bone perimeter. "),
    html.P("Ct.Th = Cortical Thickness is the direct measurement of the mid-diaphysis cortical thickness. "
           "This is calculated on a volumetric basis to obtain a highly accurate measure of average thickness"),
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
button = dbc.Button("Measurement Definitions", outline=False, color="dark", className="mr-1", id="btn_sidebar2", style=CT)

sidebar = html.Div(
    [
        html.H4("Measurement Definitions", className="display-6"),
        html.Hr(),
        # html.P("A simple sidebar layout with navigation links", className="lead"),
        dbc.Nav(dbc.NavItem(CORT, id="navitem", className='lead'),
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar2",
    style=SIDEBAR_HIDEN,
)


def layout_CORT():
    return  dbc.Container( children=[
        dcc.Store(id='side_click2'),
        sidebar,
    dbc.Row(
        dbc.Col(button)
    )

    ],
)


@callback(
    [   Output("sidebar2", "style"),
        Output("side_click2", "data"),
    ],

    [Input("btn_sidebar2", "n_clicks")],
    [State("side_click2", "data")]
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