from textblob import TextBlob

def analyze_news():

    news = [
        "Company profits increased this quarter",
        "Investors are optimistic about the market",
        "Stock demand is rising rapidly"
    ]

    score = 0

    for headline in news:

        sentiment = TextBlob(headline).sentiment.polarity
        score += sentiment

    if score > 0:
        return "Positive Market Sentiment 📈"
    else:
        return "Negative Market Sentiment 📉"
