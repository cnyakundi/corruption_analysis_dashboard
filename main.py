# # import dash
# from dash import dcc
# from dash import html
# import plotly.express as px
# import pandas as pd
#
# from dash.dependencies import Input, Output
#
# data = pd.read_csv("county_dataset.csv")
#
#



#
# bribery_prevalence = pd.read_csv('bribery_prevalence.csv')
#
# app = dash.Dash(__name__)
#
# fig = px.scatter(data, x=data['2015_avg_bribe'], y=data['total_gcp'],
#                  size=data['total_population19'], color="2015_avg_time_bribe_paid", hover_name="county_name",
#                  log_x=True, size_max=60)
#
# fig1 = px.bar(data, x=data['county_name'], y=data['2015_avg_bribe'], barmode="group")
# fig2 = px.bar(data, x=data['county_name'], y=data['2016_avg_bribe'], barmode="group")
# fig3 = px.bar(data, x=data['county_name'], y=data['2017_avg_bribe'], barmode="group")
#
# app.layout = html.Div([
#     html.Br(),
#     html.H1(children='Incredibles corruption Analysis ',
#             style={"fontSize": "48px", "color": "red", 'text-align': 'center', 'font-weight': '900',
#                    'text-shadow': '0 1px 0 rgba(255, 255, 255, 0.4)'}, ),
#     html.Br(),
#     dcc.Dropdown(
#         id='demo-dropdown',
#         options=[
#             {'label': 'kisii', 'value': data['county_name']},
#             {'label': 'kilifi', 'value': 'kilifi'},
#             {'label': 'migori', 'value': 'migori'},
#             {'label': 'laikipia', 'value': 'laikipia'}
#         ],
#         value='laikipia'
#     ),
#
#     html.Div(id='dd-output-container'),
#
#     dcc.Graph(
#         figure=fig2
#     ),
#
#     dcc.Graph(
#         id='life-exp-vs-gdp',
#         figure=fig
#     ),
#
#     dcc.Graph(
#         figure={
#             "data": [
#                 {
#                     "x": bribery_prevalence['Institution'],
#                     "y": bribery_prevalence['Bribery Prevalence by percentage'],
#                     "type": "lines",
#                 },
#             ],
#             "layout": {"title": "Institutions and Bribery Prevalence"},
#         },
#
#     )
# ])
#
#
# @app.callback(
#     [Output(component_id='output_container', component_property='children')],
#
#     [Input(component_id='slct_county', component_property='value')]
# )
# def update_chart(option_slctd):
#     # print(option_slctd)
#     print(type(option_slctd))
#
#     container = "The year chosen by user was: {}".format(option_slctd)
#
#     dff = data.copy()
#     dff = dff[dff["county_name"] == option_slctd]
#     # dff = dff[dff["Entity"] == "Entity"]
#
#
# if __name__ == '__main__':
#     app.run_server(port=8050)
