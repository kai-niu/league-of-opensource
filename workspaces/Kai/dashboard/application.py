import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import requests
import pandas as pd
import json

df = pd.read_csv('https://github.com/kai-niu/league-of-opensource/raw/main/assets/dataset/relocation_db_with_gender.csv', index_col=None)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['BIRTH_YEAR'].min(),
        max=df['BIRTH_YEAR'].max(),
        value=df['BIRTH_YEAR'].min(),
        marks={str(year): str(year) for year in df['BIRTH_YEAR'].unique()},
        step=None
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.BIRTH_YEAR <= selected_year]

    # call endpoint to score
    gender = filtered_df.loc[:,'GENDER']
    X = filtered_df.drop(['GENDER','life_allocation'], axis=1)

    # api-endpoint 
    URL = "https://rqg11l7hg2.execute-api.us-west-1.amazonaws.com/life-relocation-model"

    # send some queries
    headers = {"Content-Type":"application/json"}
    p = {"data": X.values.tolist()}
    r = requests.post(url = URL, data = json.dumps(p), headers=headers)  
    y_hat = r.json()['label']

    # join result
    X['Prediction'] = y_hat
    X['Gender'] = gender

    fig = px.bar(X, x="Prediction", y='Gender')
    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)