import dash_core_components as dcc
import dash_html_components as html
from .material.card import card
from .material.stepper import stepper, step
from .material.text_input import text_input
from .material.grid import row, column


layout = html.Div(
    [
        row(
            [
                column(
                    text_input(
                        input_id="organization",
                        label="Select organization",
                        _type="number",
                    ),
                    "s4",
                ),
                column(
                    text_input(
                        input_id="mission", label="Select mission", _type="password"
                    ),
                    size="s4",
                ),
                column(
                    text_input(input_id="email", label="Select mission", _type="email"),
                    size="s3",
                ),
            ]
        )
    ],
    className="container",
)
