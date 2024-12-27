from kafka import KafkaProducer
import json
import time
import random

# Initialize the Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# List of sample stocks to simulate
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

def generate_stock_data():
    """Simulates stock price data."""
    stock = random.choice(stocks)
    price = round(random.uniform(100, 1500), 2)  # Random stock price between $100 and $1500
    timestamp = time.time()
    return {
        'stock': stock,
        'price': price,
        'timestamp': timestamp
    }

if __name__ == '__main__':
    while True:
        stock_data = generate_stock_data()
        producer.send('activity_topic', value=stock_data)
        print(f"Sent data: {stock_data}")
        time.sleep(1)  # Publish data every second
