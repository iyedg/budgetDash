import dash_core_components as dcc
import dash_html_components as html

from .material.card import card
from .material.grid import column, row, container
from .material.text_input import text_input
from .material.icon import icon
from .material.button import button

layout = container(
    row(
        column(
            size="s12",
            children=card(
                card_title="Saisie budget",
                card_content=[
                    row(column(size="s12", children=text_input("mission", "Mission"))),
                    row(
                        column(
                            size="s12",
                            children=text_input("organization", "Organisation"),
                        )
                    ),
                    row(
                        column(
                            size="s12", children=button(fab=True, icon=icon("cloud"))
                        )
                    ),
                    row(
                        column(
                            size="s12", children=button(name="add", icon=icon("add", side="right"))
                        )
                    ),
                ],
            ),
        )
    )
)
