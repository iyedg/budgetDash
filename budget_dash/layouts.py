import dash_core_components as dcc
import dash_html_components as html
from .material.card import card


layout = html.Div(
    [
        html.H3("Hello world"),
        card(
            card_title="function generated card",
            card_content=html.P("This is new"),
            card_action=[dcc.Link("Hide")],
        ),
    ],
    className="container",
)

