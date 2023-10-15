import dash
from dash import dcc, html, callback,Input, Output
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


TBSN=html.Div([
    html.P("BV/TV = Bone Volume per Total Volume (%)"),
    html.P("Tb.N = Trabecular Number (#/mm)"),
    html.P("Tb.Th = Trabecular Thickness (µm)"),
    html.P("Tb.Sp = Trabecular Spacing (µm)"),
], style={'font-family':'Arial', 'font-size':16})

BUTTON_STYLE={
    'bottom':-140,
    'left':'5%',
    'width':100,
    'height':60,
    'position': 'absolute',
    'z-index': 2,
    'font-size':12,
    'text-align':'center'

}

CT={'background-color':'#1464b3',
    'color':'white',
    'text-align':'center',
    # 'display':'block',
    'font-size':12,
    'border-radius':12,
    # 'border':'white',
    'padding':6,
    'margin':2,
    'font-family':'arial',
    'position': 'absolute',
    "z-index": 2
    }

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 250,
    "right": 0,
    "bottom": 0,
    "width": "25rem",
    "height": "50%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    "background-color": "#f8f9fa",
}

SIDEBAR_HIDEN = {
    "position": "fixed",
    "top": 250,
    "right": "-25rem",
    "bottom": 0,
    "width": "25rem",
    "height": "30%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    "background-color": "#f8f9fa",
}
button = dbc.Button("Measurement Definitions", outline=False, color="dark", className="mr-2", style=CT, id="btn_sidebar")

sidebar = html.Div(
    [
        html.H4("Measurement Definitions", className="display-6"),
        html.Hr(),
        # html.P("A simple sidebar layout with navigation links", className="lead"),
        dbc.Nav(dbc.NavItem(TBSN, id="navitem", className='lead'),
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_HIDEN,
)


def layout_SB():
    return  dbc.Container( children=[

        dcc.Store(id='side_click'),
        sidebar,
    dbc.Row(
        dbc.Col(button)

    )
    ],
)


@callback(
    [   Output("sidebar", "style"),
        Output("side_click", "data"),
    ],

    [Input("btn_sidebar", "n_clicks")],
    [State("side_click", "data")]
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