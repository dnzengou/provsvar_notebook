import dash
from dash import dcc
from dash import html
import pandas as pd

#data = pd.read_csv("https://raw.githubusercontent.com/dnzengou/provsvar_notebook/main/data/provsvar_sept_anonym_122021-Blad11_mal_full.csv")
data = pd.read_csv('data/provsvar_sept_anonym_122021-Blad11_mal_full_clean.csv')

# data cleaning
# renaming the df column names to lowercase
data.columns = map(str.lower, data.columns)

data.rename(columns = {'provsvar 1':'provsvar1', 'provsvar 2':'provsvar2', 'provsvar 3':'provsvar3', 'provsvar 4':'provsvar4', 'provsvar 5':'provsvar5', 'provsvar 6':'provsvar6', 'värde 1':'varde1', 'värde 2':'varde2', 'värde 3':'varde3', 'värde 4':'varde4', 'värde 5':'varde5',
                              'värde 6':'varde6', 'bedömning 1':'bedomning1', 'bedömning 2':'bedomning2', 'bedömning 3':'bedomning3', 'bedömning 4':'bedomning4', 'bedömning 5':'bedomning5', 'total bedomning':'total_bedomning'}, inplace = True)


data = data.query("total_bedomning == 'GRON'")
data["provsvarsdate"] = pd.to_datetime(data["provsvarsdate"], format="%d/%m/%Y")
data.sort_values("provsvarsdate", inplace=True)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

# create an instance of the Dash class: nitializing a Dash class by initializing a WSGI application using Dash(__name__)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Patient Provsvar Analytics: Visualize Your Patient Test Results!"

app.layout = html.Div(
    children=[
        html.P(children="👩🏽‍⚕️", className="header-emoji"),
        html.H1(
                    children="Patient Provsvar Analytics", className="header-title"
                ),
        html.P(
            children="Analyze the trends among patient test results"
            " based on the 'bedömning' (GRON/GUL/RÖD)"
            " over time",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["provsvarsdate"],
                        "y": data["varde1"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Värde 1 över tiden"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["provsvarsdate"],
                        "y": data["varde2"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Värde 2 över tiden"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["provsvarsdate"],
                        "y": data["varde2"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Värde 2 över tiden"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["provsvarsdate"],
                        "y": data["varde3"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Värde 3 över tiden"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["provsvarsdate"],
                        "y": data["varde4"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Värde 4 över tiden"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["provsvarsdate"],
                        "y": data["varde5"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Värde 5 över tiden"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)