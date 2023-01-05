import requests
import os
from twilio.rest import Client

#######TESLA INFO###########
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "SCDKQAPPYS5WZRXA"

#####STOCK PARAMETERS#########
#TODO 1
function = "TIME_SERIES_DAILY_ADJUSTED"
outputsize = "compact"
data_type = "json"
parameters = {"function": function,
              "symbol": STOCK_NAME,
              "outputsize": "compact",
              "datatype": data_type,
              "apikey": STOCK_API_KEY}


response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
#print(f"Data is {data}")
data = [value for (key, value) in data.items()]

# yesterdays_closing_price = float(data[3]['4. close'])
# db4_closing_price = float(data[4]['4. close'])

yesterdays_closing_price = float(data[1]['2022-12-20']['4. close'])
db4_closing_price = float(data[1]['2022-12-19']['4. close'])
##Todo 3
difference = abs(yesterdays_closing_price - db4_closing_price)

if yesterdays_closing_price - db4_closing_price < 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage_difference = round(difference / ((yesterdays_closing_price + db4_closing_price) / 2) * 100)
print(f"Percentage difference is {percentage_difference}%")

# print(new_data)
# yesterdays_price = {key['2022-12-16']:value for (key, value) in data.items()}
# print(f"Yesterdays price is {yesterdays_price}")

##########NEW INFO#############
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
q = "Tesla"
from_date = "2022-12-19"
to_date = "2022-12-19"
sortBy = "popularity"
sources = "CNN"
apiKey = "61655960f1e543a19c779dc8d18b0c83"
news_parameters = {"q": q, "from": from_date, "to": to_date, "sortBy": sortBy, "sources": sources, "apikey": apiKey}
news_update = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_data = news_update.json()['articles'][0:3] #TODO 7

# news_data = [value for (key, value) in news_data.items()]
#print(news_data)
news_update = [f"{STOCK_NAME}{up_down}{percentage_difference}% Headline: {item['title']}\nBrief: {item['description']}\nurl: {item['url']}" for item in news_data] #TODo 8
first_headline = news_update[0]
second_headline = news_update[1]
third_headline = news_update[2]

#############################TWILIO INFORMATION##############
# Download the helper library from https://www.twilio.com/docs/python/install
# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = "AC2726e2f68f7da81066f09da7822c4e29"
auth_token = "28844ce3b1f10921ecb0a87fe2fff46c"
# os.environ[""]
client = Client(account_sid, auth_token)
#############

if percentage_difference > 5:
    # print(f"This is the percentage difference, {percentage_difference}")
    for articles in news_update:
        message = client.messages.create(
            body=f"{articles}",
            from_="+13854063614",
            to="+15013094072"

        )

else:
    message = client.messages.create(
        body=f"TSLA 🔻{percentage_difference}%\n {first_headline}\n {second_headline}",
        from_="+13854063614",
        to="+15013094072")
    print(message.sid)

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.
# Optional: Format the SMS message like this:
"""

TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
