import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

from strategy import moving_average_strategy
from predictor import predict_price, forecast_prices
from indicators import calculate_rsi, calculate_macd
from sentiment import analyze_news

st.set_page_config(page_title="AI Trading Dashboard", layout="wide")

st.title("🤖 AI Stock Trading Dashboard")

stock = st.sidebar.text_input("Stock Symbol","AAPL")
investment = st.sidebar.number_input("Investment Amount ($)",1000)

data = yf.download(stock, period="6mo")

if data.empty:

    st.error("No stock data found")

else:

    st.subheader("📊 Candlestick Chart")

    fig = go.Figure(data=[go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close']
    )])

    st.plotly_chart(fig, use_container_width=True)

    signal = moving_average_strategy(data)

    st.subheader("🤖 Trading Signal")
    st.write(signal)

    current_price = data['Close'].iloc[-1]

    predicted_price = predict_price(current_price)

    st.subheader("🔮 AI Predicted Price")
    st.write(predicted_price)

    shares = investment/current_price
    future_value = shares*predicted_price
    profit = future_value - investment

    st.subheader("💰 Portfolio Simulation")

    col1,col2,col3 = st.columns(3)

    col1.metric("Current Price",round(current_price,2))
    col2.metric("Predicted Price",round(predicted_price,2))
    col3.metric("Estimated Profit",round(profit,2))

    data['RSI'] = calculate_rsi(data)

    st.subheader("📈 RSI Indicator")

    st.line_chart(data['RSI'])

    macd, signal_line = calculate_macd(data)

    st.subheader("📉 MACD Indicator")

    macd_df = pd.DataFrame({
        "MACD": macd,
        "Signal": signal_line
    })

    st.line_chart(macd_df)

    st.subheader("📰 AI Market Sentiment")

    sentiment = analyze_news()

    st.write(sentiment)

    st.subheader("🔮 AI Price Forecast")

    forecast = forecast_prices(data)

    forecast_df = pd.DataFrame({
        "Future Price": forecast
    })

    st.line_chart(forecast_df)
