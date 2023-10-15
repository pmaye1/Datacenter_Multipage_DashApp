import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


OSTB=html.Div([
    html.P("MAR = Mineral Apposition Rate: this measurement is determined by the software as the perpendicular "
           "distance between the midpoint of each mineralization line rather than the leading edge as is performed "
           "manually. By measuring the midpoint, differences in line width usually caused by variation in section angle "
           "can be minimized. The distance in microns is divided by the day interval between the two dye injections. "
           "Usually males animals have a higher MAR but significant intragroup variation in this measurement also is observed."),
    html.P("MS/BS = Mineralizing Surfaces per Bone Surface: This is calculated as the surfaces containing a double label plus ½ "
           "of the surfaces containing either a single red or green label ((dLS + sLS/2)/BS)). The calculation is the traditional "
           "measure of bone surfaces under active mineral apposition. Usually females have a higher MS/BS ratio although there is "
           "significant variation of this measure within animal groups."),
    html.P("BFR = Bone Formation Rate: This a calculated value obtained by MAR x MS/BS. It was intended to compare overall bone formation"
           " between two groups but it may obscure the underlying basis for differences in bone forming activity. Also the variation of "
           "this measurement is particularly high because of the high variation in the component measurements. Females usually have a "
           "higher BFR than males."),
    html.P("AP/BS = Alkaline Phosphatase Positive Surfaces per Bone Surface:This measurement identifies all the trabecular surfaces "
           "that are AP positive which can include active osteoblasts and bone lining cells capable of resuming an active osteoblast status."),
    html.P("AP-L/BS = Alkaline phosphatase positive surfaces over a mineral labeling surfaces per bone surface:Surfaces that are both "
           "AP+ and labeled (red, green, single or double) are assumed to be active bone forming surfaces, while those which are AP_NL/BS represent "
           "inactive (bone lining) surfaces. An example of a bone surface exhibiting AP and a red mineralization line is shown in figure x. Female "
           "mice usually have a higher AP_L/BS value than males."),
    html.P("AP-NL/BS = AP+ and non-labeling surfaces per bone surface: The AP_NL/BS represent inactive (bone lining) surfaces."
           " by the diaphyseal span length of diaphyseal span length"),
    html.P("AP-L/AP = The proportion of total AP positive cells that are over a labeled surface to determine the percentage of active "
           "osteoblasts."),
    html.P("AP-NL/AP = The proportion of total AP that is over a non-labeled surface, representing the percentage of inactive osteoblasts. "),
], style={'font-family':'Arial', 'font-size':16})

CT={'background-color':'#1464b3',
    'color':'white',
    'text-align':'center',
    # 'display':'block',
    'font-size':12,
    'border-radius':12,
    # 'border':'white',
    'padding':7.5,
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
button = dbc.Button("Measurement Definitions", outline=False, color="dark", className="mr-1", id="btn_sidebar3", style=CT)

sidebar = html.Div(
    [
        html.H4("Measurement Definitions", className="display-6"),
        html.Hr(),
        # html.P("A simple sidebar layout with navigation links", className="lead"),
        dbc.Nav(dbc.NavItem(OSTB, id="navitem", className='lead'),
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar3",
    style=SIDEBAR_HIDEN,
)


def layout_OB():
    return html.Div(
    [
        dcc.Store(id='side_click3'),
        sidebar,
        dbc.Row(
            dbc.Col(button)

        )
    ],
)


@callback(
    [   Output("sidebar3", "style"),
        Output("side_click3", "data"),
    ],

    [Input("btn_sidebar3", "n_clicks")],
    [State("side_click3", "data")]
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