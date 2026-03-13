import random
import pandas as pd

def predict_price(current_price):

    change = random.uniform(-2,2)
    predicted = current_price + change

    return round(predicted,2)


def forecast_prices(data):

    last_price = data['Close'].iloc[-1]

    future_prices = []

    for i in range(10):

        change = random.uniform(-3,3)
        last_price = last_price + change

        future_prices.append(last_price)

    return future_prices
