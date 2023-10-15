import dash
import plotly.graph_objects as go
import pandas as pd
from dash import dash_table
from dash import html,callback
import dash_bootstrap_components as dbc
from dash import dcc
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
from scipy.stats import ttest_ind

import pathlib
# from index import app

dash.register_page(__name__, path='/HOMO_CT_VTRAB')
from .Homoscroll import scroll_layout
from pages.Collapse_SB import layout_SB

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath('../datasets/KOMP220').resolve()

#Control Vertebra Data
controlfemaleVertebra_df=pd.read_csv(DATA_PATH.joinpath('controlfemaleVertebraIM.csv'))
controlfemaleVertebra_df=controlfemaleVertebra_df.dropna()

controlmaleVertebra_df=pd.read_csv(DATA_PATH.joinpath('controlmaleVertebraIM.csv'))
controlmaleVertebra_df=controlmaleVertebra_df.dropna()

#Homozygous Mutant Vertebra Data
femaleVert_df=pd.read_csv(DATA_PATH.joinpath('femaleVertebraIM.csv'))
maleVert_df=pd.read_csv(DATA_PATH.joinpath('maleVertebraIM.csv'))
data3= pd.read_csv(DATA_PATH.joinpath('female_Vert_average.csv'))
data4= pd.read_csv(DATA_PATH.joinpath('male_Vert_average.csv'))


ratio_df=pd.DataFrame(columns=['Gene Symbol', 'Female Vertebra', 'Male Vertebra'])

#calculating the average BV/TV of control groups
FemaleVertebra_Count=controlfemaleVertebra_df['BV/TV'].count()
FV_BVTVave=(sum(controlfemaleVertebra_df['BV/TV'])/FemaleVertebra_Count)*100
MaleVertebra_Count=controlmaleVertebra_df['BV/TV'].count()
MV_BVTVave=(sum(controlmaleVertebra_df['BV/TV'])/MaleVertebra_Count)*100

ratio_df['Gene Symbol']=data3['gene_symbol']
ratio_df['Female Vertebra']=((((data3['BV/TV'])*100/FV_BVTVave)-1)*100)
ratio_df['Male Vertebra']=((((data4['BV/TV'])*100/MV_BVTVave)-1)*100)


BoneType = ['Female Vertebra', 'Male Vertebra']
ratio_df=ratio_df.round(2)

genelist=ratio_df['Gene Symbol']

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
    'z-index':1}

