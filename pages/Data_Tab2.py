import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback,Input, Output
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
from scipy.stats import ttest_ind

import pathlib

dash.register_page(__name__,path='/Data_Tab2.py')
from .Homoscroll import scroll_layout

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath('../datasets/KOMP220').resolve()

#Control Data
controlfemaleFemur_df=pd.read_csv(DATA_PATH.joinpath('controlfemale_femurIM.csv'))
controlfemaleFemur_df=controlfemaleFemur_df.dropna()
controlmaleFemur_df=pd.read_csv(DATA_PATH.joinpath('controlmale_femurIM.csv'))
controlmaleFemur_df=controlmaleFemur_df.dropna()
controlfemaleFemurCort_df=pd.read_csv(DATA_PATH.joinpath('controlfemale_CortIM.csv'))
# controlfemaleFemur_df=controlfemaleFemur_df.dropna()
controlmaleFemurCort_df=pd.read_csv(DATA_PATH.joinpath('controlmale_CorticalIM.csv'))
# controlmaleFemur_df=controlmaleFemur_df.dropna()
controlfemaleVertebra_df=pd.read_csv(DATA_PATH.joinpath('controlfemaleVertebraIM.csv'))
controlfemaleVertebra_df=controlfemaleVertebra_df.dropna()
controlmaleVertebra_df=pd.read_csv(DATA_PATH.joinpath('controlmaleVertebraIM.csv'))
controlmaleVertebra_df=controlmaleVertebra_df.dropna()
conHISTOfemaleFemur_df=pd.read_csv(DATA_PATH.joinpath('controlfemale_femurHistoIM.csv'))
conHISTOmaleFemur_df=pd.read_csv(DATA_PATH.joinpath('controlmale_femurHistoIM.csv'))
controlfemaleHISTOVert_df=pd.read_csv(DATA_PATH.joinpath('controlfemale_vertHistoIM.csv'))
controlmaleHISTOVert_df=pd.read_csv(DATA_PATH.joinpath('controlmale_vertHistoIM.csv'))

#Homozygous Mutant Data
femaleFemur_df=pd.read_csv(DATA_PATH.joinpath('female_femurIM.csv'))
maleFemur_df=pd.read_csv(DATA_PATH.joinpath('male_femurIM.csv'))
femaleFemurCort_df=pd.read_csv(DATA_PATH.joinpath('female_femurCorticalIM.csv'))
maleFemurCort_df=pd.read_csv(DATA_PATH.joinpath('male_femurCorticalIM.csv'))
femaleVert_df=pd.read_csv(DATA_PATH.joinpath('femaleVertebraIM.csv'))
maleVert_df=pd.read_csv(DATA_PATH.joinpath('maleVertebraIM.csv'))
HISTOfemaleFemur_df=pd.read_csv(DATA_PATH.joinpath('female_femurHistoIM.csv'))
HISTOmaleFemur_df=pd.read_csv(DATA_PATH.joinpath('male_femurHistoIM.csv'))
femaleHISTOVert_df=pd.read_csv(DATA_PATH.joinpath('female_vertHistoIM.csv'))
maleHISTOVert_df=pd.read_csv(DATA_PATH.joinpath('male_vertHistoIM.csv'))


genelist=femaleFemur_df['gene_symbol'].drop_duplicates().to_list()

tabs_styles = {
    'height': '44px'
}
CTtab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'fontWeight': 'bold',
    'border-top-left-radius':20,
    'border-top-right-radius':20,
    'backgroundColor': '#176d9d',
    'color':'white'
}
HISTOtab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'fontWeight': 'bold',
    'border-top-left-radius':20,
    'border-top-right-radius':20,
    'backgroundColor': '#053465',
    'color':'white'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'backgroundColor': '#FFF',
    'color': 'black',
    'border-top-left-radius':20,
    'border-top-right-radius':20,
    }
def layout():
    return dbc.Container([
        dbc.Row(scroll_layout()),
    dbc.Col([
    html.Br(),
    dbc.Row([
        dbc.Col([
        html.H5('Please Type in Your Gene Symbol and Hit Enter:'),
            ],width=6),
        dbc.Col([
        html.Div(
        dcc.Input(
            id="gs",
            type='text',
            placeholder='gene symbol',
            style={'text-align':'center','font-family':'Arial','font-weight':'600'},
            debounce=True,
            n_submit=0,
            value=''),
        ),
            ],width=2, style={'margin-left':-20}),
    html.Div(id='tabs-content-example-graph2'),
        ], style={'height': 30, 'margin-left':150, 'padding-bottom': 0, 'padding-top': 0, 'margin-bottom':0}),
    html.Div(id='my-output'),
    html.Br(),
    dbc.Row( id='subtitles',children=[
        dbc.Col([html.H4('μCT Data')],style={'text-align':'center'}, width=4),
        dbc.Col([],width=1),
        dbc.Col([html.H4('Histomorphometry Data')],style={'text-align':'center'},width=7),
    ],style={'padding-left':10, 'color':'#55575c','font-family': 'Playfair Display'}),
    dbc.Row(
        html.Div([
            dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph',
            children=[
                dcc.Tab(label='Femur Trabecular Bone', value='tab1-graph',style=CTtab_style, selected_style=tab_selected_style),
                dcc.Tab(label='Femur Cortical Bone', value='tab2-graph', style=CTtab_style, selected_style=tab_selected_style),
                dcc.Tab(label='Vertebra Trabecular Bone', value='tab3-graph',style=CTtab_style, selected_style=tab_selected_style),
                dcc.Tab(label='Femur Trabecular Bone Static', value='tab4-graph',style=HISTOtab_style, selected_style=tab_selected_style),
                dcc.Tab(label='Femur Trabecular Bone Osteoblast', value='tab5-graph',style=HISTOtab_style, selected_style=tab_selected_style),
                dcc.Tab(label='Femur Trabecular Bone Osteoclast', value='tab6-graph',style=HISTOtab_style, selected_style=tab_selected_style),
                dcc.Tab(label='Vertebra Trabecular Bone Static', value='tab7-graph',style=HISTOtab_style, selected_style=tab_selected_style),
                dcc.Tab(label='Vertebra Trabecular Bone Osteoblast', value='tab8-graph',style=HISTOtab_style, selected_style=tab_selected_style),
                dcc.Tab(label='Vertebra Trabecular Bone Osteoclast', value='tab9-graph',style=HISTOtab_style, selected_style=tab_selected_style),
            ],vertical=False, style={'font-family':'Arial', 'font-weight':'600'},
            ),

        html.Div(id='tabs-content-example-graph', style={'margin-left':-70}),

    ],style={'height':1000})
    ),


        # html.Div(
        #     html.H3('Please Select Tab to View Data'),
        # )

],md=12,style={'margin-left':-50})
])


#callback to notify user that mouse line for input gene symbol has not been analyzed
@callback(
    Output('tabs-content-example-graph2', 'children'),
    Input(component_id='gs', component_property='value')
    )
def update_input (value):
    if len(value) == 0:
        return ""
    elif value in genelist:
        return ""
    else:
        return html.H5("The Mouse Line For This Gene Has Not Been Analyzed", style={'color':'red'})


@callback(
    Output(component_id='box_plot30', component_property='figure'),
    Input(component_id='gs', component_property='value')
    )

