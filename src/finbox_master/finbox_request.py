import requests
import io
import json
import csv
from math import floor

class finboxRequest:
    
    def __init__(self):
        self.url = "https://api.finbox.io/beta"
        self.headers = {
        'authorization': "Bearer 509e960d5d374b8958f00bd5e977d13f001925fe",
        'accept': "application/json",
        'content-type': "application/json"
        }

    def getUrl(self, extension):
        return (self.url + extension)


    
    data = {
    "data": {
        "finbox_id": {
        
    }
    }
    }






def floored_percentage(val, digits):
    val *= 10 ** (digits + 2)
    return '{1:.{0}f}%'.format(digits, floor(val) / 10 ** digits)

fRequest = finboxRequest()
ticker = input("Enter a stock ticker: ")

response = requests.get(fRequest.getUrl("/fairvalues/"+ticker),headers=fRequest.headers)

ticker_parsed = json.loads(response.text)

fvHigh = ticker_parsed.get('data',{}).get('price',{}).get('high')
fvMid = ticker_parsed.get('data',{}).get('price',{}).get('mid')
fvLow = ticker_parsed.get('data',{}).get('price',{}).get('low')
upHigh = floored_percentage(ticker_parsed.get('data',{}).get('upside',{}).get('high'),1)
upMid = floored_percentage(ticker_parsed.get('data',{}).get('upside',{}).get('mid'),1)
upLow = floored_percentage(ticker_parsed.get('data',{}).get('upside',{}).get('low'),1)

print ('Ticker: ' + ticker_parsed.get('data',{}).get('ticker'))
print ('Finbox Fair Value Range: ' + "\n" + "High Fair Value : %.2f" % fvHigh
+ "\n" + "Mid Fair Value : %.2f" % fvMid
+ "\n" + "Low Fair Value : %.2f" % fvLow)
print ('Finbox Upside: ' + "\n" + "High Upside : " + upHigh
+ "\n" + "Mid Upside : " + upMid
+ "\n" + "Low Upside : " + upLow)
print ('Number of Estimates: ' + str(ticker_parsed.get('data',{}).get('estimates')))
print ('Confidence Level: ' + ticker_parsed.get('data',{}).get('confidence'))