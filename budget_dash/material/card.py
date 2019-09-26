import dash_core_components as dcc
import dash_html_components as html

from loguru import logger


def card(card_id=None, card_title="", card_content=[], card_action=[], card_image=None):
    return html.Div(
        className="card",
        children=[
            html.Div(
                className="card-content",
                children=[
                    html.Span(f"{card_title}", className="card-title"),
                    *card_content,
                ],
            ),
            html.Div(children=card_action, className="card-action"),
        ],
    )
