import dash   # Servidor Flask
import dash_core_components as dcc  # Graficacion
import dash_html_components as html # HTML
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
        children=["Dashboard COVID-19"],
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Graph(
        id="graph1",
        figure={
            'data': [
                {'x': fechas_mexico[:-1], 'y': casos_mexico[:-1], 'type': 'line', 'name': 'Mexico'},
                {'x': fechas_peru[:-1], 'y': casos_peru[:-1], 'type': 'line', 'name': 'Peru'},
                {'x': fechas_ecuador[:-1], 'y': casos_ecuador[:-1], 'type': 'line', 'name': 'Ecuador'},
                {'x': fechas_brasil[:-1], 'y': casos_brasil[:-1], 'type': 'line', 'name': 'Brasil'},
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
    Este es un dashboard de ejemplo donde mostramos la información recogida de la API [covid19api.com](https://api.covid19api.com/) de casos confirmados diferentes países de America Latina.

    Para mostrar estos resultados, se utilizó [Dash](https://dash.plotly.com/) y [Heroku](https://dashboard.heroku.com) para subir este código a la nube.

    Código fuente: https://github.com/checor/covid-dashboard
    """, style={
        'color': colors['text']
    })
])

if __name__ == "__main__":
    app.run_server(debug=True)