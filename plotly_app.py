import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import dash_table
import pandas as pd

df = pd.read_csv('../data/provsvar_sept_anonym_122021-Blad11_mal_full_clean.csv')
#df = pd.read_csv('https://raw.githubusercontent.com/dnzengou/provsvar_notebook/main/data/provsvar_sept_anonym_full_clean_indexed.csv')

df[' index'] = range(1, len(df) + 1)

app = dash.Dash(__name__)

PAGE_SIZE = 5


external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Patient provsvar analytics"


app.layout = html.Div(
    className="row",
    children=[
        html.Div(
            dash_table.DataTable(
                id='table-paging-with-graph',
                columns=[
                    {"name": i, "id": i} for i in sorted(df.columns)
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
        )
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
    dff = df
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
                            #"x": dff["provsvarsdate"],
                            "x": dff["personnummer"],
                            "y": dff[column] if column in dff else [],
                            "type": "bar",
                            "marker": {"color": "#0074D9"},
                        }
                    ],
                    "layout": {
                        "xaxis": {"automargin": True},
                        "yaxis": {"automargin": True},
                        "height": 250,
                        "margin": {"t": 10, "l": 10, "r": 10},
                    },
                },
            )
            for column in ["varde1", "varde2", "varde3"]
        ]
    )




#app.layout = html.Div([
#    dash_table.DataTable(
        #id='datatable-paging-page-count',
        #id='table-paging-and-sorting',
#        id='table-filtering',
#        columns=[
#            {"name": i, "id": i, 'deletable': True} for i in sorted(df.columns)
#        ],
#        page_current=0,
#        page_size=PAGE_SIZE,
#        page_action='custom',
        
#        sort_action='custom',
#        sort_mode='single',
#        sort_by=[],
        
#        filter_action='custom',
#        filter_query=''
#    )
    
    #,html.Br(),
    #dcc.Checklist(
    #    id='datatable-use-page-count',
    #    options=[
    #        {'label': 'Use page_count', 'value': 'True'}
    #    ],
    #    value=['True']
    #),
    #'Page count: ',
    #dcc.Input(
    #    id='datatable-page-count',
    #    type='number',
    #    min=1,
    #    max=29,
    #    value=20
    #)
#])

#def update_table(page_current, page_size, sort_by):
#    if len(sort_by):
#        dff = df.sort_values(
#            sort_by[0]['column_id'],
#            ascending=sort_by[0]['direction'] == 'asc',
#            inplace=False
#        )
#    else:
#        # No sort is applied
#        dff = df

#    return dff.iloc[
#        page_current*page_size:(page_current+ 1)*page_size
#    ].to_dict('records')


#@app.callback(
#    Output('datatable-paging-page-count', 'data'),
#    Input('datatable-paging-page-count', "page_current"),
#    Input('datatable-paging-page-count', "page_size"))
#def update_table(page_current,page_size):
#    return df.iloc[
#        page_current*page_size:(page_current+ 1)*page_size
#    ].to_dict('records')

#@app.callback(
#    Output('datatable-paging-page-count', 'page_count'),
#    Input('datatable-use-page-count', 'value'),
#    Input('datatable-page-count', 'value'))
#def update_table(use_page_count, page_count_value):
#    if len(use_page_count) == 0 or page_count_value is None:
#        return None
#    return page_count_value


if __name__ == '__main__':
    app.run_server(debug=True)
    