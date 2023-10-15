import plotly.graph_objects as go
import pandas as pd
import dash
from dash import dash_table
from dash import html,callback,Input,Output
import dash_bootstrap_components as dbc
from dash import dcc
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
from scipy.stats import ttest_ind

import pathlib
dash.register_page(__name__, path='/HOMO_HISTO_FTRAB_OC')
from pages.Homoscroll import scroll_layout
from pages.Collapse_Osteoclast import layout_OC

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath('../datasets/KOMP220').resolve()

#Control Femur Data
controlfemaleFemur_df=pd.read_csv(DATA_PATH.joinpath('controlfemale_femurHistoIM.csv'))
controlmaleFemur_df=pd.read_csv(DATA_PATH.joinpath('controlmale_femurHistoIM.csv'))

#Homozygous Mutant Femur Data
femaleFemur_df=pd.read_csv(DATA_PATH.joinpath('female_femurHistoIM.csv'))
maleFemur_df=pd.read_csv(DATA_PATH.joinpath('male_femurHistoIM.csv'))
data1= pd.read_csv(DATA_PATH.joinpath('Histofemale_Femur_average.csv'))
data2= pd.read_csv(DATA_PATH.joinpath('Histomale_Femur_average.csv'))


ratio_df=pd.DataFrame(columns=['Gene Symbol', 'Female Femur', 'Male Femur'])

#calculating the average MAR of control groups
FemaleFemur_Count=controlfemaleFemur_df['TRAP_BS'].count()
FFlist=controlfemaleFemur_df['TRAP_BS'].dropna().to_list()
FF_TRAPave=(sum(FFlist)/(FemaleFemur_Count))

MaleFemur_Count=controlmaleFemur_df['TRAP_BS'].count()
MFlist=controlmaleFemur_df['TRAP_BS'].dropna().to_list()
MF_TRAPave=(sum(MFlist)/(MaleFemur_Count))


ratio_df['Gene Symbol']=data1['gene_symbol']
ratio_df['Female Femur']=((((data1['TRAP_BS'])/FF_TRAPave)-1)*100)
ratio_df['Male Femur']=((((data2['TRAP_BS'])/MF_TRAPave)-1)*100)


BoneType = ['Female Femur', 'Male Femur']
ratio_df=ratio_df.round(2)

genelist=ratio_df['Gene Symbol']

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