def update_boxplots(value):
    if len(value) == 0:
        df_filtered = femaleFemur_df[femaleFemur_df['gene_symbol'].isin(['Irf8'])]
        df_filtered_MF = maleFemur_df[maleFemur_df['gene_symbol'].isin(['Irf8'])]

        bvtv = df_filtered['BV/TV']
        bvtv2 = df_filtered_MF['BV/TV']
        TbN = df_filtered['Tb.N']
        TbN2 = df_filtered_MF['Tb.N']
        TbTh = df_filtered['Tb.Th']
        TbTh2 = df_filtered_MF['Tb.Th']
        TbSp = df_filtered['Tb.Sp']
        TbSp2 = df_filtered_MF['Tb.Sp']

        y = bvtv
        y1 = controlfemaleFemur_df['BV/TV']
        y2 = bvtv2
        y3 = controlmaleFemur_df['BV/TV']
        y4 = TbN
        y5 = controlfemaleFemur_df['Tb.N']
        y6 = TbN2
        y7 = controlmaleFemur_df['Tb.N']
        y8 = TbTh
        y9 = controlfemaleFemur_df['Tb.Th']
        y10 = TbTh2
        y11 = controlmaleFemur_df['Tb.Th']
        y12 = TbSp
        y13 = controlfemaleFemur_df['Tb.Sp']
        y14 = TbSp2
        y15 = controlmaleFemur_df['Tb.Sp']

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
    # elif genelist.isin([value])==False:
    #     raise dash.exceptions.PreventUpdate

    else:
        df_filtered = femaleFemur_df[femaleFemur_df['gene_symbol'].isin([value])]
        df_filtered_MF = maleFemur_df[maleFemur_df['gene_symbol'].isin([value])]

        bvtv = df_filtered['BV/TV']
        bvtv2 = df_filtered_MF['BV/TV']
        TbN = df_filtered['Tb.N']
        TbN2 = df_filtered_MF['Tb.N']
        TbTh = df_filtered['Tb.Th']
        TbTh2 = df_filtered_MF['Tb.Th']
        TbSp = df_filtered['Tb.Sp']
        TbSp2 = df_filtered_MF['Tb.Sp']

        y = bvtv
        y1 = controlfemaleFemur_df['BV/TV']
        y2 = bvtv2
        y3 = controlmaleFemur_df['BV/TV']
        y4 = TbN
        y5 = controlfemaleFemur_df['Tb.N']
        y6 = TbN2
        y7 = controlmaleFemur_df['Tb.N']
        y8 = TbTh
        y9 = controlfemaleFemur_df['Tb.Th']
        y10 = TbTh2
        y11 = controlmaleFemur_df['Tb.Th']
        y12 = TbSp
        y13 = controlfemaleFemur_df['Tb.Sp']
        y14 = TbSp2
        y15 = controlmaleFemur_df['Tb.Sp']

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
                             specs=[[{}, {}, {}, {}], [{}, {}, {}, {}]], vertical_spacing=0.17,
                             # for colspan and rowspan default is 1 col or 1 row so setting up the spect like this
                             # defines a 4x2 subplot
                             subplot_titles=(
                             "<b>BV/TV</b> (%)", "<b>Tb.N</b> (#/mm)", "<b>Tb.Th</b> (µm)", '<b>Tb.Sp</b> (µm)',
                             "<b>BV/TV</b> (%)", "<b>Tb.N</b> (#/mm)", "<b>Tb.Th</b> (µm)", '<b>Tb.Sp</b> (µm)'))

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

    box_plot.update_layout(height=650, width=900, margin={'t': 30}, plot_bgcolor='white', font_family='Arial')
    box_plot.update_yaxes(title_text="<b>Female</b>", row=1, col=1, range=[0, 35], gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14))
    box_plot.update_yaxes(row=2, col=1, title_text="<b>Male</b>", range=[0, 35], gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14))
    box_plot.update_yaxes(row=1, col=2, range=[0, 7], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(range=[0, 7], row=2, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(row=1, col=3, range=[20, 80], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(row=2, col=3, range=[20, 80], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(row=1, col=4, range=[100, 600], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(range=[100, 600], row=2, col=4, gridcolor='#D3D3D3', tickfont=dict(size=14))

    box_plot.update_xaxes(showline=True, linewidth=2, linecolor='#666A6D')
    box_plot.update_yaxes(showline=True, linewidth=2, linecolor='#666A6D')

    if stat1 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat1}'), row=1, col=1)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=1)
    if stat2 > 0.001:
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
    Output(component_id='box_plot31', component_property='figure'),
    Input(component_id='gs', component_property='value')
)
# selected_rows provides a row index number. It was a challenge to use this as a callback.
# The simple solution was to create a list and use the number from selected rows to determine the
# gene symbol in the list based on its index. This provided the corrected gene symbol (value) which
# was fed in to filter the dataframe to select the bvtv data for that gene.  The second challenge was converting
# that list item into a string so the plot would show its name at the bottom. This was done by: n=''.join([str(elem) for elem in s])
def update_boxplots(value):
    if len(value) == 0:
        df_filtered = femaleFemurCort_df[femaleFemurCort_df['gene_symbol'].isin(['Irf8'])]
        df_filtered_MF = maleFemurCort_df[maleFemurCort_df['gene_symbol'].isin(['Irf8'])]

        # df_filtered_FV = femaleVert_df[femaleVert_df['gene_symbol'].isin(['Alg3'])]
        # df_filtered_MV = maleVert_df[maleVert_df['gene_symbol'].isin(['Alg3'])]

        TtAr = df_filtered['Tt.Ar']
        TtAr2 = df_filtered_MF['Tt.Ar']
        MaAr = df_filtered['Ma.Ar']
        MaAr2 = df_filtered_MF['Ma.Ar']
        Mask = df_filtered['Ct.Mask']
        Mask2 = df_filtered_MF['Ct.Mask']
        CtArTtAr = df_filtered['Ct.Ar_Tt.Ar']
        CtArTtAr2 = df_filtered_MF['Ct.Ar_Tt.Ar']

        y = TtAr
        y1 = controlfemaleFemurCort_df['Tt.Ar']
        y2 = TtAr2
        y3 = controlmaleFemurCort_df['Tt.Ar']
        y4 = MaAr
        y5 = controlfemaleFemurCort_df['Ma.Ar']
        y6 = MaAr2
        y7 = controlmaleFemurCort_df['Ma.Ar']
        y8 = Mask
        y9 = controlfemaleFemurCort_df['Ct.Mask']
        y10 = Mask2
        y11 = controlmaleFemurCort_df['Ct.Mask']
        y12 = CtArTtAr
        y13 = controlfemaleFemurCort_df['Ct.Ar_Tt.Ar']
        y14 = CtArTtAr2
        y15 = controlmaleFemurCort_df['Ct.Ar_Tt.Ar']

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
        df_filtered = femaleFemurCort_df[femaleFemurCort_df['gene_symbol'].isin([value])]
        df_filtered_MF = maleFemurCort_df[maleFemurCort_df['gene_symbol'].isin([value])]
        # df_filtered_FV = femaleVert_df[femaleVert_df['gene_symbol'].isin(value)]
        # df_filtered_MV = maleVert_df[maleVert_df['gene_symbol'].isin(value)]

        TtAr = df_filtered['Tt.Ar']
        TtAr2 = df_filtered_MF['Tt.Ar']
        MaAr = df_filtered['Ma.Ar']
        MaAr2 = df_filtered_MF['Ma.Ar']
        Mask = df_filtered['Ct.Mask']
        Mask2 = df_filtered_MF['Ct.Mask']
        CtArTtAr = df_filtered['Ct.Ar_Tt.Ar']
        CtArTtAr2 = df_filtered_MF['Ct.Ar_Tt.Ar']

        y = TtAr
        y1 = controlfemaleFemurCort_df['Tt.Ar']
        y2 = TtAr2
        y3 = controlmaleFemurCort_df['Tt.Ar']
        y4 = MaAr
        y5 = controlfemaleFemurCort_df['Ma.Ar']
        y6 = MaAr2
        y7 = controlmaleFemurCort_df['Ma.Ar']
        y8 = Mask
        y9 = controlfemaleFemurCort_df['Ct.Mask']
        y10 = Mask2
        y11 = controlmaleFemurCort_df['Ct.Mask']
        y12 = CtArTtAr
        y13 = controlfemaleFemurCort_df['Ct.Ar_Tt.Ar']
        y14 = CtArTtAr2
        y15 = controlmaleFemurCort_df['Ct.Ar_Tt.Ar']

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
                             specs=[[{}, {}, {}, {}], [{}, {}, {}, {}]], vertical_spacing=0.2,
                             # for colspan and rowspan default is 1 col or 1 row so setting up the spect like this
                             # defines a 2x4 subplot
                             subplot_titles=(
                             "<b>Ct.Mask </b>(mm\u00b2)", "<b>Ma.Ar </b>(mm\u00b2)", "<b>Tt.Ar </b>(mm\u00b2)",
                             '<b>Ct.Ar/Tt.Ar</b> (%)',
                             "<b>Ct.Mask </b>(mm\u00b2)", "<b>Ma.Ar </b>(mm\u00b2)", "<b>Tt.Ar </b>(mm\u00b2)",
                             '<b>Ct.Ar/Tt.Ar</b> (%)',
                             ))

    box_plot.add_trace(go.Box(y=y, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#f39c12', pointpos=0, legendgroup='a'), row=1, col=3)
    box_plot.add_trace(go.Box(y=y1, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#2c3e50', pointpos=0, legendgroup='a'), row=1, col=3)
    box_plot.add_trace(go.Box(y=y2, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#f39c12', pointpos=0, showlegend=False), row=2, col=3)
    box_plot.add_trace(go.Box(y=y3, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#2c3e50', pointpos=0, showlegend=False), row=2, col=3)
    box_plot.add_trace(go.Box(y=y4, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#f39c12', pointpos=0, showlegend=False), row=1, col=2)
    box_plot.add_trace(go.Box(y=y5, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#2c3e50', pointpos=0, showlegend=False), row=1, col=2)
    box_plot.add_trace(go.Box(y=y6, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#f39c12', pointpos=0, showlegend=False), row=2, col=2)
    box_plot.add_trace(go.Box(y=y7, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#2c3e50', pointpos=0, showlegend=False), row=2, col=2)
    box_plot.add_trace(go.Box(y=y8, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#f39c12', pointpos=0, showlegend=False), row=1, col=1)
    box_plot.add_trace(go.Box(y=y9, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#2c3e50', pointpos=0, showlegend=False), row=1, col=1)
    box_plot.add_trace(go.Box(y=y10, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#f39c12', pointpos=0, showlegend=False), row=2, col=1)
    box_plot.add_trace(go.Box(y=y11, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#2c3e50', pointpos=0, showlegend=False), row=2, col=1)
    box_plot.add_trace(go.Box(y=y12, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#f39c12', pointpos=0, showlegend=False), row=1, col=4)
    box_plot.add_trace(go.Box(y=y13, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#2c3e50', pointpos=0, showlegend=False), row=1, col=4)
    box_plot.add_trace(go.Box(y=y14, name=name, boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#f39c12', pointpos=0, showlegend=False), row=2, col=4)
    box_plot.add_trace(go.Box(y=y15, name="Control", boxpoints='all', jitter=0.3, whiskerwidth=0.2,
                              marker_color='#2c3e50', pointpos=0, showlegend=False), row=2, col=4)

    box_plot.update_layout(height=600, width=900, margin={'t': 30}, plot_bgcolor='white', font_family='Arial')
    box_plot.update_yaxes(title_text="<b>Female</b>", row=1, col=1, gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14), range=[0.4, 1.0])
    box_plot.update_yaxes(row=2, col=1, title_text="<b>Male</b>", gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14), range=[0.4, 1.0])
    box_plot.update_yaxes(row=1, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0.5, 1.5])
    box_plot.update_yaxes(row=2, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0.5, 1.5])
    box_plot.update_yaxes(row=1, col=3, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[1.0, 2.5])
    box_plot.update_yaxes(row=2, col=3, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[1.0, 2.5])
    box_plot.update_yaxes(row=1, col=4, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[25, 50])
    box_plot.update_yaxes(row=2, col=4, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[25, 50])

    box_plot.update_xaxes(showline=True, linewidth=2, linecolor='#666A6D')
    box_plot.update_yaxes(showline=True, linewidth=2, linecolor='#666A6D')
    if stat1 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat1}'), row=1, col=3)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=3)
    if stat2 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat2}'), row=2, col=3)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=2, col=3)
    if stat3 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat3}'), row=1, col=2)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=2)
    if stat4 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat4}'), row=2, col=2)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=2, col=2)
    if stat5 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat5}'), row=1, col=1)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=1)
    if stat6 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat6}'), row=2, col=1)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=2, col=1)
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
    Output(component_id='box_plot32', component_property='figure'),
    Input(component_id='gs', component_property='value')
    )

def update_boxplots(value):
    if len(value) == 0:
        df_filtered = femaleFemurCort_df[femaleFemurCort_df['gene_symbol'].isin(['Irf8'])]
        df_filtered_MF = maleFemurCort_df[maleFemurCort_df['gene_symbol'].isin(['Irf8'])]

        CtAr = df_filtered['Ct.Ar']
        CtAr2 = df_filtered_MF['Ct.Ar']
        PsPm = df_filtered['Ps.Pm']
        PsPm2 = df_filtered_MF['Ps.Pm']
        EcPm = df_filtered['Ec.Pm']
        EcPm2 = df_filtered_MF['Ec.Pm']
        CtTh = df_filtered['Ct.Th']
        CtTh2 = df_filtered_MF['Ct.Th']

        y16 = CtAr
        y17 = controlfemaleFemurCort_df['Ct.Ar']
        y18 = CtAr2
        y19 = controlmaleFemurCort_df['Ct.Ar']
        y20 = PsPm
        y21 = controlfemaleFemurCort_df['Ps.Pm']
        y22 = PsPm2
        y23 = controlmaleFemurCort_df['Ps.Pm']
        y24 = EcPm
        y25 = controlfemaleFemurCort_df['Ec.Pm']
        y26 = EcPm2
        y27 = controlmaleFemurCort_df['Ec.Pm']
        y28 = CtTh
        y29 = controlfemaleFemurCort_df['Ct.Th']
        y30 = CtTh2
        y31 = controlmaleFemurCort_df['Ct.Th']

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
        df_filtered = femaleFemurCort_df[femaleFemurCort_df['gene_symbol'].isin([value])]
        df_filtered_MF = maleFemurCort_df[maleFemurCort_df['gene_symbol'].isin([value])]

        CtAr = df_filtered['Ct.Ar']
        CtAr2 = df_filtered_MF['Ct.Ar']
        PsPm = df_filtered['Ps.Pm']
        PsPm2 = df_filtered_MF['Ps.Pm']
        EcPm = df_filtered['Ec.Pm']
        EcPm2 = df_filtered_MF['Ec.Pm']
        CtTh = df_filtered['Ct.Th']
        CtTh2 = df_filtered_MF['Ct.Th']

        y16 = CtAr
        y17 = controlfemaleFemurCort_df['Ct.Ar']
        y18 = CtAr2
        y19 = controlmaleFemurCort_df['Ct.Ar']
        y20 = PsPm
        y21 = controlfemaleFemurCort_df['Ps.Pm']
        y22 = PsPm2
        y23 = controlmaleFemurCort_df['Ps.Pm']
        y24 = EcPm
        y25 = controlfemaleFemurCort_df['Ec.Pm']
        y26 = EcPm2
        y27 = controlmaleFemurCort_df['Ec.Pm']
        y28 = CtTh
        y29 = controlfemaleFemurCort_df['Ct.Th']
        y30 = CtTh2
        y31 = controlmaleFemurCort_df['Ct.Th']

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
                             subplot_titles=(
                             "<b>Ct.Ar</b> (mm\u00b2)", "<b>Ps.Pm</b> (mm)", "<b>Ec.Pm</b> (mm)", '<b>Ct.Th</b> (mm)',
                             "<b>Ct.Ar</b> (mm\u00b2)", "<b>Ps.Pm</b> (mm)", "<b>Ec.Pm</b> (mm)", '<b>Ct.Th</b> (mm)'))

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

    box_plot.update_layout(height=600, width=900, margin={'t': 30}, plot_bgcolor='white', font_family='Arial')
    box_plot.update_yaxes(title_text="<b>Female</b>", row=1, col=1, gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14), range=[0.3, 1.0])
    box_plot.update_yaxes(row=2, col=1, title_text="<b>Male</b>", gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14), range=[0.3, 1.0])
    box_plot.update_yaxes(row=1, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[3.0, 6.0])
    box_plot.update_yaxes(row=2, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[3.0, 6.0])
    box_plot.update_yaxes(row=1, col=3, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[2.5, 5.0])
    box_plot.update_yaxes(row=2, col=3, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[2.5, 5.0])
    box_plot.update_yaxes(row=1, col=4, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0.1, 0.2])
    box_plot.update_yaxes(row=2, col=4, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0.1, 0.2])

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
    Output(component_id='box_plot33', component_property='figure'),
    Input(component_id='gs', component_property='value')
    )
def update_boxplots(value):
    if len(value) == 0:
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
        df_filtered_FV = femaleVert_df[femaleVert_df['gene_symbol'].isin([value])]
        df_filtered_MV = maleVert_df[maleVert_df['gene_symbol'].isin([value])]

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
                             specs=[[{}, {}, {}, {}], [{}, {}, {}, {}]], vertical_spacing=0.17,
                             # for colspan and rowspan default is 1 col or 1 row so setting up the spect like this
                             # defines a 4x2 subplot
                             subplot_titles=(
                             "<b>BV/TV</b> (%)", "<b>Tb.N</b> (#/mm)", "<b>Tb.Th</b> (µm)", '<b>Tb.Sp</b> (µm)',
                             "<b>BV/TV</b> (%)", "<b>Tb.N</b> (#/mm)", "<b>Tb.Th</b> (µm)", '<b>Tb.Sp</b> (µm)'))

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

    box_plot.update_layout(height=650, width=900, margin={'t': 30}, plot_bgcolor='white', font_family='Arial')
    box_plot.update_yaxes(title_text="<b>Female</b>", row=1, col=1, range=[10, 40], gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14))
    box_plot.update_yaxes(row=2, col=1, title_text="<b>Male</b>", range=[10, 40], gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14))
    box_plot.update_yaxes(row=1, col=2, range=[3, 8], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(range=[3, 8], row=2, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(row=1, col=3, range=[20, 80], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(row=2, col=3, range=[20, 80], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(row=1, col=4, range=[0, 400], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(range=[0, 400], row=2, col=4, gridcolor='#D3D3D3', tickfont=dict(size=14))

    box_plot.update_xaxes(showline=True, linewidth=2, linecolor='#666A6D')
    box_plot.update_yaxes(showline=True, linewidth=2, linecolor='#666A6D')

    if stat1 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat1}'), row=1, col=1)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=1)
    if stat2 > 0.001:
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
    Output(component_id='box_plot34', component_property='figure'),
    Input(component_id='gs', component_property='value')
    )
def update_boxplots(value):
    if len(value) == 0:
        df_filtered = HISTOfemaleFemur_df[HISTOfemaleFemur_df['gene_symbol'].isin(['Irf8'])]
        df_filtered_MF = HISTOmaleFemur_df[HISTOmaleFemur_df['gene_symbol'].isin(['Irf8'])]

        bvtv = df_filtered['BV_TV'].dropna()
        bvtv2 = df_filtered_MF['BV_TV'].dropna()
        TbN = df_filtered['Tb.N'].dropna()
        TbN2 = df_filtered_MF['Tb.N'].dropna()
        TbTh = df_filtered['Tb.Th'].dropna()
        TbTh2 = df_filtered_MF['Tb.Th'].dropna()
        TbSp = df_filtered['Tb.Sp'].dropna()
        TbSp2 = df_filtered_MF['Tb.Sp'].dropna()

        y = bvtv
        y1 = conHISTOfemaleFemur_df['BV_TV'].dropna()
        y2 = bvtv2
        y3 = conHISTOmaleFemur_df['BV_TV'].dropna()
        y4 = TbN
        y5 = conHISTOfemaleFemur_df['Tb.N'].dropna()
        y6 = TbN2
        y7 = conHISTOmaleFemur_df['Tb.N'].dropna()
        y8 = TbTh
        y9 = conHISTOfemaleFemur_df['Tb.Th'].dropna()
        y10 = TbTh2
        y11 = conHISTOmaleFemur_df['Tb.Th'].dropna()
        y12 = TbSp
        y13 = conHISTOfemaleFemur_df['Tb.Sp'].dropna()
        y14 = TbSp2
        y15 = conHISTOmaleFemur_df['Tb.Sp'].dropna()

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
        df_filtered = HISTOfemaleFemur_df[HISTOfemaleFemur_df['gene_symbol'].isin([value])]
        df_filtered_MF = HISTOmaleFemur_df[HISTOmaleFemur_df['gene_symbol'].isin([value])]

        bvtv = df_filtered['BV_TV'].dropna()
        bvtv2 = df_filtered_MF['BV_TV'].dropna()
        TbN = df_filtered['Tb.N'].dropna()
        TbN2 = df_filtered_MF['Tb.N'].dropna()
        TbTh = df_filtered['Tb.Th'].dropna()
        TbTh2 = df_filtered_MF['Tb.Th'].dropna()
        TbSp = df_filtered['Tb.Sp'].dropna()
        TbSp2 = df_filtered_MF['Tb.Sp'].dropna()

        y = bvtv
        y1 = conHISTOfemaleFemur_df['BV_TV'].dropna()
        y2 = bvtv2
        y3 = conHISTOmaleFemur_df['BV_TV'].dropna()
        y4 = TbN
        y5 = conHISTOfemaleFemur_df['Tb.N'].dropna()
        y6 = TbN2
        y7 = conHISTOmaleFemur_df['Tb.N'].dropna()
        y8 = TbTh
        y9 = conHISTOfemaleFemur_df['Tb.Th'].dropna()
        y10 = TbTh2
        y11 = conHISTOmaleFemur_df['Tb.Th'].dropna()
        y12 = TbSp
        y13 = conHISTOfemaleFemur_df['Tb.Sp'].dropna()
        y14 = TbSp2
        y15 = conHISTOmaleFemur_df['Tb.Sp'].dropna()

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
                             specs=[[{}, {}, {}, {}], [{}, {}, {}, {}]], vertical_spacing=0.17,
                             # for colspan and rowspan default is 1 col or 1 row so setting up the spect like this
                             # defines a 4x2 subplot
                             subplot_titles=(
                             "<b>BV/TV</b> (%)", "<b>Tb.N</b> (#/mm)", "<b>Tb.Th</b> (µm)", '<b>Tb.Sp</b> (µm)',
                             "<b>BV/TV</b> (%)", "<b>Tb.N</b> (#/mm)", "<b>Tb.Th</b> (µm)", '<b>Tb.Sp</b> (µm)'))

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

    box_plot.update_layout(height=650, width=900, margin={'t': 30}, plot_bgcolor='white', font_family='Arial')
    box_plot.update_yaxes(title_text="<b>Female</b>", row=1, col=1, range=[0, 35], gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14))
    box_plot.update_yaxes(row=2, col=1, title_text="<b>Male</b>", range=[0, 35], gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14))
    box_plot.update_yaxes(row=1, col=2, range=[0, 7], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(range=[0, 7], row=2, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(row=1, col=3, range=[20, 80], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(row=2, col=3, range=[20, 80], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(row=1, col=4, range=[100, 1400], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(range=[100, 1400], row=2, col=4, gridcolor='#D3D3D3', tickfont=dict(size=14))

    box_plot.update_xaxes(showline=True, linewidth=2, linecolor='#666A6D')
    box_plot.update_yaxes(showline=True, linewidth=2, linecolor='#666A6D')

    if stat1 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat1}'), row=1, col=1)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=1)
    if stat2 > 0.001:
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
    Output(component_id='box_plot35', component_property='figure'),
    Input(component_id='gs', component_property='value')
    )
def update_boxplots(value):
    if len(value) == 0:
        df_filtered = HISTOfemaleFemur_df[HISTOfemaleFemur_df['gene_symbol'].isin(['Irf8'])]
        df_filtered_MF = HISTOmaleFemur_df[HISTOmaleFemur_df['gene_symbol'].isin(['Irf8'])]

        mar = df_filtered['MAR'].dropna()
        mar2 = df_filtered_MF['MAR'].dropna()
        msbs = df_filtered['MS_BS'].dropna()
        msbs2 = df_filtered_MF['MS_BS'].dropna()
        bfr = df_filtered['BFR'].dropna()
        bfr2 = df_filtered_MF['BFR'].dropna()
        apbs = df_filtered['AP_BS'].dropna()
        apbs2 = df_filtered_MF['AP_BS'].dropna()

        y = mar
        y1 = conHISTOfemaleFemur_df['MAR'].dropna()
        y2 = mar2
        y3 = conHISTOmaleFemur_df['MAR'].dropna()
        y4 = msbs
        y5 = conHISTOfemaleFemur_df['MS_BS'].dropna()
        y6 = msbs2
        y7 = conHISTOmaleFemur_df['MS_BS'].dropna()
        y8 = bfr
        y9 = conHISTOfemaleFemur_df['BFR'].dropna()
        y10 = bfr2
        y11 = conHISTOmaleFemur_df['BFR'].dropna()
        y12 = apbs
        y13 = conHISTOfemaleFemur_df['AP_BS'].dropna()
        y14 = apbs2
        y15 = conHISTOmaleFemur_df['AP_BS'].dropna()

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
        df_filtered = HISTOfemaleFemur_df[HISTOfemaleFemur_df['gene_symbol'].isin([value])]
        df_filtered_MF = HISTOmaleFemur_df[HISTOmaleFemur_df['gene_symbol'].isin([value])]

        mar = df_filtered['MAR'].dropna()
        mar2 = df_filtered_MF['MAR'].dropna()
        msbs = df_filtered['MS_BS'].dropna()
        msbs2 = df_filtered_MF['MS_BS'].dropna()
        bfr = df_filtered['BFR'].dropna()
        bfr2 = df_filtered_MF['BFR'].dropna()
        apbs = df_filtered['AP_BS'].dropna()
        apbs2 = df_filtered_MF['AP_BS'].dropna()

        y = mar
        y1 = conHISTOfemaleFemur_df['MAR'].dropna()
        y2 = mar2
        y3 = conHISTOmaleFemur_df['MAR'].dropna()
        y4 = msbs
        y5 = conHISTOfemaleFemur_df['MS_BS'].dropna()
        y6 = msbs2
        y7 = conHISTOmaleFemur_df['MS_BS'].dropna()
        y8 = bfr
        y9 = conHISTOfemaleFemur_df['BFR'].dropna()
        y10 = bfr2
        y11 = conHISTOmaleFemur_df['BFR'].dropna()
        y12 = apbs
        y13 = conHISTOfemaleFemur_df['AP_BS'].dropna()
        y14 = apbs2
        y15 = conHISTOmaleFemur_df['AP_BS'].dropna()

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
                             specs=[[{}, {}, {}, {}], [{}, {}, {}, {}]], vertical_spacing=0.2,
                             # for colspan and rowspan default is 1 col or 1 row so setting up the spect like this
                             # defines a 2x4 subplot
                             subplot_titles=(
                             "<b>MAR </b>(µm/day)", "<b>MS/BS </b>(%)", "<b>BFR </b>(µm3/µm2/day)", '<b>AP/BS</b> (%)',
                             "<b>MAR </b>(µm/day)", "<b>MS/BS </b>(%)", "<b>BFR </b>(µm3/µm2/day)", '<b>AP/BS</b> (%)',
                             ))

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

    box_plot.update_layout(height=600, width=900, margin={'t': 30}, plot_bgcolor='white', font_family='Arial')
    box_plot.update_yaxes(title_text="<b>Female</b>", row=1, col=1, gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14), range=[0, 5])
    box_plot.update_yaxes(row=2, col=1, title_text="<b>Male</b>", gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14), range=[0, 5])
    box_plot.update_yaxes(row=1, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 50])
    box_plot.update_yaxes(row=2, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 50])
    box_plot.update_yaxes(row=1, col=3, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 1.5])
    box_plot.update_yaxes(row=2, col=3, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 1.5])
    box_plot.update_yaxes(row=1, col=4, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 100])
    box_plot.update_yaxes(row=2, col=4, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 100])

    box_plot.update_xaxes(showline=True, linewidth=2, linecolor='#666A6D')
    box_plot.update_yaxes(showline=True, linewidth=2, linecolor='#666A6D')
    if stat1 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat1}'), row=1, col=1)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=1)
    if stat2 > 0.001:
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
    Output(component_id='box_plot36', component_property='figure'),
    Input(component_id='gs', component_property='value')
    )
def update_boxplots(value):
    if len(value) == 0:
        df_filtered = HISTOfemaleFemur_df[HISTOfemaleFemur_df['gene_symbol'].isin(['Irf8'])]
        df_filtered_MF = HISTOmaleFemur_df[HISTOmaleFemur_df['gene_symbol'].isin(['Irf8'])]

        aplbs = df_filtered['AP_L_BS'].dropna()
        aplbs2 = df_filtered_MF['AP_L_BS'].dropna()
        apnlbs = df_filtered['AP_NL_BS'].dropna()
        apnlbs2 = df_filtered_MF['AP_NL_BS'].dropna()
        aplap = df_filtered['AP_L_AP'].dropna()
        aplap2 = df_filtered_MF['AP_L_AP'].dropna()
        apnlap = df_filtered['AP_NL_AP'].dropna()
        apnlap2 = df_filtered_MF['AP_NL_AP'].dropna()

        y16 = aplbs
        y17 = conHISTOfemaleFemur_df['AP_L_BS'].dropna()
        y18 = aplbs2
        y19 = conHISTOmaleFemur_df['AP_L_BS'].dropna()
        y20 = apnlbs
        y21 = conHISTOfemaleFemur_df['AP_NL_BS'].dropna()
        y22 = apnlbs2
        y23 = conHISTOmaleFemur_df['AP_NL_BS'].dropna()
        y24 = aplap
        y25 = conHISTOfemaleFemur_df['AP_L_AP'].dropna()
        y26 = aplap2
        y27 = conHISTOmaleFemur_df['AP_L_AP'].dropna()
        y28 = apnlap
        y29 = conHISTOfemaleFemur_df['AP_NL_AP'].dropna()
        y30 = apnlap2
        y31 = conHISTOmaleFemur_df['AP_NL_AP'].dropna()

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
        df_filtered = HISTOfemaleFemur_df[HISTOfemaleFemur_df['gene_symbol'].isin([value])]
        df_filtered_MF = HISTOmaleFemur_df[HISTOmaleFemur_df['gene_symbol'].isin([value])]

        aplbs = df_filtered['AP_L_BS'].dropna()
        aplbs2 = df_filtered_MF['AP_L_BS'].dropna()
        apnlbs = df_filtered['AP_NL_BS'].dropna()
        apnlbs2 = df_filtered_MF['AP_NL_BS'].dropna()
        aplap = df_filtered['AP_L_AP'].dropna()
        aplap2 = df_filtered_MF['AP_L_AP'].dropna()
        apnlap = df_filtered['AP_NL_AP'].dropna()
        apnlap2 = df_filtered_MF['AP_NL_AP'].dropna()

        y16 = aplbs
        y17 = conHISTOfemaleFemur_df['AP_L_BS'].dropna()
        y18 = aplbs2
        y19 = conHISTOmaleFemur_df['AP_L_BS'].dropna()
        y20 = apnlbs
        y21 = conHISTOfemaleFemur_df['AP_NL_BS'].dropna()
        y22 = apnlbs2
        y23 = conHISTOmaleFemur_df['AP_NL_BS'].dropna()
        y24 = aplap
        y25 = conHISTOfemaleFemur_df['AP_L_AP'].dropna()
        y26 = aplap2
        y27 = conHISTOmaleFemur_df['AP_L_AP'].dropna()
        y28 = apnlap
        y29 = conHISTOfemaleFemur_df['AP_NL_AP'].dropna()
        y30 = apnlap2
        y31 = conHISTOmaleFemur_df['AP_NL_AP'].dropna()

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
        subplot_titles=("<b>AP<sub>L</sub>/BS</b> (%)", "<b>AP<sub>NL</sub>/BS</b> (%)","<b>AP<sub>L</sub>/AP</b> (%)", '<b>AP<sub>NL</sub>/AP</b> (%)',
                        "<b>AP<sub>L</sub>/BS</b> (%)", "<b>AP<sub>NL</sub>/BS</b> (%)","<b>AP<sub>L</sub>/AP</b> (%)",'<b>AP<sub>NL</sub>/AP</b> (%)'))


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
    box_plot.update_yaxes(title_text="<b>Female</b>", row=1, col=1,gridcolor='#D3D3D3', title_font=dict(size=18,family='Arial'),tickfont=dict(size=14), range=[0,100])
    box_plot.update_yaxes(row=2, col=1,title_text="<b>Male</b>",gridcolor='#D3D3D3',title_font=dict(size=18,family='Arial'),tickfont=dict(size=14),range=[0,100])
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
    Output(component_id='box_plot37', component_property='figure'),
    Input(component_id='gs', component_property='value')
    )
def update_boxplots(value):
    if len(value) == 0:
        df_filtered = HISTOfemaleFemur_df[HISTOfemaleFemur_df['gene_symbol'].isin(['Irf8'])]
        df_filtered_MF = HISTOmaleFemur_df[HISTOmaleFemur_df['gene_symbol'].isin(['Irf8'])]

        trapbs = df_filtered['TRAP_BS'].dropna()
        trapbs2 = df_filtered_MF['TRAP_BS'].dropna()
        traplbs = df_filtered['TRAP_L_BS'].dropna()
        traplbs2 = df_filtered_MF['TRAP_L_BS'].dropna()
        trapnlbs = df_filtered['TRAP_NL_BS'].dropna()
        trapnlbs2 = df_filtered_MF['TRAP_NL_BS'].dropna()

        y = trapbs
        y1 = conHISTOfemaleFemur_df['TRAP_BS'].dropna()
        y2 = trapbs2
        y3 = conHISTOmaleFemur_df['TRAP_BS'].dropna()
        y4 = traplbs
        y5 = conHISTOfemaleFemur_df['TRAP_L_BS'].dropna()
        y6 = traplbs2
        y7 = conHISTOmaleFemur_df['TRAP_L_BS'].dropna()
        y8 = trapnlbs
        y9 = conHISTOfemaleFemur_df['TRAP_NL_BS'].dropna()
        y10 = trapnlbs2
        y11 = conHISTOmaleFemur_df['TRAP_NL_BS'].dropna()

        name = "Irf8 -/-"

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

    else:
        df_filtered = HISTOfemaleFemur_df[HISTOfemaleFemur_df['gene_symbol'].isin([value])]
        df_filtered_MF = HISTOmaleFemur_df[HISTOmaleFemur_df['gene_symbol'].isin([value])]

        trapbs = df_filtered['TRAP_BS'].dropna()
        trapbs2 = df_filtered_MF['TRAP_BS'].dropna()
        traplbs = df_filtered['TRAP_L_BS'].dropna()
        traplbs2 = df_filtered_MF['TRAP_L_BS'].dropna()
        trapnlbs = df_filtered['TRAP_NL_BS'].dropna()
        trapnlbs2 = df_filtered_MF['TRAP_NL_BS'].dropna()

        y = trapbs
        y1 = conHISTOfemaleFemur_df['TRAP_BS'].dropna()
        y2 = trapbs2
        y3 = conHISTOmaleFemur_df['TRAP_BS'].dropna()
        y4 = traplbs
        y5 = conHISTOfemaleFemur_df['TRAP_L_BS'].dropna()
        y6 = traplbs2
        y7 = conHISTOmaleFemur_df['TRAP_L_BS'].dropna()
        y8 = trapnlbs
        y9 = conHISTOfemaleFemur_df['TRAP_NL_BS'].dropna()
        y10 = trapnlbs2
        y11 = conHISTOmaleFemur_df['TRAP_NL_BS'].dropna()

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
                             specs=[[{}, {}, {}], [{}, {}, {}]], vertical_spacing=0.2,
                             # for colspan and rowspan default is 1 col or 1 row so setting up the spect like this
                             # defines a 2x4 subplot
                             subplot_titles=(
                             "<b>TRAP/BS </b> (%)", "<b>TRAP<sub>L</sub>/BS</b> (%)", "<b>TRAP<sub>NL</sub>/BS</b> (%)",
                             "<b>TRAP/BS</b> (%)", "<b>TRAP<sub>L</sub>/BS</b> (%)", "<b>TRAP<sub>NL</sub>/BS</b> (%)"))

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

    box_plot.update_layout(height=600, width=900, margin={'t': 30}, plot_bgcolor='white', font_family='Arial')
    box_plot.update_yaxes(title_text="<b>Female</b>", row=1, col=1, gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14), range=[0, 60])
    box_plot.update_yaxes(row=2, col=1, title_text="<b>Male</b>", gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14), range=[0, 60])
    box_plot.update_yaxes(row=1, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 50])
    box_plot.update_yaxes(row=2, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 50])
    box_plot.update_yaxes(row=1, col=3, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 30])
    box_plot.update_yaxes(row=2, col=3, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 30])

    box_plot.update_xaxes(showline=True, linewidth=2, linecolor='#666A6D')
    box_plot.update_yaxes(showline=True, linewidth=2, linecolor='#666A6D')
    if stat1 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat1}'), row=1, col=3)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=3)
    if stat2 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat2}'), row=2, col=3)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=2, col=3)
    if stat3 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat3}'), row=1, col=2)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=2)
    if stat4 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat4}'), row=2, col=2)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=2, col=2)
    if stat5 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat5}'), row=1, col=1)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=1)
    if stat6 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat6}'), row=2, col=1)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=2, col=1)

    return box_plot

