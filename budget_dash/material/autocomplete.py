import dash_core_components as dcc
import dash_html_components as html

from .text_input import text_input


def autocomplete(autocomplete_id="", icon=None, label=""):
    return html.Div(className="input-field", children=[
        icon, text_input(input_id=autocomplete_id, label=label, className="autocomplete")
    ])