def layout():
    return html.Div([ dbc.Container([
    dbc.Row(scroll_layout()),
dbc.Col([

    # row  2
    dbc.Row(
        [html.H1('Vertebra µCT Outcomes for Global Homozygous KO Mice',
                        style={'color': 'black', 'fontSize': 25,'fontFamily': "Verdana","font-weight":"600",
                               'margin':'auto'}),

        ], style={'height': 60, 'padding-bottom': 0, 'padding-top': 0, 'margin-bottom':0, 'margin-left':200,'margin-right':-50},

    ),
    # row  3
    dbc.Row([
        dbc.Col([
            html.Div([
                html.P("% Increase/Decrease in BV/TV", style={'font-family':'arial', 'font-weight':'bold', 'padding-left':50, 'padding-bottom':0, 'margin-bottom':0}),
                dash_table.DataTable(
                    id='Table3',
                    data=ratio_df.to_dict('records'),
                    sort_action='native',
                    row_selectable='single',
                    selected_rows=[],
                    columns=[{'name':'Gene Symbol', 'id': 'Gene Symbol', 'type': 'text', 'editable': False},
                            # {'name':'Female Femur', 'id': 'Female Femur','type':'numeric','editable':False},
                            # {'name': 'Male Femur', 'id': 'Male Femur', 'type':'numeric','editable':False}],
                            {'name':'Female Vertebra', 'id': 'Female Vertebra', 'type': 'numeric', 'editable': False},
                            {'name':'Male Vertebra', 'id': 'Male Vertebra', 'type': 'numeric', 'editable': False}],


                    style_data_conditional=[
            {'if': {
                'filter_query': '{Female Vertebra} >= 10.0',
                'column_id': 'Female Vertebra'},
            'backgroundColor': 'tomato',
            'color': 'white'
            },
            # {'if': {
            #     'filter_query': '{Female Femur} >= 20.0',
            #     'column_id': 'Female Femur'},
            # 'backgroundColor': 'tomato',
            # 'color': 'white'
            # },
            # {'if': {
            #     'filter_query': '{Male Femur} >= 20.0',
            #     'column_id': 'Male Femur'},
            # 'backgroundColor': 'tomato',
            # 'color': 'white'
            # },
            {'if': {
                'filter_query': '{Male Vertebra} >= 10.0',
                'column_id': 'Male Vertebra'},
            'backgroundColor': 'tomato',
            'color': 'white'
            },

        # {
        #     'if': {
        #         'filter_query': '{Female Femur} <= -20.0',
        #         'column_id': 'Female Femur'},
        #     'backgroundColor': 'dodgerblue',
        #     'color': 'white',
        #  },
        #     {'if': {
        #         'filter_query': '{Male Femur} <= -20.0',
        #         'column_id': 'Male Femur'},
        #     'backgroundColor': 'dodgerblue',
        #     'color': 'white'
        #     },
        {
            'if': {
                'filter_query': '{Female Vertebra} <= -10.0',
                'column_id': 'Female Vertebra'},
            'backgroundColor': 'dodgerblue',
            'color': 'white',
         },
            {'if': {
                'filter_query': '{Male Vertebra} <= -10.0',
                'column_id': 'Male Vertebra'},
            'backgroundColor': 'dodgerblue',
            'color': 'white'
            }
                                ],
            style_cell={'padding': '5px', 'font_family': 'arial','font_size': '13px',
                        'text_align': 'left'},
            style_cell_conditional=[{'if': {'column_id': 'Gene Symbol'},
                                         'fontWeight':'bold'
                                   }],
            style_header={'backgroundColor': 'white','fontWeight': 'bold','font-size':12},
            page_action='native',
            page_size=18,
            # fixed_columns={'headers': True, 'data': 1},
            style_table={'minWidth': '100%'}

            ), ]),

        ],width=4),

        # dbc.Col([], width=1),
        dbc.Col([
            dcc.Graph(id='box_plot4', config={'modeBarButtonsToRemove': ['pan2d', 'displaylogo','autoScale2d','resetScale2d','hoverClosestCartesian',
                        'lasso2d','zoomIn2d','zoomOut2d','zoom2d','select2d','toggleSpikelines','hoverCompareCartesian','toggleHover'],
                        'displayModeBar': True, 'displaylogo': False, 'toImageButtonOptions':{'format': 'png'}}) #'displayModeBar': False
                 ], width=8, style={'margin-left':25, 'margin-right':-25}),

     ], style={'height': 650, 'margin-left':-20, 'padding-bottom': 0, 'padding-top': 0, 'margin-bottom':0,'justify':'center'}),

    dbc.Row([
        dbc.Col([html.P('Numbers represent the % increase or decrease in bone volume per tissue volume'
                ' based on calculating ((BV/TV mutant/BV/TV control)-1)x100',
                        style={'color': 'black', 'fontSize': 12,'fontFamily': "Verdana",
                               'margin':'auto'}),
                ], width=4),
        dbc.Col([html.P('P values were calculated based on the outcomes of a two sample t-test',
                        style={'color': 'black', 'fontSize': 12,'fontFamily': "Verdana",
                               'margin':'auto', 'textAlign':'center'}),

               #  html.A('[Guide: µCT Measurement Definitions]',
               # style={'textAlign': 'right', 'fontFamily': "Verdana", 'color': 'black',
               #        "font-size": 12, "font-weight": 'normal', 'line-height': 15, 'margin-top': 5, 'margin-left': 150},
               # href='http://bonebase.org/08_DataInterpretation/MicroCt.html'),
        ], width=3, style={'margin-left':80}),

        dbc.Col([
            html.Div([
                dbc.Button(
                    'µCT Images',
                    id='btn-nclicks-3',
                    className="mx-2",
                    style=CT,
                    n_clicks=0,
                    href='https://ucsci.uchc.edu/bonebase/GeneEntry.html?GeneSymbol=Irf8+MicroCT_VertTrab',
                    target='_blank',
                    external_link=True
                ),
                ]),
            ],width=2,style={'margin-right':-20,'margin-left':100, 'margin-top':0}),

        dbc.Col(html.Div([layout_SB()], style={'margin-top': 0, 'margin-left': -20}),
                width=2, style={'margin-left': -70}),

        ], style={'height': 40, 'padding-bottom': 0, 'padding-top': 0, 'margin-bottom':0})

],md=12, style={'margin-left':-100})
])
],style={'margin-left':-50})

