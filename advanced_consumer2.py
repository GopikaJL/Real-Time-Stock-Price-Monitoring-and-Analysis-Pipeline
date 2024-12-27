from kafka import KafkaConsumer
import json

# Initialize the Kafka Consumer
consumer = KafkaConsumer(
    'activity_topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

if __name__ == '__main__':
    print("Starting stock price consumer...")
    for message in consumer:
        stock_data = message.value
        print(f"Received data: Stock: {stock_data['stock']}, Price: {stock_data['price']}, Timestamp: {stock_data['timestamp']}")