@callback(
    Output(component_id='box_plot38', component_property='figure'),
    Input(component_id='gs', component_property='value')
    )
def update_boxplots(value):
    if len(value) == 0:
        df_filtered = HISTOfemaleFemur_df[HISTOfemaleFemur_df['gene_symbol'].isin(['Irf8'])]
        df_filtered_MF = HISTOmaleFemur_df[HISTOmaleFemur_df['gene_symbol'].isin(['Irf8'])]

        aptrap = df_filtered['AP_TRAP_R_RG_BS'].dropna()
        aptrap2 = df_filtered_MF['AP_TRAP_R_RG_BS'].dropna()
        trapontrap = df_filtered['TRAP_on_TRAP'].dropna()
        trapontrap2 = df_filtered_MF['TRAP_on_TRAP'].dropna()
        trapltrapon = df_filtered['TRAP_L_TRAP_on'].dropna()
        trapltrapon2 = df_filtered_MF['TRAP_L_TRAP_on'].dropna()
        trapnltrapon = df_filtered['TRAP_NL_TRAP_on'].dropna()
        trapnltrapon2 = df_filtered_MF['TRAP_NL_TRAP_on'].dropna()

        y16 = aptrap
        y17 = conHISTOfemaleFemur_df['AP_TRAP_R_RG_BS'].dropna()
        y18 = aptrap2
        y19 = conHISTOmaleFemur_df['AP_TRAP_R_RG_BS'].dropna()
        y20 = trapontrap
        y21 = conHISTOfemaleFemur_df['TRAP_on_TRAP'].dropna()
        y22 = trapontrap2
        y23 = conHISTOmaleFemur_df['TRAP_on_TRAP'].dropna()
        y24 = trapltrapon
        y25 = conHISTOfemaleFemur_df['TRAP_L_TRAP_on'].dropna()
        y26 = trapltrapon2
        y27 = conHISTOmaleFemur_df['TRAP_L_TRAP_on'].dropna()
        y28 = trapnltrapon
        y29 = conHISTOfemaleFemur_df['TRAP_NL_TRAP_on'].dropna()
        y30 = trapnltrapon2
        y31 = conHISTOmaleFemur_df['TRAP_NL_TRAP_on'].dropna()

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
        df_filtered = HISTOfemaleFemur_df[HISTOfemaleFemur_df['gene_symbol'].isin([value])]
        df_filtered_MF = HISTOmaleFemur_df[HISTOmaleFemur_df['gene_symbol'].isin([value])]

        aptrap = df_filtered['AP_TRAP_R_RG_BS'].dropna()
        aptrap2 = df_filtered_MF['AP_TRAP_R_RG_BS'].dropna()
        trapontrap = df_filtered['TRAP_on_TRAP'].dropna()
        trapontrap2 = df_filtered_MF['TRAP_on_TRAP'].dropna()
        trapltrapon = df_filtered['TRAP_L_TRAP_on'].dropna()
        trapltrapon2 = df_filtered_MF['TRAP_L_TRAP_on'].dropna()
        trapnltrapon = df_filtered['TRAP_NL_TRAP_on'].dropna()
        trapnltrapon2 = df_filtered_MF['TRAP_NL_TRAP_on'].dropna()

        y16 = aptrap
        y17 = conHISTOfemaleFemur_df['AP_TRAP_R_RG_BS'].dropna()
        y18 = aptrap2
        y19 = conHISTOmaleFemur_df['AP_TRAP_R_RG_BS'].dropna()
        y20 = trapontrap
        y21 = conHISTOfemaleFemur_df['TRAP_on_TRAP'].dropna()
        y22 = trapontrap2
        y23 = conHISTOmaleFemur_df['TRAP_on_TRAP'].dropna()
        y24 = trapltrapon
        y25 = conHISTOfemaleFemur_df['TRAP_L_TRAP_on'].dropna()
        y26 = trapltrapon2
        y27 = conHISTOmaleFemur_df['TRAP_L_TRAP_on'].dropna()
        y28 = trapnltrapon
        y29 = conHISTOfemaleFemur_df['TRAP_NL_TRAP_on'].dropna()
        y30 = trapnltrapon2
        y31 = conHISTOmaleFemur_df['TRAP_NL_TRAP_on'].dropna()

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
    Output(component_id='box_plot39', component_property='figure'),
    Input(component_id='gs', component_property='value')
    )
