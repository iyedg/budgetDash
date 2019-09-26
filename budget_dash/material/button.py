import dash_core_components as dcc
import dash_html_components as html


def button(name="", fab=False, icon=None, *args, **kwargs):
    # TODO: work on icon
    if fab:
        return html.Div(
            className="fixed-action-btn",
            children=[
                html.A(
                    *args,
                    **kwargs,
                    className="btn-floating btn-large red",
                    children=[icon]
                )
            ],
        )
    else:
        return html.A(*args, **kwargs, className="btn", children=[icon, name])

