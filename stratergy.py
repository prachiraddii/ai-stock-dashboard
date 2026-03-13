import pandas as pd

def moving_average_strategy(data):

    data['SMA20'] = data['Close'].rolling(20).mean()
    data['SMA50'] = data['Close'].rolling(50).mean()

    if data['SMA20'].iloc[-1] > data['SMA50'].iloc[-1]:
        return "BUY 📈"
    else:
        return "SELL 📉"