def update_boxplots(value):
    if len(value) == 0:
        df_filtered_F = femaleHISTOVert_df[femaleHISTOVert_df['gene_symbol'].isin(['Irf8'])]
        df_filtered_M = maleHISTOVert_df[maleHISTOVert_df['gene_symbol'].isin(['Irf8'])]

        bvtv = df_filtered_F['BV_TV'].dropna()
        bvtv2 = df_filtered_M['BV_TV'].dropna()
        TbN = df_filtered_F['Tb.N'].dropna()
        TbN2 = df_filtered_M['Tb.N'].dropna()
        TbTh = df_filtered_F['Tb.Th'].dropna()
        TbTh2 = df_filtered_M['Tb.Th'].dropna()
        TbSp = df_filtered_F['Tb.Sp'].dropna()
        TbSp2 = df_filtered_M['Tb.Sp'].dropna()

        y = bvtv
        y1 = controlfemaleHISTOVert_df['BV_TV'].dropna()
        y2 = bvtv2
        y3 = controlmaleHISTOVert_df['BV_TV'].dropna()
        y4 = TbN
        y5 = controlfemaleHISTOVert_df['Tb.N'].dropna()
        y6 = TbN2
        y7 = controlmaleHISTOVert_df['Tb.N'].dropna()
        y8 = TbTh
        y9 = controlfemaleHISTOVert_df['Tb.Th'].dropna()
        y10 = TbTh2
        y11 = controlmaleHISTOVert_df['Tb.Th'].dropna()
        y12 = TbSp
        y13 = controlfemaleHISTOVert_df['Tb.Sp'].dropna()
        y14 = TbSp2
        y15 = controlmaleHISTOVert_df['Tb.Sp'].dropna()

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
        df_filtered_F = femaleHISTOVert_df[femaleHISTOVert_df['gene_symbol'].isin([value])]
        df_filtered_M = maleHISTOVert_df[maleHISTOVert_df['gene_symbol'].isin([value])]

        bvtv = df_filtered_F['BV_TV'].dropna()
        bvtv2 = df_filtered_M['BV_TV'].dropna()
        TbN = df_filtered_F['Tb.N'].dropna()
        TbN2 = df_filtered_M['Tb.N'].dropna()
        TbTh = df_filtered_F['Tb.Th'].dropna()
        TbTh2 = df_filtered_M['Tb.Th'].dropna()
        TbSp = df_filtered_F['Tb.Sp'].dropna()
        TbSp2 = df_filtered_M['Tb.Sp'].dropna()

        y = bvtv
        y1 = controlfemaleHISTOVert_df['BV_TV'].dropna()
        y2 = bvtv2
        y3 = controlmaleHISTOVert_df['BV_TV'].dropna()
        y4 = TbN
        y5 = controlfemaleHISTOVert_df['Tb.N'].dropna()
        y6 = TbN2
        y7 = controlmaleHISTOVert_df['Tb.N'].dropna()
        y8 = TbTh
        y9 = controlfemaleHISTOVert_df['Tb.Th'].dropna()
        y10 = TbTh2
        y11 = controlmaleHISTOVert_df['Tb.Th'].dropna()
        y12 = TbSp
        y13 = controlfemaleHISTOVert_df['Tb.Sp'].dropna()
        y14 = TbSp2
        y15 = controlmaleHISTOVert_df['Tb.Sp'].dropna()

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
                             specs=[[{}, {}, {}, {}], [{}, {}, {}, {}]], vertical_spacing=0.17,
                             # for colspan and rowspan default is 1 col or 1 row so setting up the spect like this
                             # defines a 4x2 subplot
                             subplot_titles=(
                             "<b>BV/TV</b> (%)", "<b>Tb.N</b> (#/mm)", "<b>Tb.Th</b> (µm)", '<b>Tb.Sp</b> (µm)',
                             "<b>BV/TV</b> (%)", "<b>Tb.N</b> (#/mm)", "<b>Tb.Th</b> (µm)", '<b>Tb.Sp</b> (µm)'))

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

    box_plot.update_layout(height=650, width=900, margin={'t': 30}, plot_bgcolor='white', font_family='Arial')
    box_plot.update_yaxes(title_text="<b>Female</b>", row=1, col=1, range=[0, 35], gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14))
    box_plot.update_yaxes(row=2, col=1, title_text="<b>Male</b>", range=[0, 35], gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14))
    box_plot.update_yaxes(row=1, col=2, range=[0, 7], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(range=[0, 7], row=2, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(row=1, col=3, range=[20, 80], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(row=2, col=3, range=[20, 80], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(row=1, col=4, range=[0, 600], gridcolor='#D3D3D3', tickfont=dict(size=14))
    box_plot.update_yaxes(range=[0, 600], row=2, col=4, gridcolor='#D3D3D3', tickfont=dict(size=14))

    box_plot.update_xaxes(showline=True, linewidth=2, linecolor='#666A6D')
    box_plot.update_yaxes(showline=True, linewidth=2, linecolor='#666A6D')

    if stat1 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat1}'), row=1, col=1)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=1)
    if stat2 > 0.001:
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
    Output(component_id='box_plot40', component_property='figure'),
    Input(component_id='gs', component_property='value')
    )
def update_boxplots(value):
    if len(value) == 0:
        df_filtered = femaleHISTOVert_df[femaleHISTOVert_df['gene_symbol'].isin(['Irf8'])]
        df_filtered_MF = maleHISTOVert_df[maleHISTOVert_df['gene_symbol'].isin(['Irf8'])]

        mar = df_filtered['MAR'].dropna()
        mar2 = df_filtered_MF['MAR'].dropna()
        msbs = df_filtered['MS_BS'].dropna()
        msbs2 = df_filtered_MF['MS_BS'].dropna()
        bfr = df_filtered['BFR'].dropna()
        bfr2 = df_filtered_MF['BFR'].dropna()
        apbs = df_filtered['AP_BS'].dropna()
        apbs2 = df_filtered_MF['AP_BS'].dropna()

        y = mar
        y1 = controlfemaleHISTOVert_df['MAR'].dropna()
        y2 = mar2
        y3 = controlmaleHISTOVert_df['MAR'].dropna()
        y4 = msbs
        y5 = controlfemaleHISTOVert_df['MS_BS'].dropna()
        y6 = msbs2
        y7 = controlmaleHISTOVert_df['MS_BS'].dropna()
        y8 = bfr
        y9 = controlfemaleHISTOVert_df['BFR'].dropna()
        y10 = bfr2
        y11 = controlmaleHISTOVert_df['BFR'].dropna()
        y12 = apbs
        y13 = controlfemaleHISTOVert_df['AP_BS'].dropna()
        y14 = apbs2
        y15 = controlmaleHISTOVert_df['AP_BS'].dropna()

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
        df_filtered = femaleHISTOVert_df[femaleHISTOVert_df['gene_symbol'].isin([value])]
        df_filtered_MF = maleHISTOVert_df[maleHISTOVert_df['gene_symbol'].isin([value])]

        mar = df_filtered['MAR'].dropna()
        mar2 = df_filtered_MF['MAR'].dropna()
        msbs = df_filtered['MS_BS'].dropna()
        msbs2 = df_filtered_MF['MS_BS'].dropna()
        bfr = df_filtered['BFR'].dropna()
        bfr2 = df_filtered_MF['BFR'].dropna()
        apbs = df_filtered['AP_BS'].dropna()
        apbs2 = df_filtered_MF['AP_BS'].dropna()

        y = mar
        y1 = controlfemaleHISTOVert_df['MAR'].dropna()
        y2 = mar2
        y3 = controlmaleHISTOVert_df['MAR'].dropna()
        y4 = msbs
        y5 = controlfemaleHISTOVert_df['MS_BS'].dropna()
        y6 = msbs2
        y7 = controlmaleHISTOVert_df['MS_BS'].dropna()
        y8 = bfr
        y9 = controlfemaleHISTOVert_df['BFR'].dropna()
        y10 = bfr2
        y11 = controlmaleHISTOVert_df['BFR'].dropna()
        y12 = apbs
        y13 = controlfemaleHISTOVert_df['AP_BS'].dropna()
        y14 = apbs2
        y15 = controlmaleHISTOVert_df['AP_BS'].dropna()

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
                             specs=[[{}, {}, {}, {}], [{}, {}, {}, {}]], vertical_spacing=0.2,
                             # for colspan and rowspan default is 1 col or 1 row so setting up the spect like this
                             # defines a 2x4 subplot
                             subplot_titles=(
                             "<b>MAR </b>(µm/day)", "<b>MS/BS </b>(%)", "<b>BFR </b>(µm3/µm2/day)", '<b>AP/BS</b> (%)',
                             "<b>MAR </b>(µm/day)", "<b>MS/BS </b>(%)", "<b>BFR </b>(µm3/µm2/day)", '<b>AP/BS</b> (%)',
                             ))

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

    box_plot.update_layout(height=600, width=900, margin={'t': 30}, plot_bgcolor='white', font_family='Arial')
    box_plot.update_yaxes(title_text="<b>Female</b>", row=1, col=1, gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14), range=[0, 5])
    box_plot.update_yaxes(row=2, col=1, title_text="<b>Male</b>", gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14), range=[0, 5])
    box_plot.update_yaxes(row=1, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 60])
    box_plot.update_yaxes(row=2, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 60])
    box_plot.update_yaxes(row=1, col=3, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 1.5])
    box_plot.update_yaxes(row=2, col=3, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 1.5])
    box_plot.update_yaxes(row=1, col=4, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 100])
    box_plot.update_yaxes(row=2, col=4, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 100])

    box_plot.update_xaxes(showline=True, linewidth=2, linecolor='#666A6D')
    box_plot.update_yaxes(showline=True, linewidth=2, linecolor='#666A6D')
    if stat1 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat1}'), row=1, col=1)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=1)
    if stat2 > 0.001:
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
    Output(component_id='box_plot41', component_property='figure'),
    Input(component_id='gs', component_property='value')
    )

