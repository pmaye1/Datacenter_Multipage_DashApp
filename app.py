import dash
from dash import dcc
from dash import html, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from flask import Flask

server = Flask(__name__)

app = dash.Dash(__name__,server=server, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True,
	meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])



app.title='Datacenter | Bonebase'

Navbar=[
        dbc.NavItem(dbc.NavLink("Home", href="https://bonebase.lab.uconn.edu/",style={'color':'white'})),
        dbc.NavItem(dbc.NavLink('Datacenter Home', href="/",style={'color':'white'})),
        dbc.NavItem(dbc.NavLink('Project1', href="/Project1",style={'color':'white'})),
        dbc.NavItem(dbc.NavLink('Project2', href="/Project2",style={'color':'white'})),
        dbc.NavItem(dbc.NavLink("Project Information", href="https://bonebase.lab.uconn.edu/projects-data/",style={'color':'white'})),
        dbc.NavItem(dbc.NavLink("Data Interpretation", href="https://bonebase.lab.uconn.edu/projects-data/interpretation-of-data/",style={'color':'white'})),
        dbc.NavItem(dbc.NavLink("Contact Us", href="https://bonebase.lab.uconn.edu/contact_us/",style={'color':'white'})),
    ]


Nav1=dbc.Nav(Navbar,pills=True,
    style={'text-align':'center','fontSize': 15,'border-color':"white", 'font-weight':'normal','font-family':'arial'}),



app.layout = html.Div([ dbc.Container([

    dbc.Row([
    dbc.Col([

     html.A(
        dbc.Row([
            dbc.Col([

                     (html.Img(src='/assets/uconn.png',
                        style={'height': '7.5%', 'margin-top':20},
                    ) )
            ])

        ], style={'background-color':'#000e2f',
                    'padding-left':1000, 'margin-left':-1000, 'margin-right':-500,'padding-right':0,'height':60}
        ),href="https://health.uconn.edu/"),
html.A(
        dbc.Row([
            dbc.Col([
                    html.Br(),
                    html.P('CENTER FOR REGENERATIVE MEDICINE AND SKELETAL DEVELOPMENT',
                    style={'textAlign': 'left', 'fontFamily': 'Segoe UI Emoji', 'color':'#989898', 'font-size':11,
                        'letter-spacing':2, 'line-height':1,'margin-top':10}),

            ]),
        ], style={'background-color':'#04305E','padding-left':1000, 'margin-left':-1000, 'margin-right':-500,
                 'padding-right':-500,'height':50,'border-top':1,'border-top-style': 'solid','border-top-color':'#989898'}
        ),href='https://dentalmedicine.uconn.edu/divisions/center-for-regenerative-medicine-and-skeletal-development/',className="text-decoration-none"
),
html.A(
        dbc.Row([
            dbc.Col([

                html.H6('Bonebase', style={'textAlign': 'left', 'fontFamily': "Helvetica", 'color': 'white',
                                               "font-size":20, "font-weight":'550','line-height':15,'margin-top':0}),
            ],style={'justify':'center'})
        ], style={'background-color':'#04305E','padding-left':1000, 'margin-left':-1000, 'margin-right':-500,
                 'padding-right':-500,'height':25}
        ), href='https://bonebase.lab.uconn.edu/',className="text-decoration-none"),

        dbc.Row([
            dbc.Col([

                html.H6('Welcome to the Bonebase Datacenter', style={'textAlign': 'left', 'fontFamily': "Verdana", 'color': 'white',
                                               "font-size":18, "font-weight":'normal','line-height':15,'margin-top':5}),
            ])
        ], style={'background-color':'#04305E','padding-left':1000, 'margin-left':-1000, 'margin-right':-500,
                 'padding-right':-500,'height':30}, justify='end',
        ),

        dbc.Row([
            dbc.Col([ html.Div(Nav1)


                # dbc.Nav( children=[
                #     dbc.NavLink("Home", href="https://bonebase.lab.uconn.edu/",style={'color':'white'}),
                #     dbc.NavLink('Datacenter Home', href="/",style={'color':'white'}),
                #     dbc.NavLink('Project1', href="/Project1",style={'color':'white'}),
                #     dbc.NavLink('Project2', href="/Project2",style={'color':'white'}),
                #     dbc.NavLink("Project Information", href="https://bonebase.lab.uconn.edu/projects-data/",style={'color':'white'}),
                #     dbc.NavLink("Data Interpretation", href="https://bonebase.lab.uconn.edu/projects-data/interpretation-of-data/",style={'color':'white'}),
                #     dbc.NavLink("Contact Us", href="https://bonebase.lab.uconn.edu/contact_us/",style={'color':'white'}),
                # ], pills=True,style={'text-align':'center','fontSize': 15,'border-color':"white",
                #                         'font-weight':'normal','font-family':'arial'}),


            ])
        ],  style={'background-color':'#04305E','padding-left':1000, 'margin-left':-1000, 'margin-right':-500,
                 'padding-right':0,'height':40}, justify='end',
        ),


        # content of each page
        dbc.Row([
            html.Div(children=[
            dash.page_container]
            ),

            # dcc.Location(id='url', refresh=True),

        ],justify='center'),


    ],md=10),
],justify='center') #style={'overflow-x':'hidden'}

])
])

if __name__ == '__main__':
    app.run(debug=True)
    #app.run_server(debug=True)