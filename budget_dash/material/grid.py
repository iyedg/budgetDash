import dash_core_components as dcc
import dash_html_components as html


def row(children):
    return html.Div(className="row", children=children)


def column(children, size):
    className = f"col {size}"
    return html.Div(className=className, children=children)
