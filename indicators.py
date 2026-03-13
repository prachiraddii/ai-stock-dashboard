import pandas as pd

def calculate_rsi(data, window=14):

    delta = data['Close'].diff()

    gain = (delta.where(delta > 0, 0)).rolling(window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window).mean()

    rs = gain / loss

    rsi = 100 - (100/(1+rs))

    return rsi


def calculate_macd(data):

    short_ema = data['Close'].ewm(span=12).mean()
    long_ema = data['Close'].ewm(span=26).mean()

    macd = short_ema - long_ema
    signal = macd.ewm(span=9).mean()

    return macd, signal
