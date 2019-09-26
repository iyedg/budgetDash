import dash

external_stylesheets = [
    "https://fonts.googleapis.com/icon?family=Material+Icons",
    "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css",
    "https://unpkg.com/materialize-stepper@3.1.0/dist/css/mstepper.min.css",
]
external_scripts = [
    "https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js",
    "https://unpkg.com/materialize-stepper@3.0.0/dist/js/mstepper.min.js",
]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
)
server = app.server
app.config.suppress_callback_exceptions = True
