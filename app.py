import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

from dash.dependencies import Input, Output

data = pd.read_csv("county_dataset.csv")

bribery_prevalence=pd.read_csv('bribery_prevalence.csv')

app = dash.Dash(__name__)




fig = px.scatter(data, x=data['2015_avg_bribe'], y=data['total_gcp'],
                 size=data['total_population19'], color="2015_avg_time_bribe_paid", hover_name="county_name",
                 log_x=True, size_max=60)




fig1 = px.bar(data, x=data['county_name'], y=data['2015_avg_bribe'], barmode="group")
fig2 = px.bar(data, x=data['county_name'], y=data['2016_avg_bribe'], barmode="group")
fig3 = px.bar(data, x=data['county_name'], y=data['2017_avg_bribe'], barmode="group")


app.layout = html.Div([
    html.Br(),
    html.H1(children='Incredibles corruption Analysis ',
            style={"fontSize": "48px", "color": "red", 'text-align':'center', 'font-weight': '900', 'text-shadow': '0 1px 0 rgba(255, 255, 255, 0.4)'},),
    html.Br(),
    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': '2015', 'value': '2015_avg_bribe'},
            {'label': '2016', 'value': '2016_avg_bribe'},
            {'label': '2017', 'value': '2017_avg_bribe'},
            {'label': '2018', 'value': '2018_avg_bribe'}
        ],
        value=data['2015_avg_bribe']
    ),

    html.Div(id='dd-output-container'),

    dcc.Graph(
        figure=fig1,
    ),

    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    ),

    dcc.Graph(
figure={
                "data": [
                    {
                        "x": bribery_prevalence['Institution'],
                        "y": bribery_prevalence['Bribery Prevalence by percentage'],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Institutions and Bribery Prevalence"},
            },

    )
])

if __name__ == '__main__':
    app.run_server(port=8050)