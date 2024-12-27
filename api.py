
import requests
import time
import numpy as np
import matplotlib.pyplot as plt
def calculate_statistics(real_time_data):
    buy_prices = [details['buy'] for details in real_time_data.values()]
    mean_price = np.mean(buy_prices)
    median_price = np.median(buy_prices)
    std_dev_price = np.std(buy_prices)
    print(f"Mean Buy Price: {mean_price}")
    print(f"Median Buy Price: {median_price}")
    print(f"Standard Deviation of Buy Prices: {std_dev_price}")
prices_over_time = {}
def track_price_changes(real_time_data, prices_over_time):
    for currency, details in real_time_data.items():
        if currency not in prices_over_time:
            prices_over_time[currency] = []
        prices_over_time[currency].append(details['buy'])
    history_size = 10
    for currency in prices_over_time:
        prices_over_time[currency] = prices_over_time[currency][-history_size:]
    for currency, prices in prices_over_time.items():
        price_changes_str = " -> ".join([f"{price:,.2f}" for price in prices])
        print(f"{currency}: {price_changes_str}")
def poll_api(api_url):
    prices_over_time = {} 
    while True:
        response = requests.get(api_url)
        if response.status_code == 200:
            real_time_data = response.json()
            print("------------------------------------------------------")
            print('New data received:', real_time_data)
            print("------------------------------------------------------")
            calculate_statistics(real_time_data)
            track_price_changes(real_time_data, prices_over_time)
            time.sleep(10)  
        else:
            print('Error fetching data:', response.status_code)

real_time_api_url = 'https://blockchain.info/ticker'

poll_api(real_time_api_url)
