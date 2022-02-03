import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_api_key = "<your api key>"
news_api_key = "<your api key>"


stock_url = 'https://www.alphavantage.co/query'
news_parameter = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "outputsize":"compact",
    "apikey":stock_api_key,

}
stock_response = requests.get(url=stock_url, params=news_parameter)
stock_data = stock_response.json()['Time Series (Daily)']
data_list = [j for (i,j) in stock_data.items()]

price_yesterday = float(data_list[0]['4. close'])
price_day_before_yesterday = float(data_list[1]['4. close'])

price_difference = abs(price_yesterday - price_day_before_yesterday)
percentage_difference = (price_difference/price_yesterday) * 100

if percentage_difference > 5:
    news_url = 'https://newsapi.org/v2/everything'
    news_parameter = {
        "qInTitle": COMPANY_NAME,
        "apikey": news_api_key,
    }
    news_response = requests.get(url=news_url, params=news_parameter)
    news_data = news_response.json()['articles']
    for i in range(3):
        news_title = news_data[i]['title']
        news_description = news_data[i]['description']
        print(news_title)
        print(news_description)

