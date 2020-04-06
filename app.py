import dash
import dash_core_components as dcc
import dash_html_components as html
from covid import fechas_mexico, casos_mexico
from covid import fechas_peru, casos_peru
from covid import fechas_ecuador, casos_ecuador
from covid import fechas_brasil, casos_brasil

app = dash.Dash(__name__)
server = app.server

colors = {
    'background': "#111111",
    'text': "#7FDBFF"
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children=["Mi primer dashboard"],
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Graph(
        id="graph1",
        figure={
            'data': [
                {'x': fechas_mexico, 'y': casos_mexico, 'type': 'line', 'name': 'Mexico'},
                {'x': fechas_peru, 'y': casos_peru, 'type': 'line', 'name': 'Peru'},
                {'x': fechas_ecuador, 'y': casos_ecuador, 'type': 'line', 'name': 'Ecuador'},
                {'x': fechas_brasil, 'y': casos_brasil, 'type': 'line', 'name': 'Brasil'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),
    dcc.Markdown(children="""
    ## Casos de Covid-19
    Este es un dashboard de ejemplo donde mostramos la información recogida de la API [covid19api.com](https://api.covid19api.com/) de diferentes países de America Latina.
    """, style={
        'color': colors['text']
    })
])

if __name__ == "__main__":
    app.run_server(debug=True)