def update_boxplots(value):
    if len(value) == 0:
        df_filtered = femaleHISTOVert_df[femaleHISTOVert_df['gene_symbol'].isin(['Irf8'])]
        df_filtered_MF = maleHISTOVert_df[maleHISTOVert_df['gene_symbol'].isin(['Irf8'])]

        aplbs = df_filtered['AP_L_BS'].dropna()
        aplbs2 = df_filtered_MF['AP_L_BS'].dropna()
        apnlbs = df_filtered['AP_NL_BS'].dropna()
        apnlbs2 = df_filtered_MF['AP_NL_BS'].dropna()
        aplap = df_filtered['AP_L_AP'].dropna()
        aplap2 = df_filtered_MF['AP_L_AP'].dropna()
        apnlap = df_filtered['AP_NL_AP'].dropna()
        apnlap2 = df_filtered_MF['AP_NL_AP'].dropna()

        y16 = aplbs
        y17 = controlfemaleHISTOVert_df['AP_L_BS'].dropna()
        y18 = aplbs2
        y19 = controlmaleHISTOVert_df['AP_L_BS'].dropna()
        y20 = apnlbs
        y21 = controlfemaleHISTOVert_df['AP_NL_BS'].dropna()
        y22 = apnlbs2
        y23 = controlmaleHISTOVert_df['AP_NL_BS'].dropna()
        y24 = aplap
        y25 = controlfemaleHISTOVert_df['AP_L_AP'].dropna()
        y26 = aplap2
        y27 = controlmaleHISTOVert_df['AP_L_AP'].dropna()
        y28 = apnlap
        y29 = controlfemaleHISTOVert_df['AP_NL_AP'].dropna()
        y30 = apnlap2
        y31 = controlmaleHISTOVert_df['AP_NL_AP'].dropna()

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
        df_filtered = femaleHISTOVert_df[femaleHISTOVert_df['gene_symbol'].isin([value])]
        df_filtered_MF = maleHISTOVert_df[maleHISTOVert_df['gene_symbol'].isin([value])]

        aplbs = df_filtered['AP_L_BS'].dropna()
        aplbs2 = df_filtered_MF['AP_L_BS'].dropna()
        apnlbs = df_filtered['AP_NL_BS'].dropna()
        apnlbs2 = df_filtered_MF['AP_NL_BS'].dropna()
        aplap = df_filtered['AP_L_AP'].dropna()
        aplap2 = df_filtered_MF['AP_L_AP'].dropna()
        apnlap = df_filtered['AP_NL_AP'].dropna()
        apnlap2 = df_filtered_MF['AP_NL_AP'].dropna()

        y16 = aplbs
        y17 = controlfemaleHISTOVert_df['AP_L_BS'].dropna()
        y18 = aplbs2
        y19 = controlmaleHISTOVert_df['AP_L_BS'].dropna()
        y20 = apnlbs
        y21 = controlfemaleHISTOVert_df['AP_NL_BS'].dropna()
        y22 = apnlbs2
        y23 = controlmaleHISTOVert_df['AP_NL_BS'].dropna()
        y24 = aplap
        y25 = controlfemaleHISTOVert_df['AP_L_AP'].dropna()
        y26 = aplap2
        y27 = controlmaleHISTOVert_df['AP_L_AP'].dropna()
        y28 = apnlap
        y29 = controlfemaleHISTOVert_df['AP_NL_AP'].dropna()
        y30 = apnlap2
        y31 = controlmaleHISTOVert_df['AP_NL_AP'].dropna()

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
        subplot_titles=("<b>AP<sub>L</sub>/BS</b> (%)", "<b>AP<sub>NL</sub>/BS</b> (%)","<b>AP<sub>L</sub>/AP</b> (%)", '<b>AP<sub>NL</sub>/AP</b> (%)',
                        "<b>AP<sub>L</sub>/BS</b> (%)", "<b>AP<sub>NL</sub>/BS</b> (%)","<b>AP<sub>L</sub>/AP</b> (%)",'<b>AP<sub>NL</sub>/AP</b> (%)'))


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
    box_plot.update_yaxes(title_text="<b>Female</b>", row=1, col=1,gridcolor='#D3D3D3', title_font=dict(size=18,family='Arial'),tickfont=dict(size=14), range=[0,100])
    box_plot.update_yaxes(row=2, col=1,title_text="<b>Male</b>",gridcolor='#D3D3D3',title_font=dict(size=18,family='Arial'),tickfont=dict(size=14),range=[0,100])
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
    Output(component_id='box_plot42', component_property='figure'),
    Input(component_id='gs', component_property='value')
    )