def layout():
    return dbc.Container([
        dbc.Row(scroll_layout()),
dbc.Col([
    # row  2
    dbc.Row(
        [html.H1('Femur Osteoclast Histomorphometric Analyses of Global Homozygous KO Mice',
                        style={'color': 'black', 'fontSize': 25,'fontFamily': "Verdana","font-weight":"600",
                               'margin-left':30}),

        ], style={'height': 60, 'padding-top': 15, 'margin-bottom':20, 'margin-left':0, 'margin-right':-100},

    ),
    # row  3
    dbc.Row([
        dbc.Col([
            html.Div([
                html.P("% Increase/Decrease in TRAP/BS", style={'font-family':'arial', 'font-weight':'bold', 'padding-left':50, 'padding-bottom':0, 'margin-bottom':0}),
                dash_table.DataTable(
                    id='Table6',
                    data=ratio_df.to_dict('records'),
                    sort_action='native',
                    row_selectable='single',
                    selected_rows=[],
                    columns=[{'name':'Gene Symbol', 'id': 'Gene Symbol', 'type': 'text', 'editable': False},
                            {'name':'Female Femur', 'id': 'Female Femur','type':'numeric','editable':False},
                            {'name': 'Male Femur', 'id': 'Male Femur', 'type':'numeric','editable':False}],
                            # {'name':'Female Vertebra', 'id': 'Female Vertebra', 'type': 'numeric', 'editable': False},
                            # {'name':'Male Vertebra', 'id': 'Male Vertebra', 'type': 'numeric', 'editable': False}],


                    style_data_conditional=[
            # {'if': {
            #     'filter_query': '{Female Vertebra} >= 10.0',
            #     'column_id': 'Female Vertebra'},
            # 'backgroundColor': 'tomato',
            # 'color': 'white'
            # },
            {'if': {
                'filter_query': '{Female Femur} >= 29.0',
                'column_id': 'Female Femur'},
            'backgroundColor': 'tomato',
            'color': 'white'
            },
            {'if': {
                'filter_query': '{Male Femur} >= 31.0',
                'column_id': 'Male Femur'},
            'backgroundColor': 'tomato',
            'color': 'white'
            },
            # {'if': {
            #     'filter_query': '{Male Vertebra} >= 10.0',
            #     'column_id': 'Male Vertebra'},
            # 'backgroundColor': 'tomato',
            # 'color': 'white'
            # },

        {
            'if': {
                'filter_query': '{Female Femur} <= -30.0',
                'column_id': 'Female Femur'},
            'backgroundColor': 'dodgerblue',
            'color': 'white',
         },
            {'if': {
                'filter_query': '{Male Femur} <= -30.0',
                'column_id': 'Male Femur'},
            'backgroundColor': 'dodgerblue',
            'color': 'white'
            },
        # {
        #     'if': {
        #         'filter_query': '{Female Vertebra} <= -10.0',
        #         'column_id': 'Female Vertebra'},
        #     'backgroundColor': 'dodgerblue',
        #     'color': 'white',
        #  },
        #     {'if': {
        #         'filter_query': '{Male Vertebra} <= -10.0',
        #         'column_id': 'Male Vertebra'},
        #     'backgroundColor': 'dodgerblue',
        #     'color': 'white'
        #     }
                                ],
            style_cell={'padding': '5px', 'font_family': 'arial','font_size': '13px',
                        'text_align': 'left'},
            style_cell_conditional=[{'if': {'column_id': 'Gene Symbol'},
                                         'fontWeight':'bold'
                                   }],
            style_header={'backgroundColor': 'white','fontWeight': 'bold'},
            page_action='native',
            page_size=35,

            ), ]),

        ],width=4),

        # dbc.Col([], width=1),
        dbc.Col([
            dbc.Row([
                        dcc.Graph(id='box_plot8', config={'modeBarButtonsToRemove': ['pan2d', 'displaylogo','autoScale2d','resetScale2d',
                        'hoverClosestCartesian','lasso2d','zoomIn2d','zoomOut2d','zoom2d','select2d','toggleSpikelines',
                        'hoverCompareCartesian','toggleHover'],'displayModeBar': True, 'displaylogo': False,
                        'toImageButtonOptions':{'format': 'png'}}) #'displayModeBar': False
                ], style={'margin-left':5}),
            dbc.Row([],style={'height': 3, 'padding-bottom':0, 'padding-top': 0, 'margin-bottom':15, 'margin-left':75,'margin-right':-85, 'background-color':'black'}),


            dbc.Row([
                        dcc.Graph(id='box_plot9', config={'modeBarButtonsToRemove': ['pan2d', 'displaylogo','autoScale2d','resetScale2d',
                        'hoverClosestCartesian','lasso2d','zoomIn2d','zoomOut2d','zoom2d','select2d','toggleSpikelines',
                        'hoverCompareCartesian','toggleHover'],'displayModeBar': True, 'displaylogo': False,
                        'toImageButtonOptions':{'format': 'png'}}) #'displayModeBar': False

            ],style={'margin-left':5}),
                 ], width=8),


     ], style={'height': 1200, 'padding-bottom': 0, 'padding-top': 0, 'margin-top':-15,'margin-bottom':0,'justify':'center'}),

    dbc.Row([
        dbc.Col([html.P('Numbers represent the % increase or decrease in TRAP labeling relative to the '
                        'bone surface based on calculating ((TRAP/BS mutant/ TRAP/BS control)-1)x100',
                        style={'color': 'black', 'fontSize': 12,'fontFamily': "Verdana",
                               'margin-top':-40}),
                ], width=4),
        dbc.Col([html.P('P values were calculated based on the outcomes of a two sample t-test',
                        style={'color': 'black', 'fontSize': 12,'fontFamily': "Verdana",
                               'margin-left':50, 'marginRight':-30,'marginTop':20, 'textAlign':'center'}),
                # html.A('[Guide: Measurement Definitions]', style={'textAlign': 'right', 'fontFamily': "Verdana", 'color': 'black',
                #             "font-size": 12, "font-weight": 'normal', 'line-height': 15,'margin-top': 5, 'margin-left':150},
                #             href ='http://bonebase.org/08_DataInterpretation/MicroCt_Cortical.html'),
                ], width=3, style={'marginLeft':40, 'marginRight':-20}),
        dbc.Col([
            html.Div([
                dbc.Button(
                    'Histomorphometry Images',
                    id='btn-nclicks-6',
                    className="mx-2",
                    style=CT,
                    n_clicks=0,
                    href='https://ucsci.uchc.edu/bonebase/GeneEntry.html?GeneSymbol=Irf8+Histo_FemurTrab',
                    target='_blank',
                    external_link=True
                ),
                ],style={'marginLeft':30}),
        ],width=2,style={'margin-left':80, 'margin-top':20}),

        dbc.Col(html.Div([layout_OC()], style={'margin-top': 60, 'margin-left': -100}),
                width=2, style={'margin-left':-60}),

        ], style={'height': 60, 'padding-bottom': 0, 'padding-top': 0, 'margin-bottom':0})

],md=12,style={'margin-left':-100})

],style={'margin-left':-50})

