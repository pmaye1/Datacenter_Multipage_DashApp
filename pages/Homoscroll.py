import dash
import dash_bootstrap_components as dbc
from dash import html


CT={'background-color':'#176d9d',
    'color':'white',
    'text-align':'center',
    # 'display':'block',
    'font-size':12,
    'border-radius':12,
    # 'border':'white',
    'padding':4,
    'margin':2,
    'font-family':'arial'}
HISTO={'background-color':'#053465',
    'color':'white',
    'text-align':'center',
    # 'display':'block',
    'font-size':12,
    'border-radius':12,
    # 'border':'white',
    'padding':4,
    'margin':2,
    'font-family':'arial'}
GV={'background-color':'#4a5658ed',
    'color':'white',
    'text-align':'center',
    # 'display':'block',
    'font-size':12,
    'border-radius':12,
    # 'border':'white',
    'padding':4,
    'margin':2,
    'font-family':'arial'}

def scroll_layout():
    return  dbc.Container([
    dbc.Row([
        dbc.Col([
        html.Div([
        html.Nav([
            html.A(html.Button("Femur Trabecular Bone", style=CT), href=dash.page_registry['pages.HOMO_CT_FTRAB']['path'],
                   className="lead"),

            html.A(html.Button("Femur Cortical Bone", style=CT), href=dash.page_registry['pages.HOMO_CT_FCOR']['path'],
                   className="lead"),
            html.A(html.Button("Vertebra Trabecular Bone", style=CT), href=dash.page_registry['pages.HOMO_CT_VTRAB']['path'],
                   className="lead"),

            html.A(html.Button("View by Gene", style=GV), href=dash.page_registry['pages.Data_Tab2']['path'],
                   className="lead"),

            html.A(html.Button("Femur Trabecular Bone Static", style=HISTO), href=dash.page_registry['pages.HOMO_HISTO_FTRAB']['path'],
                   className="lead"),

            html.A(html.Button("Femur Trabecular Bone Osteoblast", style=HISTO), href=dash.page_registry['pages.HOMO_HISTO_FTRAB_OB']['path'],
                   className="lead"),
            html.A(html.Button("Femur Trabecular Bone Osteoclast", style=HISTO), href=dash.page_registry['pages.HOMO_HISTO_FTRAB_OC']['path'],
                   className="lead"),

            html.A(html.Button("Vertebra Trabecular Bone Static", style=HISTO), href=dash.page_registry['pages.HOMO_HISTO_VTRAB']['path'],
                   className="lead"),

            html.A(html.Button("Vertebra Trabecular Bone Osteoblast", style=HISTO), href=dash.page_registry['pages.HOMO_HISTO_VTRAB_OB']['path'],
                   className="lead"),
            html.A(html.Button("Vertebra Trabecular Bone Osteoclast", style=HISTO), href=dash.page_registry['pages.HOMO_HISTO_VERT_OC']['path'],
                   className="lead"),


        ],style={'overflow-x':'scroll','white-space': 'nowrap'})


    ])

    ],md=12, style={'margin-left':-50})
    ]),


])

