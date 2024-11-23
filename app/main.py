from dash import dcc, html, dash
import dash_bootstrap_components as dbc
import flask


app= flask.Flask(__name__)
dash_app = dash.Dash(__name__, server=app, external_stylesheets=[dbc.themes.BOOTSTRAP])
dash_app.config.suppress_callback_exceptions = True

dash_app.layout = html.Div(
    children=[
        html.H1(children="FreeBirds Crew"),
        html.Div(children="""Docker Conatiner Running DASH WebApp"""),
        dcc.Graph(
            id="example-graph",
            figure={
                "data": [
                    {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "Like"},
                    {
                        "x": [1, 2, 3],
                        "y": [2, 4, 5],
                        "type": "bar",
                        "name": "Comment",
                    },
                ],
                "layout": {"title": "Atualização teste"},
            },
        ),
    ]
)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=8085)