def update_boxplots(value):
    if len(value) == 0:
        df_filtered = femaleHISTOVert_df[femaleHISTOVert_df['gene_symbol'].isin(['Irf8'])]
        df_filtered_MF = maleHISTOVert_df[maleHISTOVert_df['gene_symbol'].isin(['Irf8'])]

        trapbs = df_filtered['TRAP_BS'].dropna()
        trapbs2 = df_filtered_MF['TRAP_BS'].dropna()
        traplbs = df_filtered['TRAP_L_BS'].dropna()
        traplbs2 = df_filtered_MF['TRAP_L_BS'].dropna()
        trapnlbs = df_filtered['TRAP_NL_BS'].dropna()
        trapnlbs2 = df_filtered_MF['TRAP_NL_BS'].dropna()

        y = trapbs
        y1 = controlfemaleHISTOVert_df['TRAP_BS'].dropna()
        y2 = trapbs2
        y3 = controlmaleHISTOVert_df['TRAP_BS'].dropna()
        y4 = traplbs
        y5 = controlfemaleHISTOVert_df['TRAP_L_BS'].dropna()
        y6 = traplbs2
        y7 = controlmaleHISTOVert_df['TRAP_L_BS'].dropna()
        y8 = trapnlbs
        y9 = controlfemaleHISTOVert_df['TRAP_NL_BS'].dropna()
        y10 = trapnlbs2
        y11 = controlmaleHISTOVert_df['TRAP_NL_BS'].dropna()

        name = "Irf8 -/-"

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

    else:
        df_filtered = femaleHISTOVert_df[femaleHISTOVert_df['gene_symbol'].isin([value])]
        df_filtered_MF = maleHISTOVert_df[maleHISTOVert_df['gene_symbol'].isin([value])]

        trapbs = df_filtered['TRAP_BS'].dropna()
        trapbs2 = df_filtered_MF['TRAP_BS'].dropna()
        traplbs = df_filtered['TRAP_L_BS'].dropna()
        traplbs2 = df_filtered_MF['TRAP_L_BS'].dropna()
        trapnlbs = df_filtered['TRAP_NL_BS'].dropna()
        trapnlbs2 = df_filtered_MF['TRAP_NL_BS'].dropna()

        y = trapbs
        y1 = controlfemaleHISTOVert_df['TRAP_BS'].dropna()
        y2 = trapbs2
        y3 = controlmaleHISTOVert_df['TRAP_BS'].dropna()
        y4 = traplbs
        y5 = controlfemaleHISTOVert_df['TRAP_L_BS'].dropna()
        y6 = traplbs2
        y7 = controlmaleHISTOVert_df['TRAP_L_BS'].dropna()
        y8 = trapnlbs
        y9 = controlfemaleHISTOVert_df['TRAP_NL_BS'].dropna()
        y10 = trapnlbs2
        y11 = controlmaleHISTOVert_df['TRAP_NL_BS'].dropna()

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
                             specs=[[{}, {}, {}], [{}, {}, {}]], vertical_spacing=0.2,
                             # for colspan and rowspan default is 1 col or 1 row so setting up the spect like this
                             # defines a 2x4 subplot
                             subplot_titles=(
                             "<b>TRAP/BS </b> (%)", "<b>TRAP<sub>L</sub>/BS</b> (%)", "<b>TRAP<sub>NL</sub>/BS</b> (%)",
                             "<b>TRAP/BS</b> (%)", "<b>TRAP<sub>L</sub>/BS</b> (%)", "<b>TRAP<sub>NL</sub>/BS</b> (%)"))

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

    box_plot.update_layout(height=600, width=900, margin={'t': 30}, plot_bgcolor='white', font_family='Arial')
    box_plot.update_yaxes(title_text="<b>Female</b>", row=1, col=1, gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14), range=[0, 60])
    box_plot.update_yaxes(row=2, col=1, title_text="<b>Male</b>", gridcolor='#D3D3D3',
                          title_font=dict(size=18, family='Arial'), tickfont=dict(size=14), range=[0, 60])
    box_plot.update_yaxes(row=1, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 50])
    box_plot.update_yaxes(row=2, col=2, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 50])
    box_plot.update_yaxes(row=1, col=3, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 30])
    box_plot.update_yaxes(row=2, col=3, gridcolor='#D3D3D3', tickfont=dict(size=14), range=[0, 30])

    box_plot.update_xaxes(showline=True, linewidth=2, linecolor='#666A6D')
    box_plot.update_yaxes(showline=True, linewidth=2, linecolor='#666A6D')
    if stat1 > 0.001:
        box_plot.update_xaxes(title_text=(f'p={stat1}'), row=1, col=1)
    else:
        box_plot.update_xaxes(title_text=(f'p<0.0001'), row=1, col=1)
    if stat2 > 0.001:
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
    Output(component_id='box_plot43', component_property='figure'),
    Input(component_id='gs', component_property='value')
    )
