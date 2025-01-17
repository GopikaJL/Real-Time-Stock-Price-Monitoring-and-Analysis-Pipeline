
# Real-Time Stock Price Monitoring and Analysis Pipeline using Docker 📈📊

This project demonstrates a real-time stock price monitoring pipeline built using Kafka, Python, and Docker. The system simulates stock price data generation, processes the data in real time, and provides insights into stock price movements. Docker is used to streamline deployment and ensure consistency across environments.

---

## Project Overview 🌟

The pipeline comprises the following components:

1. **Stock Data Producer**: Simulates real-time stock price data and sends it to a Kafka topic.
2. **Kafka Consumer**: Processes incoming stock data, extracts meaningful information, and displays it in real time.
3. **Real-Time Data Analysis**: Fetches data from APIs, calculates statistical insights, and tracks trends over time.
4. **Dockerized Deployment**: All components are containerized using Docker, simplifying setup and ensuring consistency.

---

## Components and Scripts 🛠️

### 1. `advanced_producer2.py`
- **Purpose**: Generates real-time stock price data for multiple stocks and publishes the data to Kafka.
- **Features**:
  - Simulates stock price data for companies like Apple, Microsoft, and Tesla.
  - Sends data to a Kafka topic named `activity_topic`.
  - Logs generated stock price data for tracking.
    ![image](https://github.com/user-attachments/assets/290ab852-6648-4c74-892d-bde406c00ed7)


### 2. `advanced_consumer2.py`
- **Purpose**: Consumes real-time stock price data from Kafka, processes it, and displays key metrics.
- **Features**:
  - Reads stock price data from `activity_topic`.
  - Logs details like stock name, price, and timestamp for analysis.
![image](https://github.com/user-attachments/assets/1d68195a-13f2-48ab-ad19-88a1e8a4bf8f)



### 3. `realtime.py`
- **Purpose**: Fetches external API data, performs statistical calculations, and visualizes trends.
- **Features**:
  - Retrieves and analyzes stock price data from APIs such as `https://blockchain.info/ticker`.
  - Computes mean, median, and standard deviation of prices.
  - Tracks price trends and visualizes data over time.

![1 7](https://github.com/user-attachments/assets/9280641b-78c1-421f-b9ad-39bc863dc7ce)


## Dockerized Setup 🐳

Docker is used to containerize all components of the project, ensuring seamless deployment and operation. A `docker-compose.yml` file is included to orchestrate services.


### Benefits of Using Docker
- **Environment Consistency**: All components run in isolated environments, avoiding dependency conflicts.
- **Ease of Deployment**: Simplifies starting and stopping services with a single command.
- **Scalability**: Facilitates horizontal scaling of services like Kafka consumers.

---

## Getting Started 🚀

### Prerequisites 📋
1. **Docker**: Install Docker and Docker Compose on your system.
2. **Python**: Version 3.6 or above for local testing.
3. **Python Libraries**: If running locally, install required dependencies:
   ```bash
   pip install kafka-python pandas numpy matplotlib requests
   ```

---

### Running the Application with Docker ⚡

#### 1. Build and Start the Containers
Run the following command to build the Docker images and start the services:
```bash
docker-compose up --build
```

This will:
- Start a Kafka broker and Zookeeper.
- Launch the producer and consumer scripts as containers.

#### 2. Monitor the Logs
You can monitor the logs of individual services by running:
```bash
docker logs <container_name>
```

#### 3. Stop the Containers
To stop and clean up the containers, run:
```bash
docker-compose down
```

---

![docker](https://github.com/user-attachments/assets/8b2f8b1b-64a6-417e-a52d-ca885adc92f3)



## Future Enhancements 🛠️
- Add advanced analytics such as moving averages, volatility measures, and correlation analysis.
- Implement error handling and logging mechanisms for production-grade robustness.
