import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from budget_dash.app import app
from budget_dash.layouts import layout
import budget_dash.callbacks as callbacks

app.layout = layout


if __name__ == "__main__":
    app.run_server(debug=True)