def update_boxplots(value):
    if len(value) == 0:
        df_filtered = femaleHISTOVert_df[femaleHISTOVert_df['gene_symbol'].isin(['Irf8'])]
        df_filtered_MF = maleHISTOVert_df[maleHISTOVert_df['gene_symbol'].isin(['Irf8'])]

        aptrap = df_filtered['AP_TRAP_R_RG_BS'].dropna()
        aptrap2 = df_filtered_MF['AP_TRAP_R_RG_BS'].dropna()
        trapontrap = df_filtered['TRAP_on_TRAP'].dropna()
        trapontrap2 = df_filtered_MF['TRAP_on_TRAP'].dropna()
        trapltrapon = df_filtered['TRAP_L_TRAP_on'].dropna()
        trapltrapon2 = df_filtered_MF['TRAP_L_TRAP_on'].dropna()
        trapnltrapon = df_filtered['TRAP_NL_TRAP_on'].dropna()
        trapnltrapon2 = df_filtered_MF['TRAP_NL_TRAP_on'].dropna()

        y16 = aptrap
        y17 = controlfemaleHISTOVert_df['AP_TRAP_R_RG_BS'].dropna()
        y18 = aptrap2
        y19 = controlmaleHISTOVert_df['AP_TRAP_R_RG_BS'].dropna()
        y20 = trapontrap
        y21 = controlfemaleHISTOVert_df['TRAP_on_TRAP'].dropna()
        y22 = trapontrap2
        y23 = controlmaleHISTOVert_df['TRAP_on_TRAP'].dropna()
        y24 = trapltrapon
        y25 = controlfemaleHISTOVert_df['TRAP_L_TRAP_on'].dropna()
        y26 = trapltrapon2
        y27 = controlmaleHISTOVert_df['TRAP_L_TRAP_on'].dropna()
        y28 = trapnltrapon
        y29 = controlfemaleHISTOVert_df['TRAP_NL_TRAP_on'].dropna()
        y30 = trapnltrapon2
        y31 = controlmaleHISTOVert_df['TRAP_NL_TRAP_on'].dropna()

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
        df_filtered = femaleHISTOVert_df[femaleHISTOVert_df['gene_symbol'].isin([value])]
        df_filtered_MF = maleHISTOVert_df[maleHISTOVert_df['gene_symbol'].isin([value])]

        aptrap = df_filtered['AP_TRAP_R_RG_BS'].dropna()
        aptrap2 = df_filtered_MF['AP_TRAP_R_RG_BS'].dropna()
        trapontrap = df_filtered['TRAP_on_TRAP'].dropna()
        trapontrap2 = df_filtered_MF['TRAP_on_TRAP'].dropna()
        trapltrapon = df_filtered['TRAP_L_TRAP_on'].dropna()
        trapltrapon2 = df_filtered_MF['TRAP_L_TRAP_on'].dropna()
        trapnltrapon = df_filtered['TRAP_NL_TRAP_on'].dropna()
        trapnltrapon2 = df_filtered_MF['TRAP_NL_TRAP_on'].dropna()

        y16 = aptrap
        y17 = controlfemaleHISTOVert_df['AP_TRAP_R_RG_BS'].dropna()
        y18 = aptrap2
        y19 = controlmaleHISTOVert_df['AP_TRAP_R_RG_BS'].dropna()
        y20 = trapontrap
        y21 = controlfemaleHISTOVert_df['TRAP_on_TRAP'].dropna()
        y22 = trapontrap2
        y23 = controlmaleHISTOVert_df['TRAP_on_TRAP'].dropna()
        y24 = trapltrapon
        y25 = controlfemaleHISTOVert_df['TRAP_L_TRAP_on'].dropna()
        y26 = trapltrapon2
        y27 = controlmaleHISTOVert_df['TRAP_L_TRAP_on'].dropna()
        y28 = trapnltrapon
        y29 = controlfemaleHISTOVert_df['TRAP_NL_TRAP_on'].dropna()
        y30 = trapnltrapon2
        y31 = controlmaleHISTOVert_df['TRAP_NL_TRAP_on'].dropna()

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



@callback(Output('tabs-content-example-graph', 'children'),
              [Input('tabs-example-graph', 'value'),
                Input(component_id='gs', component_property='value')]
              )