@callback(
    Output(component_id='box_plot8', component_property='figure'),
    Input(component_id='Table6', component_property='selected_rows')
    )
    # selected_rows provides a row index number. It was a challenge to use this as a callback.
    # The simple solution was to create a list and use the number from selected rows to determine the
    # gene symbol in the list based on its index. This provided the corrected gene symbol (value) which
    # was fed in to filter the dataframe to select the bvtv data for that gene.  The second challenge was converting
    # that list item into a string so the plot would show its name at the bottom. This was done by: n=''.join([str(elem) for elem in s])
def update_boxplots(selected_rows):
        if len(selected_rows) == 0:
            df_filtered = femaleFemur_df[femaleFemur_df['gene_symbol'].isin(['Irf8'])]
            df_filtered_MF = maleFemur_df[maleFemur_df['gene_symbol'].isin(['Irf8'])]

            # df_filtered_FV = femaleVert_df[femaleVert_df['gene_symbol'].isin(['Alg3'])]
            # df_filtered_MV = maleVert_df[maleVert_df['gene_symbol'].isin(['Alg3'])]

            trapbs = df_filtered['TRAP_BS'].dropna()
            trapbs2 = df_filtered_MF['TRAP_BS'].dropna()
            traplbs = df_filtered['TRAP_L_BS'].dropna()
            traplbs2 = df_filtered_MF['TRAP_L_BS'].dropna()
            trapnlbs = df_filtered['TRAP_NL_BS'].dropna()
            trapnlbs2 = df_filtered_MF['TRAP_NL_BS'].dropna()

            y = trapbs
            y1 = controlfemaleFemur_df['TRAP_BS'].dropna()
            y2 = trapbs2
            y3 = controlmaleFemur_df['TRAP_BS'].dropna()
            y4 = traplbs
            y5 = controlfemaleFemur_df['TRAP_L_BS'].dropna()
            y6 = traplbs2
            y7 = controlmaleFemur_df['TRAP_L_BS'].dropna()
            y8 = trapnlbs
            y9 = controlfemaleFemur_df['TRAP_NL_BS'].dropna()
            y10 = trapnlbs2
            y11 = controlmaleFemur_df['TRAP_NL_BS'].dropna()

            name = "Irf8 -/-"

            t1, p1 = ttest_ind(y, y1)
            t2, p2 = ttest_ind(y2, y3)
            t3, p3 = ttest_ind(y4, y5)
            t4, p4 = ttest_ind(y6, y7)
            t5, p5 = ttest_ind(y8, y9)
            t6, p6 = ttest_ind(y10, y11)

            stat1 = round(p1, 5)
            stat2 = round(p2, 5)
            stat3 = round(p3, 5)
            stat4 = round(p4, 5)
            stat5 = round(p5, 5)
            stat6 = round(p6, 5)

        else:
            value = genelist[selected_rows]
            df_filtered = femaleFemur_df[femaleFemur_df['gene_symbol'].isin(value)]
            df_filtered_MF = maleFemur_df[maleFemur_df['gene_symbol'].isin(value)]
            # df_filtered_FV = femaleVert_df[femaleVert_df['gene_symbol'].isin(value)]
            # df_filtered_MV = maleVert_df[maleVert_df['gene_symbol'].isin(value)]

            trapbs = df_filtered['TRAP_BS'].dropna()
            trapbs2 = df_filtered_MF['TRAP_BS'].dropna()
            traplbs = df_filtered['TRAP_L_BS'].dropna()
            traplbs2 = df_filtered_MF['TRAP_L_BS'].dropna()
            trapnlbs = df_filtered['TRAP_NL_BS'].dropna()
            trapnlbs2 = df_filtered_MF['TRAP_NL_BS'].dropna()

            y = trapbs
            y1 = controlfemaleFemur_df['TRAP_BS'].dropna()
            y2 = trapbs2
            y3 = controlmaleFemur_df['TRAP_BS'].dropna()
            y4 = traplbs
            y5 = controlfemaleFemur_df['TRAP_L_BS'].dropna()
            y6 = traplbs2
            y7 = controlmaleFemur_df['TRAP_L_BS'].dropna()
            y8 = trapnlbs
            y9 = controlfemaleFemur_df['TRAP_NL_BS'].dropna()
            y10 = trapnlbs2
            y11 = controlmaleFemur_df['TRAP_NL_BS'].dropna()

            s = value
            n = ''.join([str(elem) for elem in s])
            name = n + '-/-'

            t1, p1 = ttest_ind(y, y1)
            t2, p2 = ttest_ind(y2, y3)
            t3, p3 = ttest_ind(y4, y5)
            t4, p4 = ttest_ind(y6, y7)
            t5, p5 = ttest_ind(y8, y9)
            t6, p6 = ttest_ind(y10, y11)

            stat1 = p1.round(5)
            stat2 = p2.round(5)
            stat3 = p3.round(5)
            stat4 = p4.round(5)
            stat5 = p5.round(5)
            stat6 = p6.round(5)

        box_plot = make_subplots(rows=2, cols=3,
            specs=[[{},{},{}],[{},{},{}]], vertical_spacing= 0.2,
            # for colspan and rowspan default is 1 col or 1 row so setting up the spect like this
            #defines a 2x4 subplot
            subplot_titles=("<b>TRAP/BS </b> (%)", "<b>TRAP<sub>L</sub>/BS</b> (%)","<b>TRAP<sub>NL</sub>/BS</b> (%)",
                            "<b>TRAP/BS</b> (%)","<b>TRAP<sub>L</sub>/BS</b> (%)","<b>TRAP<sub>NL</sub>/BS</b> (%)"))

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



        box_plot.update_layout(height=600, width=900, margin={'t': 30},plot_bgcolor='white',font_family='Arial')
        box_plot.update_yaxes(title_text="<b>Female</b>", row=1, col=1,gridcolor='#D3D3D3', title_font=dict(size=18,family='Arial'),tickfont=dict(size=14), range=[0,60])
        box_plot.update_yaxes(row=2, col=1,title_text="<b>Male</b>",gridcolor='#D3D3D3',title_font=dict(size=18,family='Arial'),tickfont=dict(size=14),range=[0,60])
        box_plot.update_yaxes(row=1, col=2,gridcolor='#D3D3D3',tickfont=dict(size=14),range=[0,50])
        box_plot.update_yaxes(row=2, col=2,gridcolor='#D3D3D3',tickfont=dict(size=14),range=[0,50])
        box_plot.update_yaxes(row=1, col=3,gridcolor='#D3D3D3',tickfont=dict(size=14),range=[0,30])
        box_plot.update_yaxes(row=2, col=3,gridcolor='#D3D3D3',tickfont=dict(size=14),range=[0,30])

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

        return box_plot


