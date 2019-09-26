from loguru import logger
import dash_core_components as dcc
import dash_html_components as html
from collections import namedtuple


Tab = namedtuple("Tab", "header content")


def tab(name="", size="", children=[], active=False):
    # TODO: children size
    if active:
        class_active = "active"
    else:
        class_active = ""
    t = Tab(
        header=html.Li(
            className=f"tab col {size}",
            children=[html.A(className=f"{class_active}", children=[name], href=f"#{name}")],
        ),
        content=html.Div(className="col", id=f"{name}", children=children),
    )
    return t


def tabs(tabs=[]):
    #TODO: color
    headers = html.Ul(className="tabs", children=[t.header for t in tabs])
    content = set([t.content for t in tabs])
    return html.Div(children=[headers, *content])
