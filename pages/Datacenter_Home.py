import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__, path='/', name="Datacenter Home")


layout = html.Div([
    html.Br(),
    dbc.Col([
dbc.Container(
    [

        html.H1("Welcome to the Bonebase Datacenter", className="text-md-center" #className="display-4"
            ),

        html.P(
            "Please Select the Links to Project 1 and Project 2 to View Bone Phenotyping Data on Several Knockout Mouse Lines",
            className="text-md-center" ,  style={'font-size':18}, #className="lead",
        ),

        html.Hr(className="my-2"),
        html.Br(),
        html.P("To learn how to navigate the datacenter please select the button below."),

        html.P(dbc.Button("Datacenter Tutorial",
                          href="https://bonebase.lab.uconn.edu/video-tutorial-on-how-to-use-and-navigate-through-the-datacenter/",
                          color="primary"),  className="lead"),

    ],fluid=True,className="py-3",
    style={'border-style': 'solid', 'border-color': 'black', 'gray':3,'background-color':'#d1d1d157'}),

], md=12,lg=12,sm=12,xl=12,xs=12, style={"margin-left":-75})
    ])