def render_content(tab, value):
    if len(value)==0:
        return html.Div([
            dbc.Row([
            html.H3('Please Type in Gene Symbol and Select Tab to View Data', style={'padding-top':50,
                                                                    'padding-bottom':10,'text-align':'center'}),
            html.H5('Note: Gene Symbols are Case Sensitive (For example, use Rin3 not rin3)',
                        style={'padding-top': 0, 'padding-bottom': 20,'text-align':'center'}),
        ],justify='center', style={'margin-left':50})
            ]),


    elif tab =='tab1-graph':
        return html.Div([
            dbc.Row([
            html.H3('μCT Analysis of Femur Trabecular Bone', style={'padding-left': 175,'padding-top':20, 'padding-bottom':20}),
            dcc.Graph(id='box_plot30', config={
                'modeBarButtonsToRemove': ['pan2d', 'displaylogo', 'autoScale2d', 'resetScale2d',
                                           'hoverClosestCartesian',
                                           'lasso2d', 'zoomIn2d', 'zoomOut2d', 'zoom2d', 'select2d', 'toggleSpikelines',
                                           'hoverCompareCartesian', 'toggleHover'],
                'displayModeBar': True, 'displaylogo': False, 'toImageButtonOptions': {'format': 'png'}})
        ])
            ],style={'padding-left': 150})
    elif tab == 'tab2-graph':
        return html.Div([

            html.H3('μCT Analysis of Femur Cortical Bone',style={'margin-left':360,'padding-top':20, 'padding-bottom':20}),
            dbc.Row([
                dcc.Graph(id='box_plot31',
                          config={'modeBarButtonsToRemove': ['pan2d', 'displaylogo', 'autoScale2d', 'resetScale2d',
                                                             'hoverClosestCartesian', 'lasso2d', 'zoomIn2d',
                                                             'zoomOut2d', 'zoom2d', 'select2d', 'toggleSpikelines',
                                                             'hoverCompareCartesian', 'toggleHover'],
                                  'displayModeBar': True, 'displaylogo': False,
                                  'toImageButtonOptions': {'format': 'png'}})  # 'displayModeBar': False
            ],style={'padding-left': 150}),


            dbc.Row(
                dbc.Col([],style={'height': 3, 'padding-left':0, 'padding-right':0,'padding-bottom': 0, 'padding-top': 0, 'margin-bottom':15, 'margin-left':175,
                           'margin-right':0, 'background-color': 'black'}, width=8)
            ),

            dbc.Row([
                dcc.Graph(id='box_plot32',
                          config={'modeBarButtonsToRemove': ['pan2d', 'displaylogo', 'autoScale2d', 'resetScale2d',
                                                             'hoverClosestCartesian', 'lasso2d', 'zoomIn2d',
                                                             'zoomOut2d', 'zoom2d', 'select2d', 'toggleSpikelines',
                                                             'hoverCompareCartesian', 'toggleHover'],
                                  'displayModeBar': True, 'displaylogo': False,
                                  'toImageButtonOptions': {'format': 'png'}})  # 'displayModeBar': False

            ],style={'padding-left': 150}),
        ])

    elif tab == 'tab3-graph':
        return html.Div([
            html.H3('μCT Analysis of Vertebral Trabecular Bone',style={'padding-left':175,'padding-top':20, 'padding-bottom':20}),
            dcc.Graph(id='box_plot33', config={
                'modeBarButtonsToRemove': ['pan2d', 'displaylogo', 'autoScale2d', 'resetScale2d',
                                           'hoverClosestCartesian',
                                           'lasso2d', 'zoomIn2d', 'zoomOut2d', 'zoom2d', 'select2d', 'toggleSpikelines',
                                           'hoverCompareCartesian', 'toggleHover'],
                'displayModeBar': True, 'displaylogo': False, 'toImageButtonOptions': {'format': 'png'}})
            # 'displayModeBar': False
        ],style={'padding-left': 150})
    elif tab == 'tab4-graph':
        return html.Div([
            html.H3('Static Histomorphometric Analysis of Femur Trabecular Bone',style={'padding-left':50,'padding-top':20, 'padding-bottom':20}),
            dcc.Graph(id='box_plot34', config={
                'modeBarButtonsToRemove': ['pan2d', 'displaylogo', 'autoScale2d', 'resetScale2d',
                                           'hoverClosestCartesian',
                                           'lasso2d', 'zoomIn2d', 'zoomOut2d', 'zoom2d', 'select2d', 'toggleSpikelines',
                                           'hoverCompareCartesian', 'toggleHover'],
                'displayModeBar': True, 'displaylogo': False, 'toImageButtonOptions': {'format': 'png'}})
        ],style={'padding-left': 150})
    elif tab == 'tab5-graph':
        return html.Div([
            html.H3('Dynamic and Osteoblast Parameters of Femur Trabecular Bone',style={'padding-left': 175,'padding-top':20, 'padding-bottom':20}),
            dbc.Row([
                dcc.Graph(id='box_plot35',
                          config={'modeBarButtonsToRemove': ['pan2d', 'displaylogo', 'autoScale2d', 'resetScale2d',
                                                             'hoverClosestCartesian', 'lasso2d', 'zoomIn2d',
                                                             'zoomOut2d', 'zoom2d', 'select2d', 'toggleSpikelines',
                                                             'hoverCompareCartesian', 'toggleHover'],
                                  'displayModeBar': True, 'displaylogo': False,
                                  'toImageButtonOptions': {'format': 'png'}})  # 'displayModeBar': False
            ], style={'padding-left': 150}),
            dbc.Row([
                dbc.Col([],
                    style={'height': 3, 'padding-bottom': 0, 'padding-top': 0, 'margin-bottom': 15, 'margin-left': 175,
                           'margin-right':0, 'background-color': 'black'},width=8),
                    ]),
            dbc.Row([
                dcc.Graph(id='box_plot36',
                          config={'modeBarButtonsToRemove': ['pan2d', 'displaylogo', 'autoScale2d', 'resetScale2d',
                                                             'hoverClosestCartesian', 'lasso2d', 'zoomIn2d',
                                                             'zoomOut2d', 'zoom2d', 'select2d', 'toggleSpikelines',
                                                             'hoverCompareCartesian', 'toggleHover'],
                                  'displayModeBar': True, 'displaylogo': False,
                                  'toImageButtonOptions': {'format': 'png'}})  # 'displayModeBar': False

            ], style={'padding-left': 150}),
        ])
    elif tab == 'tab6-graph':
        return html.Div([
            html.H3('Osteoclast and Remodeling Parameters of Femur Trabecular Bone',style={'padding-left': 175,'padding-top':20, 'padding-bottom':20}),
            dbc.Row([
                 dcc.Graph(id='box_plot37',
                          config={'modeBarButtonsToRemove': ['pan2d', 'displaylogo', 'autoScale2d', 'resetScale2d',
                                                             'hoverClosestCartesian', 'lasso2d', 'zoomIn2d',
                                                             'zoomOut2d', 'zoom2d', 'select2d', 'toggleSpikelines',
                                                             'hoverCompareCartesian', 'toggleHover'],
                                  'displayModeBar': True, 'displaylogo': False,
                                  'toImageButtonOptions': {'format': 'png'}})  # 'displayModeBar': False
                     ], style={'padding-left': 150}),

            dbc.Row([
                dbc.Col([],
                    style={'height': 3, 'padding-bottom': 0, 'padding-top': 0, 'margin-bottom': 15, 'margin-left': 175,
                           'margin-right':0, 'background-color': 'black'},width=8),
                    ]),

            dbc.Row([
                dcc.Graph(id='box_plot38',
                          config={'modeBarButtonsToRemove': ['pan2d', 'displaylogo', 'autoScale2d', 'resetScale2d',
                                                             'hoverClosestCartesian', 'lasso2d', 'zoomIn2d',
                                                             'zoomOut2d', 'zoom2d', 'select2d', 'toggleSpikelines',
                                                             'hoverCompareCartesian', 'toggleHover'],
                                  'displayModeBar': True, 'displaylogo': False,
                                  'toImageButtonOptions': {'format': 'png'}})  # 'displayModeBar': False

            ], style={'padding-left': 150}),
        ]),
    elif tab == 'tab7-graph':
        return html.Div([
            html.H3('Static Histomorphometric Analysis of Vertebra Trabecular Bone',style={'padding-left': 50,'padding-top':20, 'padding-bottom':20}),
            dcc.Graph(id='box_plot39', config={
                'modeBarButtonsToRemove': ['pan2d', 'displaylogo', 'autoScale2d', 'resetScale2d',
                                           'hoverClosestCartesian',
                                           'lasso2d', 'zoomIn2d', 'zoomOut2d', 'zoom2d', 'select2d', 'toggleSpikelines',
                                           'hoverCompareCartesian', 'toggleHover'],
                'displayModeBar': True, 'displaylogo': False, 'toImageButtonOptions': {'format': 'png'}})
        ], style={'padding-left': 150})
    elif tab == 'tab8-graph':
        return html.Div([
            html.H3('Dynamic and Osteoblast Parameters of Vertebra Trabecular Bone',style={'padding-left': 175,'padding-top':20, 'padding-bottom':20}),
            dbc.Row([
                 dcc.Graph(id='box_plot40',
                          config={'modeBarButtonsToRemove': ['pan2d', 'displaylogo', 'autoScale2d', 'resetScale2d',
                                                             'hoverClosestCartesian', 'lasso2d', 'zoomIn2d',
                                                             'zoomOut2d', 'zoom2d', 'select2d', 'toggleSpikelines',
                                                             'hoverCompareCartesian', 'toggleHover'],
                                  'displayModeBar': True, 'displaylogo': False,
                                  'toImageButtonOptions': {'format': 'png'}})  # 'displayModeBar': False
                     ], style={'padding-left': 150}),

            dbc.Row([
                dbc.Col([],
                    style={'height': 3, 'padding-bottom': 0, 'padding-top': 0, 'margin-bottom': 15, 'margin-left': 175,
                           'margin-right':0, 'background-color': 'black'},width=8),
                    ]),

            dbc.Row([
                dcc.Graph(id='box_plot41',
                          config={'modeBarButtonsToRemove': ['pan2d', 'displaylogo', 'autoScale2d', 'resetScale2d',
                                                             'hoverClosestCartesian', 'lasso2d', 'zoomIn2d',
                                                             'zoomOut2d', 'zoom2d', 'select2d', 'toggleSpikelines',
                                                             'hoverCompareCartesian', 'toggleHover'],
                                  'displayModeBar': True, 'displaylogo': False,
                                  'toImageButtonOptions': {'format': 'png'}})  # 'displayModeBar': False

            ], style={'padding-left': 150}),
        ]),
    elif tab == 'tab9-graph':
        return html.Div([
            html.H3('Osteoclast and Remodeling Parameters of Vertebra Trabecular Bone',style={'text-align': 'center', 'margin-left':70,'padding-top':20, 'padding-bottom':20}),
            dbc.Row([
                 dcc.Graph(id='box_plot42',
                          config={'modeBarButtonsToRemove': ['pan2d', 'displaylogo', 'autoScale2d', 'resetScale2d',
                                                             'hoverClosestCartesian', 'lasso2d', 'zoomIn2d',
                                                             'zoomOut2d', 'zoom2d', 'select2d', 'toggleSpikelines',
                                                             'hoverCompareCartesian', 'toggleHover'],
                                  'displayModeBar': True, 'displaylogo': False,
                                  'toImageButtonOptions': {'format': 'png'}})  # 'displayModeBar': False
                     ], style={'padding-left': 150}),

            dbc.Row([
                dbc.Col([],
                    style={'height': 3, 'padding-bottom': 0, 'padding-top': 0, 'margin-bottom': 15, 'margin-left': 175,
                           'margin-right':0, 'background-color': 'black'},width=8),
                    ]),

            dbc.Row([
                dcc.Graph(id='box_plot43',
                          config={'modeBarButtonsToRemove': ['pan2d', 'displaylogo', 'autoScale2d', 'resetScale2d',
                                                             'hoverClosestCartesian', 'lasso2d', 'zoomIn2d',
                                                             'zoomOut2d', 'zoom2d', 'select2d', 'toggleSpikelines',
                                                             'hoverCompareCartesian', 'toggleHover'],
                                  'displayModeBar': True, 'displaylogo': False,
                                  'toImageButtonOptions': {'format': 'png'}})  # 'displayModeBar': False

            ], style={'padding-left': 150}),
        ]),

