from dash import Dash, html, dcc, Input, Output
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc

# 2024-03-26: from
# 100 simple examples of Dash components interacting with Plotly graphs
# https://dash-example-index.herokuapp.com
# through
# Dash in 20 minutes
# https://dash.plotly.com/tutorial

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

heading = html.H4(
    "Normal Distribution Simulation", className="bg-primary text-white p-2"
)


sample_size = html.Div(
    [
        dbc.Label("Sample Size", html_for="size"),
        dcc.Slider(1, 1000, value=250, id="size",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)


n_bins = html.Div(
    [
        dbc.Label("Number of Bins", html_for="n_bins"),
        dcc.Slider(1, 100, 10, value=20, id="n_bins",
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ],
    className="mt-2",
)

mean = html.Div(
    [dbc.Label("Mean", html_for="mean"), dbc.Input(id="mean", type="number", value=0)],
    className="mt-2",
)

std_dev = html.Div(
    [
        dbc.Label("Standard Deviation", html_for="std_dev"),
        dbc.Input(id="std_dev",type="number", value=1),
    ],
    className="mt-2",
)

control_panel = dbc.Card(
    dbc.CardBody(
        [sample_size, n_bins, mean, std_dev],
        className="bg-light",
    )
)

graph = dbc.Card(
    [html.Div(id="error_msg", className="text-danger"), dcc.Graph(id="graph")]
)

app.layout = html.Div(
    [heading, dbc.Row([dbc.Col(control_panel, md=4), dbc.Col(graph, md=8)])]
)


@app.callback(
    Output("graph", "figure"),
    Output("error_msg", "children"),
    Input("mean", "value"),
    Input("std_dev", "value"),
    Input("n_bins", "value"),
    Input("size", "value"),
)
def callback(m, std_dev, n_bins, n):
    if m is None or std_dev is None:
        return {}, "Please enter Standard Deviation and Mean"
    if std_dev < 0:
        return {}, "Please enter Standard Deviation > 0"
    data = np.random.normal(m, std_dev, n)
    return px.histogram(data, nbins=n_bins), None


if __name__ == "__main__":
    app.run_server(debug=True)