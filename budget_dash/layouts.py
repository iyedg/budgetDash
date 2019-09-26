import dash_core_components as dcc
import dash_html_components as html

from .material.card import card
from .material.grid import column, row, container
from .material.text_input import text_input
from .material.icon import icon
from .material.button import button
from .material.tabs import tabs, tab
from .material.autocomplete import autocomplete


layout = container(
    [
        card(
            card_title="Saisie",
            card_content=[
                tabs(
                    [
                        tab(
                            name="General",
                            size="s3",
                            children=[
                                text_input(input_id="general_input", label="General"),
                                autocomplete(autocomplete_id="orgs", label="Organizations")
                            ],
                            active=True,
                        ),
                        tab(
                            name="Budget",
                            size="s3",
                            children=[html.P("Budget paragraph content")],
                        ),
                    ]
                ),
            ],
        ),
    ]
)

