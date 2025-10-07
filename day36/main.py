import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "458634f3adbe464480632c07e64ef27d"

STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
STOCK_API_KEY = "JKA75K1W71LGFOXJ"
STOCK_PARAMETER = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

stock = requests.get(STOCK_ENDPOINT, params = STOCK_PARAMETER)
stock_data = stock.json()[["Time Series (Daily)"]]
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


diff_percent = round(difference/float(yesterday_closing_price)) * 100

if abs(diff_percent) > 5:
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()["articles"]
    three_articles = news_data[:3]

    formatted_articles = [f"{STOCK}: {up_down}{difference}%\nHeadline: {news_data['title']}. \nBrief: {news_data['description']}" for news_data in three_articles]