@callback(
    Output(component_id='box_plot4', component_property='figure'),
    Input(component_id='Table3', component_property='selected_rows')
    )
    # selected_rows provides a row index number. It was a challenge to use this as a callback.
    # The simple solution was to create a list and use the number from selected rows to determine the
    # gene symbol in the list based on its index. This provided the corrected gene symbol (value) which
    # was fed in to filter the dataframe to select the bvtv data for that gene.  The second challenge was converting
    # that list item into a string so the plot would show its name at the bottom. This was done by: n=''.join([str(elem) for elem in s])
def update_boxplots(selected_rows):
        if len(selected_rows) == 0:
            # df_filtered = femaleFemur_df[femaleFemur_df['gene_symbol'].isin(['Irf8'])]
            # df_filtered_MF = maleFemur_df[maleFemur_df['gene_symbol'].isin(['Irf8'])]

            df_filtered_FV = femaleVert_df[femaleVert_df['gene_symbol'].isin(['Irf8'])]
            df_filtered_MV = maleVert_df[maleVert_df['gene_symbol'].isin(['Irf8'])]

            bvtv = df_filtered_FV['BV/TV']
            bvtv2 = df_filtered_MV['BV/TV']
            TbN = df_filtered_FV['Tb.N']
            TbN2 = df_filtered_MV['Tb.N']
            TbTh = df_filtered_FV['Tb.Th']
            TbTh2 = df_filtered_MV['Tb.Th']
            TbSp = df_filtered_FV['Tb.Sp']
            TbSp2 = df_filtered_MV['Tb.Sp']

            y = bvtv
            y1 = controlfemaleVertebra_df['BV/TV']
            y2 = bvtv2
            y3 = controlmaleVertebra_df['BV/TV']
            y4 = TbN
            y5 = controlfemaleVertebra_df['Tb.N']
            y6 = TbN2
            y7 = controlmaleVertebra_df['Tb.N']
            y8 = TbTh
            y9 = controlfemaleVertebra_df['Tb.Th']
            y10 = TbTh2
            y11 = controlmaleVertebra_df['Tb.Th']
            y12 = TbSp
            y13 = controlfemaleVertebra_df['Tb.Sp']
            y14 = TbSp2
            y15 = controlmaleVertebra_df['Tb.Sp']

            name = "Irf8 -/-"

            t1, p1 = ttest_ind(y, y1)
            t2, p2 = ttest_ind(y2, y3)
            t3, p3 = ttest_ind(y4, y5)
            t4, p4 = ttest_ind(y6, y7)
            t5, p5 = ttest_ind(y8, y9)
            t6, p6 = ttest_ind(y10, y11)
            t7, p7 = ttest_ind(y12, y13)
            t8, p8 = ttest_ind(y14, y15)
            stat1 = round(p1, 5)
            stat2 = round(p2, 5)
            stat3 = round(p3, 5)
            stat4 = round(p4, 5)
            stat5 = round(p5, 5)
            stat6 = round(p6, 5)
            stat7 = round(p7, 5)
            stat8 = round(p8, 5)

        else:
            value = genelist[selected_rows]
            # df_filtered = femaleFemur_df[femaleFemur_df['gene_symbol'].isin(value)]
            # df_filtered_MF = maleFemur_df[maleFemur_df['gene_symbol'].isin(value)]
            df_filtered_FV = femaleVert_df[femaleVert_df['gene_symbol'].isin(value)]
            df_filtered_MV = maleVert_df[maleVert_df['gene_symbol'].isin(value)]

            bvtv = df_filtered_FV['BV/TV']
            bvtv2 = df_filtered_MV['BV/TV']
            TbN = df_filtered_FV['Tb.N']
            TbN2 = df_filtered_MV['Tb.N']
            TbTh = df_filtered_FV['Tb.Th']
            TbTh2 = df_filtered_MV['Tb.Th']
            TbSp = df_filtered_FV['Tb.Sp']
            TbSp2 = df_filtered_MV['Tb.Sp']


            y = bvtv
            y1 = controlfemaleVertebra_df['BV/TV']
            y2 = bvtv2
            y3 = controlmaleVertebra_df['BV/TV']
            y4 = TbN
            y5 = controlfemaleVertebra_df['Tb.N']
            y6 = TbN2
            y7 = controlmaleVertebra_df['Tb.N']
            y8 = TbTh
            y9 = controlfemaleVertebra_df['Tb.Th']
            y10 = TbTh2
            y11 = controlmaleVertebra_df['Tb.Th']
            y12 = TbSp
            y13 = controlfemaleVertebra_df['Tb.Sp']
            y14 = TbSp2
            y15 = controlmaleVertebra_df['Tb.Sp']


            s = value
            n = ''.join([str(elem) for elem in s])
            name = n + '-/-'

            t1, p1 = ttest_ind(y, y1)
            t2, p2 = ttest_ind(y2, y3)
            t3, p3 = ttest_ind(y4, y5)
            t4, p4 = ttest_ind(y6, y7)
            t5, p5 = ttest_ind(y8, y9)
            t6, p6 = ttest_ind(y10, y11)
            t7, p7 = ttest_ind(y12, y13)
            t8, p8 = ttest_ind(y14, y15)
            stat1 = round(p1, 5)
            stat2 = round(p2, 5)
            stat3 = round(p3, 5)
            stat4 = round(p4, 5)
            stat5 = round(p5, 5)
            stat6 = round(p6, 5)
            stat7 = round(p7, 5)
            stat8 = round(p8, 5)

        box_plot = make_subplots(rows=2, cols=4,
            specs=[[{},{},{},{}],[{},{},{},{}]], vertical_spacing= 0.17,
            # for colspan and rowspan default is 1 col or 1 row so setting up the spect like this
            #defines a 4x2 subplot
            subplot_titles=("<b>BV/TV</b> (%)", "<b>Tb.N</b> (#/mm)", "<b>Tb.Th</b> (µm)",'<b>Tb.Sp</b> (µm)',"<b>BV/TV</b> (%)", "<b>Tb.N</b> (#/mm)", "<b>Tb.Th</b> (µm)",'<b>Tb.Sp</b> (µm)'))

        box_plot.add_trace(go.Box(y=y, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, legendgroup='a'), row=1, col=1)
        box_plot.add_trace(go.Box(y=y1, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, legendgroup='a'), row=1, col=1)
        box_plot.add_trace(go.Box(y=y2, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, showlegend=False), row=2, col=1)
        box_plot.add_trace(go.Box(y=y3, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, showlegend=False), row=2, col=1)
        box_plot.add_trace(go.Box(y=y4, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, showlegend=False), row=1, col=2)
        box_plot.add_trace(go.Box(y=y5, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, showlegend=False), row=1, col=2)
        box_plot.add_trace(go.Box(y=y6, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, showlegend=False), row=2, col=2)
        box_plot.add_trace(go.Box(y=y7, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, showlegend=False), row=2, col=2)
        box_plot.add_trace(go.Box(y=y8, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, showlegend=False), row=1, col=3)
        box_plot.add_trace(go.Box(y=y9, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, showlegend=False), row=1, col=3)
        box_plot.add_trace(go.Box(y=y10, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, showlegend=False), row=2, col=3)
        box_plot.add_trace(go.Box(y=y11, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, showlegend=False), row=2, col=3)
        box_plot.add_trace(go.Box(y=y12, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, showlegend=False), row=1, col=4)
        box_plot.add_trace(go.Box(y=y13, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, showlegend=False), row=1, col=4)
        box_plot.add_trace(go.Box(y=y14, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, showlegend=False), row=2, col=4)
        box_plot.add_trace(go.Box(y=y15, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, showlegend=False), row=2, col=4)

        box_plot.update_layout(height=650, width=900, margin={'t': 30},plot_bgcolor='white',font_family='Arial')
        box_plot.update_yaxes(title_text="<b>Female</b>", row=1, col=1, range=[10, 40],gridcolor='#D3D3D3', title_font=dict(size=18,family='Arial'),tickfont=dict(size=14))
        box_plot.update_yaxes(row=2, col=1,title_text="<b>Male</b>", range=[10, 40],gridcolor='#D3D3D3',title_font=dict(size=18,family='Arial'),tickfont=dict(size=14))
        box_plot.update_yaxes(row=1, col=2, range=[3, 8],gridcolor='#D3D3D3',tickfont=dict(size=14))
        box_plot.update_yaxes(range=[3, 8], row=2, col=2,gridcolor='#D3D3D3',tickfont=dict(size=14) )
        box_plot.update_yaxes(row=1, col=3, range=[20, 80],gridcolor='#D3D3D3',tickfont=dict(size=14))
        box_plot.update_yaxes(row=2, col=3, range=[20, 80],gridcolor='#D3D3D3',tickfont=dict(size=14))
        box_plot.update_yaxes(row=1, col=4, range=[0, 400],gridcolor='#D3D3D3',tickfont=dict(size=14))
        box_plot.update_yaxes(range=[0, 400], row=2, col=4,gridcolor='#D3D3D3',tickfont=dict(size=14) )

        box_plot.update_xaxes(showline=True, linewidth=2, linecolor='#666A6D')
        box_plot.update_yaxes(showline=True, linewidth=2, linecolor='#666A6D')

        if stat1>0.001:
            box_plot.update_xaxes(title_text=(f'p={stat1}'), row=1, col=1)
        else:
            box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=1)
        if stat2>0.001:
            box_plot.update_xaxes(title_text=(f'p={stat2}'), row=2, col=1)
        else:
            box_plot.update_xaxes(title_text=(f'p<0.0001'), row=2, col=1)
        if stat3 > 0.001:
            box_plot.update_xaxes(title_text=(f'p={stat3}'), row=1, col=2)
        else:
            box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=2)
        if stat4 > 0.001:
            box_plot.update_xaxes(title_text=(f'p={stat4}'), row=2, col=2)
        else:
            box_plot.update_xaxes(title_text=(f'p<0.0001'), row=2, col=2)
        if stat5 > 0.001:
            box_plot.update_xaxes(title_text=(f'p={stat5}'), row=1, col=3)
        else:
            box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=3)
        if stat6 > 0.001:
            box_plot.update_xaxes(title_text=(f'p={stat6}'), row=2, col=3)
        else:
            box_plot.update_xaxes(title_text=(f'p<0.0001'), row=2, col=3)
        if stat7 > 0.001:
            box_plot.update_xaxes(title_text=(f'p={stat7}'), row=1, col=4)
        else:
            box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=4)
        if stat8 > 0.001:
            box_plot.update_xaxes(title_text=(f'p={stat8}'), row=2, col=4)
        else:
            box_plot.update_xaxes(title_text=(f'p<0.0001'), row=2, col=4)
        return box_plot


@callback(
    Output('btn-nclicks-3', 'href'),
    Input('btn-nclicks-3','n_clicks'),
    Input('Table3','selected_rows')
)
def display_page_contents(n_clicks,selected_rows):
    # Logic to extract the parameters you need from the pathname. This could vary if you are using a multi-page app, for example
    if len(selected_rows) > 0 & n_clicks >= 0:
        value = genelist[selected_rows]
        s = value
        n = ''.join([str(elem) for elem in s])
        string = 'https://ucsci.uchc.edu/bonebase/GeneEntry.html?GeneSymbol=Irf8+MicroCT_VertTrab'
        pathname = string.replace('Irf8', n)
        print(pathname)
        return (pathname)
    elif n_clicks==1 & len(selected_rows)== 0:
        return 'https://ucsci.uchc.edu/bonebase/GeneEntry.html?GeneSymbol=Irf8+MicroCT_VertTrab'

    else:
        raise dash.exceptions.PreventUpdate

