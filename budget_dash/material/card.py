import dash_core_components as dcc
import dash_html_components as html


def card(card_id=None, card_title="", card_content=[], card_action=[], card_image=None):
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.Span(f"{card_title}", className="card-title"),
                    *[card_content],
                ],
                className="card-content",
            ),
            html.Div(children=list(card_action), className="card-action"),
        ],
        className="card",
    )
