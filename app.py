import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import dash_table
import pandas as pd
import numpy as np

#data = pd.read_csv("https://raw.githubusercontent.com/dnzengou/provsvar_notebook/main/data/provsvar_sept_anonym_122021-Blad11_mal_full.csv")
data = pd.read_csv('data/provsvar_sept_anonym_122021-Blad11_mal_full_clean.csv') #with index
#data = pd.read_csv('data/provsvar_sept_anonym_full_clean_indexed.csv') # with 

# data cleaning
# renaming the df column names to lowercase
data.columns = map(str.lower, data.columns)

data.rename(columns = {'provsvar 1':'provsvar1', 'provsvar 2':'provsvar2', 'provsvar 3':'provsvar3', 'provsvar 4':'provsvar4', 'provsvar 5':'provsvar5', 'provsvar 6':'provsvar6', 'värde 1':'varde1', 'värde 2':'varde2', 'värde 3':'varde3', 'värde 4':'varde4', 'värde 5':'varde5',
                              'värde 6':'varde6', 'bedömning 1':'bedomning1', 'bedömning 2':'bedomning2', 'bedömning 3':'bedomning3', 'bedömning 4':'bedomning4', 'bedömning 5':'bedomning5', 'total bedomning':'total_bedomning'}, inplace = True)


#data = data.query("total_bedomning == 'GRON'")
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
server = app.server

app.title = "Patient Provsvar Analytics: Visualize Your Patient Test Results!"



app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="👩🏽‍⚕️", className="header-emoji"),
                html.H1(
                    children="Patient Provsvar Analytics", className="header-title"
                ),
                html.P(
                    children="Analyze the trends among patient test results"
                    " based on the 'bedömning' (GRON/GUL/RÖD)"
                    " over time",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Värde 1", className="menu-title"),
                        dcc.Dropdown(
                            id="varde1-filter",
                            options=[
                                {"label": varde1, "value": varde1}
                                for varde1 in np.sort(data.varde1.unique())
                            ],
                            value="13",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Värde 2", className="menu-title"),
                        dcc.Dropdown(
                            id="varde2-filter",
                            options=[
                                {"label": varde2, "value": varde2}
                                for varde2 in data.varde2.unique()
                            ],
                            value="0.92",
                            clearable=False,
                            searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range",
                            className="menu-title"
                            ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=data.provsvarsdate.min().date(),
                            max_date_allowed=data.provsvarsdate.max().date(),
                            start_date=data.provsvarsdate.min().date(),
                            end_date=data.provsvarsdate.max().date(),
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        
        html.Div(
            dash_table.DataTable(
                id='table-paging-with-graph',
                columns=[
                    {"name": i, "id": i} for i in sorted(data.columns)
                ],
                page_current=0,
                page_size=20,
                page_action='custom',

                filter_action='custom',
                filter_query='',

                sort_action='custom',
                sort_mode='multi',
                sort_by=[]
            ),
            style={'height': 750, 'overflowY': 'scroll'},
            className='six columns'
        ),
        html.Div(
            id='table-paging-with-graph-container',
            className="five columns"
        ),
        
        
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="varde1-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["personnummer"],
                                    "y": data["varde1"],
                                    "type": "bar",
                                    "marker": {"color": "#0074D9"},
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Värde 1 av personnummer",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#0074D9"],
                            },
                        },
                    ),                    
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="varde2-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["personnummer"],
                                    "y": data["varde2"],
                                    "type": "bar",
                                    "marker": {"color": "#0074D9"},
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Värde 2 av personnummer",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#0074D9"],
                            },
                        },
                    ),                    
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="varde3-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["personnummer"],
                                    "y": data["varde3"],
                                    "type": "bar",
                                    "marker": {"color": "#0074D9"},
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Värde 3 av personnummer",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#0074D9"],
                            },
                        },
                    ),                    
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="varde4-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["provsvarsdate"],
                                    "y": data["varde4"],
                                    "type": "lines",
                                    "hovertemplate": "%{y:.2f}"
                                                     "<extra></extra>",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Värde 4 över tiden",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": " ",
                                    "fixedrange": True,
                                },
                                "colorway": ["#8AD868"],
                            },
                        },
                    ),
                    className="card",
                ),                    
                html.Div(
                    children=dcc.Graph(
                        id="varde5-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["provsvarsdate"],
                                    "y": data["varde5"],
                                    "type": "lines",
                                },
                            ],
                            "layout": {
                                "title": {
                                    "text": "Värde 5 över tiden",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#8AD868"],
                            },
                        },
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)




operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]


def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]

                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part

                # word operators need spaces after them in the filter string,
                # but we don't want these later
                return name, operator_type[0].strip(), value

    return [None] * 3


@app.callback(
    Output('table-paging-with-graph', "data"),
    Input('table-paging-with-graph', "page_current"),
    Input('table-paging-with-graph', "page_size"),
    Input('table-paging-with-graph', "sort_by"),
    Input('table-paging-with-graph', "filter_query"))
def update_table(page_current, page_size, sort_by, filter):
    filtering_expressions = filter.split(' && ')
    dff = data
    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)

        if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
            # these operators match pandas series operator method names
            dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
        elif operator == 'contains':
            dff = dff.loc[dff[col_name].str.contains(filter_value)]
        elif operator == 'datestartswith':
            # this is a simplification of the front-end filtering logic,
            # only works with complete fields in standard format
            dff = dff.loc[dff[col_name].str.startswith(filter_value)]

    if len(sort_by):
        dff = dff.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )

    return dff.iloc[
        page_current*page_size: (page_current + 1)*page_size
    ].to_dict('records')






@app.callback(
    [Output("varde1-chart", "figure"), Output("varde2-chart", "figure")],
    [
        Input("varde1-filter", "value"),
        Input("varde2-filter", "value"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date"),
    ],
)
def update_charts(varde1, varde2, start_date, end_date):
    mask = (
        (data.varde1 == varde1)
        & (data.varde2 == varde2)
        & (data.provsvarsdate >= start_date)
        & (data.provsvarsdate <= end_date)
    )
    filtered_data = data.loc[mask, :]
    varde1_chart_figure = {
        "data": [
            {
                "x": filtered_data["provsvarsdate"],
                "y": filtered_data["varde1"],
                "type": "lines",
                "hovertemplate": "%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Varde 1 över tiden",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "", "fixedrange": True},
            "colorway": ["#17B897"],
        },
    }

    varde2_chart_figure = {
        "data": [
            {
                "x": filtered_data["provsvarsdate"],
                "y": filtered_data["varde2"],
                "type": "lines",
            },
        ],
        "layout": {
            "title": {"text": "Varde 2 över tiden", "x": 0.05, "xanchor": "left"},
            "xaxis": {"fixedrange": True},
            "yaxis": {"fixedrange": True},
            "colorway": ["#E12D39"],
        },
    }
    return varde1_chart_figure, varde2_chart_figure



@app.callback(
    Output('table-paging-with-graph-container', "children"),
    Input('table-paging-with-graph', "data"))
def update_graph(rows):
    dff = pd.DataFrame(rows)
    return html.Div(
        [
            dcc.Graph(
                id=column,
                figure={
                    "data": [
                        {
                            "x": dff["provsvarsdate"],
                            #"x": dff["personnummer"],
                            "y": dff[column] if column in dff else [],
                            #"type": "bar",
                            "type": "lines",
                            "marker": {"color": "#0074D9"},
                        }
                    ],
                    "layout": {
                                "title": {
                                    "text": "Värde 1, 2 och 3 över tiden",
                                    "x": 0.1,
                                    "xanchor": "left",
                                },
                        "xaxis": {"automargin": True},
                        "yaxis": {"automargin": True},
                        "height": 300,
                        "margin": {"t": 30, "l": 30, "r": 30},
                    },
                },
            )
            for column in ["varde1", "varde2", "varde3"]
        ]
    )




if __name__ == "__main__":
    app.run_server(debug=True)