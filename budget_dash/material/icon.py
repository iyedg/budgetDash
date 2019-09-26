from loguru import logger
import dash_core_components as dcc
import dash_html_components as html


def icon(name, size="", side=""):
    sizes = ("tiny", "small", "medium", "large", "")
    if size not in sizes:
        logger.error(f"{size} is not a valid size, setting size to 'small'")
        size = "small"
    return html.I(name, className=f"material-icons {size} {side}")
