from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from kafka import KafkaConsumer
import json
import threading

app = Dash(__name__)

# Initialize Kafka consumer
consumer = KafkaConsumer(
    'activity_topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Shared DataFrame to store stock data
data_df = pd.DataFrame(columns=['stock', 'price', 'timestamp'])

def consume_data():
    global data_df
    for message in consumer:
        stock_data = message.value
        data_df = pd.concat([data_df, pd.DataFrame([stock_data])], ignore_index=True)
        data_df = data_df.tail(100)  # Keep only the last 100 entries for the graph

# Start Kafka consumer in a separate thread
consumer_thread = threading.Thread(target=consume_data)
consumer_thread.daemon = True
consumer_thread.start()

# Dashboard layout
app.layout = html.Div([
    html.H1("Real-Time Stock Price Dashboard"),
    dcc.Graph(id='stock-price-graph'),
    dcc.Interval(
        id='interval-component',
        interval=1000,  # Update every second
        n_intervals=0
    )
])

@app.callback(
    Output('stock-price-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n_intervals):
    global data_df
    if data_df.empty:
        return dash.no_update

    fig = px.line(data_df, x='timestamp', y='price', color='stock', title="Real-Time Stock Prices")
    fig.update_layout(xaxis_title='Time', yaxis_title='Price (USD)')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
