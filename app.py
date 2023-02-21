# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from utils import Database

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Period": ["1M", "3M", "6M", "YTD", "1Y", "3Y", "1M", "3M", "6M", "YTD", "1Y", "3Y"],
    "Rtn": [20.3, 33.2, 32.2, 20.3, 18.5, 70.2, 20.3, 33.2, 32.2, 20.3, 18.5, 70.2],
    "Cat": ['Port'] * 6 + ['BM'] * 6
})

px
fig = px.bar(df, x="Period", y="Rtn", color="Cat", barmode="group")
fig2 = px.bar(df, x='date', y='return (%)')
fig3 = px.line(df, x='Period', y='Rtn')

app.layout = html.Div(children=[
    html.H1(children='Hello Dash', style={'text-align':'center'}),

    html.Div(children =[
        dcc.Graph(id='performance', figure=fig, style={'display': 'inline-block', 'width':'50%'}),
        dcc.Graph(id='monthly-performance', figure=fig2, style={'display': 'inline-block', 'width':'50%'})
    ]),

    html.Div(children =[
        dcc.Graph(id='performance', figure=fig3, style={'display': 'inline-block', 'width':'50%'}),
        dcc.Graph(id='monthly-performance', figure=fig3, style={'display': 'inline-block', 'width':'50%'})
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)