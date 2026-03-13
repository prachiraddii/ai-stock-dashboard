import random

def predict_price(current_price):

    change = random.uniform(-2, 2)

    predicted = current_price + change

    return round(predicted,2)