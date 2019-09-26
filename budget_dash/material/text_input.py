import dash_core_components as dcc
import dash_html_components as html
from loguru import logger


def text_input(
    input_id, label="", value="", _type="text", placeholder="", *args, **kwargs
):
    ALLOWED_TYPES = (
        "text",
        "number",
        "password",
        "email",
        "search",
        "tel",
        "url",
        "range",
        "hidden",
    )
    if _type not in ALLOWED_TYPES:
        logger.error(
            f"the type {_type} for {input_id} is not in {ALLOWED_TYPES}, setting it to 'text'"
        )
        _type = "text"
    if value != "":
        label_active = "active"
    else:
        label_active = ""
    logger.debug(_type)
    return html.Div(
        className="input-field",
        children=[
            html.Label(label, className=label_active),
            dcc.Input(
                *args,
                **kwargs,
                id=input_id,
                placeholder=placeholder,
                value=value,
                type=_type,
            ),
        ],
    )