@callback(
    Output(component_id='box_plot9', component_property='figure'),
    Input(component_id='Table6', component_property='selected_rows')
    )
def update_boxplots(selected_rows):
    if len(selected_rows) == 0:
        df_filtered = femaleFemur_df[femaleFemur_df['gene_symbol'].isin(['Irf8'])]
        df_filtered_MF = maleFemur_df[maleFemur_df['gene_symbol'].isin(['Irf8'])]

        aptrap = df_filtered['AP_TRAP_R_RG_BS'].dropna()
        aptrap2 = df_filtered_MF['AP_TRAP_R_RG_BS'].dropna()
        trapontrap = df_filtered['TRAP_on_TRAP'].dropna()
        trapontrap2 = df_filtered_MF['TRAP_on_TRAP'].dropna()
        trapltrapon = df_filtered['TRAP_L_TRAP_on'].dropna()
        trapltrapon2 = df_filtered_MF['TRAP_L_TRAP_on'].dropna()
        trapnltrapon = df_filtered['TRAP_NL_TRAP_on'].dropna()
        trapnltrapon2 = df_filtered_MF['TRAP_NL_TRAP_on'].dropna()

        y16 = aptrap
        y17 = controlfemaleFemur_df['AP_TRAP_R_RG_BS'].dropna()
        y18 = aptrap2
        y19 = controlmaleFemur_df['AP_TRAP_R_RG_BS'].dropna()
        y20 = trapontrap
        y21 = controlfemaleFemur_df['TRAP_on_TRAP'].dropna()
        y22 = trapontrap2
        y23 = controlmaleFemur_df['TRAP_on_TRAP'].dropna()
        y24 = trapltrapon
        y25 = controlfemaleFemur_df['TRAP_L_TRAP_on'].dropna()
        y26 = trapltrapon2
        y27 = controlmaleFemur_df['TRAP_L_TRAP_on'].dropna()
        y28 = trapnltrapon
        y29 = controlfemaleFemur_df['TRAP_NL_TRAP_on'].dropna()
        y30 = trapnltrapon2
        y31 = controlmaleFemur_df['TRAP_NL_TRAP_on'].dropna()

        name = "Irf8 -/-"

        t9, p9 = ttest_ind(y16, y17)
        t10, p10 = ttest_ind(y18, y19)
        t11, p11 = ttest_ind(y20, y21)
        t12, p12 = ttest_ind(y22, y23)
        t13, p13 = ttest_ind(y24, y25)
        t14, p14 = ttest_ind(y26, y27)
        t15, p15 = ttest_ind(y28, y29)
        t16, p16 = ttest_ind(y30, y31)

        stat9 = p9.round(5)
        stat10 = p10.round(5)
        stat11 = p11.round(5)
        stat12 = p12.round(5)
        stat13 = p13.round(5)
        stat14 = p14.round(5)
        stat15 = p15.round(5)
        stat16 = p16.round(5)

    else:
        value = genelist[selected_rows]
        df_filtered = femaleFemur_df[femaleFemur_df['gene_symbol'].isin(value)]
        df_filtered_MF = maleFemur_df[maleFemur_df['gene_symbol'].isin(value)]

        aptrap = df_filtered['AP_TRAP_R_RG_BS'].dropna()
        aptrap2 = df_filtered_MF['AP_TRAP_R_RG_BS'].dropna()
        trapontrap = df_filtered['TRAP_on_TRAP'].dropna()
        trapontrap2 = df_filtered_MF['TRAP_on_TRAP'].dropna()
        trapltrapon = df_filtered['TRAP_L_TRAP_on'].dropna()
        trapltrapon2 = df_filtered_MF['TRAP_L_TRAP_on'].dropna()
        trapnltrapon = df_filtered['TRAP_NL_TRAP_on'].dropna()
        trapnltrapon2 = df_filtered_MF['TRAP_NL_TRAP_on'].dropna()

        y16 = aptrap
        y17 = controlfemaleFemur_df['AP_TRAP_R_RG_BS'].dropna()
        y18 = aptrap2
        y19 = controlmaleFemur_df['AP_TRAP_R_RG_BS'].dropna()
        y20 = trapontrap
        y21 = controlfemaleFemur_df['TRAP_on_TRAP'].dropna()
        y22 = trapontrap2
        y23 = controlmaleFemur_df['TRAP_on_TRAP'].dropna()
        y24 = trapltrapon
        y25 = controlfemaleFemur_df['TRAP_L_TRAP_on'].dropna()
        y26 = trapltrapon2
        y27 = controlmaleFemur_df['TRAP_L_TRAP_on'].dropna()
        y28 = trapnltrapon
        y29 = controlfemaleFemur_df['TRAP_NL_TRAP_on'].dropna()
        y30 = trapnltrapon2
        y31 = controlmaleFemur_df['TRAP_NL_TRAP_on'].dropna()

        s = value
        n = ''.join([str(elem) for elem in s])
        name = n + '-/-'


        t9, p9 = ttest_ind(y16, y17)
        t10, p10 = ttest_ind(y18, y19)
        t11, p11 = ttest_ind(y20, y21)
        t12, p12 = ttest_ind(y22, y23)
        t13, p13 = ttest_ind(y24, y25)
        t14, p14 = ttest_ind(y26, y27)
        t15, p15 = ttest_ind(y28, y29)
        t16, p16 = ttest_ind(y30, y31)

        stat9 = p9.round(5)
        stat10 = p10.round(5)
        stat11 = p11.round(5)
        stat12 = p12.round(5)
        stat13 = p13.round(5)
        stat14 = p14.round(5)
        stat15 = p15.round(5)
        stat16 = p16.round(5)


    box_plot = make_subplots(rows=2, cols=4,
        specs=[[{}, {}, {}, {}], [{}, {}, {}, {}]], vertical_spacing=0.2,
        # for colspan and rowspan default is 1 col or 1 row so setting up the spect like this
        # defines a 2x4 subplot
        subplot_titles=("<b>AP<sub>L</sub>-TRAP<sub>L</sub>/BS</b> (%)", "<b>TRAP<sub>BS</sub>/TRAP</b> (%)","<b>TRAP<sub>L</sub>/TRAP<sub>BS</sub></b> (%)", '<b>TRAP<sub>NL</sub>/TRAP<sub>BS</sub></b> (%)',
                        "<b>AP<sub>L</sub>-TRAP<sub>L</sub>/BS</b> (%)", "<b>TRAP<sub>BS</sub>/TRAP</b> (%)","<b>TRAP<sub>L</sub>/TRAP<sub>BS</sub></b> (%)",'<b>TRAP<sub>NL</sub>/TRAP<sub>BS</sub></b> (%)'))


    box_plot.add_trace(go.Box(y=y16, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, showlegend=False), row=1, col=1)
    box_plot.add_trace(go.Box(y=y17, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, showlegend=False), row=1, col=1)
    box_plot.add_trace(go.Box(y=y18, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, showlegend=False), row=2, col=1)
    box_plot.add_trace(go.Box(y=y19, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, showlegend=False), row=2, col=1)
    box_plot.add_trace(go.Box(y=y20, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, showlegend=False), row=1, col=2)
    box_plot.add_trace(go.Box(y=y21, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, showlegend=False), row=1, col=2)
    box_plot.add_trace(go.Box(y=y22, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, showlegend=False), row=2, col=2)
    box_plot.add_trace(go.Box(y=y23, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, showlegend=False), row=2, col=2)
    box_plot.add_trace(go.Box(y=y24, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, showlegend=False), row=1, col=3)
    box_plot.add_trace(go.Box(y=y25, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, showlegend=False), row=1, col=3)
    box_plot.add_trace(go.Box(y=y26, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, showlegend=False), row=2, col=3)
    box_plot.add_trace(go.Box(y=y27, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, showlegend=False), row=2, col=3)
    box_plot.add_trace(go.Box(y=y28, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, showlegend=False), row=1, col=4)
    box_plot.add_trace(go.Box(y=y29, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, showlegend=False), row=1, col=4)
    box_plot.add_trace(go.Box(y=y30, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#f39c12', pointpos=0, showlegend=False), row=2, col=4)
    box_plot.add_trace(go.Box(y=y31, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                                  marker_color='#2c3e50', pointpos=0, showlegend=False), row=2, col=4)

    box_plot.update_layout(height=600, width=900, margin={'t': 30},plot_bgcolor='white',font_family='Arial')
    box_plot.update_yaxes(title_text="<b>Female</b>", row=1, col=1,gridcolor='#D3D3D3', title_font=dict(size=18,family='Arial'),tickfont=dict(size=14), range=[0,30])
    box_plot.update_yaxes(row=2, col=1,title_text="<b>Male</b>",gridcolor='#D3D3D3',title_font=dict(size=18,family='Arial'),tickfont=dict(size=14),range=[0,30])
    box_plot.update_yaxes(row=1, col=2,gridcolor='#D3D3D3',tickfont=dict(size=14),range=[0,100])
    box_plot.update_yaxes(row=2, col=2,gridcolor='#D3D3D3',tickfont=dict(size=14),range=[0,100])
    box_plot.update_yaxes(row=1, col=3,gridcolor='#D3D3D3',tickfont=dict(size=14),range=[0,100])
    box_plot.update_yaxes(row=2, col=3,gridcolor='#D3D3D3',tickfont=dict(size=14),range=[0,100])
    box_plot.update_yaxes(row=1, col=4,gridcolor='#D3D3D3',tickfont=dict(size=14),range=[0,100])
    box_plot.update_yaxes(row=2, col=4,gridcolor='#D3D3D3',tickfont=dict(size=14),range=[0,100])

    box_plot.update_xaxes(showline=True, linewidth=2, linecolor='#666A6D')
    box_plot.update_yaxes(showline=True, linewidth=2, linecolor='#666A6D')

    if stat9 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat9}'), row=1, col=1)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=1)
    if stat10 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat10}'), row=2, col=1)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=2, col=1)
    if stat11 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat11}'), row=1, col=2)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=2)
    if stat12 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat12}'), row=2, col=2)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=2, col=2)
    if stat13 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat13}'), row=1, col=3)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=3)
    if stat14 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat14}'), row=2, col=3)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=2, col=3)
    if stat15 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat15}'), row=1, col=4)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=4)
    if stat16 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat16}'), row=2, col=4)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=2, col=4)


    return box_plot

@callback(
    Output('btn-nclicks-6', 'href'),
    Input('btn-nclicks-6','n_clicks'),
    Input('Table6','selected_rows')
)
def display_page_contents(n_clicks,selected_rows):
    # Logic to extract the parameters you need from the pathname. This could vary if you are using a multi-page app, for example
    if len(selected_rows) > 0 & n_clicks >= 0:
        value = genelist[selected_rows]
        s = value
        n = ''.join([str(elem) for elem in s])
        string = 'https://ucsci.uchc.edu/bonebase/GeneEntry.html?GeneSymbol=Irf8+Histo_FemurTrab'
        pathname = string.replace('Irf8', n)
        print(pathname)
        return (pathname)
    elif n_clicks==1 & len(selected_rows)== 0:
        return 'https://ucsci.uchc.edu/bonebase/GeneEntry.html?GeneSymbol=Irf8+Histo_FemurTrab'

    else:
        raise dash.exceptions.PreventUpdate


