# import pandas as pd
# import yfinance as yf
# import json
# # Ticker allows to get market and meta data for a security
# apple = yf.Ticker("AAPL")

# with open('apple.json') as json_file:
#     apple_info = json.load(json_file)
#     # Print type of data variable
#     # print(type(apple_info))

# print(apple_info['country'])
# # print(apple_info['city'])
# apple_share_price_history = apple.history(period="max")
# # print(apple_share_price_history)
# # print(apple_share_price_history.head())

# # print(apple_share_price_history.reset_index(inplace=True))
# # print(apple_share_price_history.plot(x="Date",y="Open"))
# print(apple.dividends)
# print(apple.dividends.plot())

import pandas as pd
import yfinance as yf

# Data for microsoft

msft = yf.Ticker("MSFT")
# msft_data = msft.history(period="max")
msft_data = msft.history(period="ytd")
print(msft_data)

# display first 5 rows ofthe data
print(msft_data.head())

print(msft.info)
print(type(msft.info))
print(msft.info['sector'])