import requests
import io
import json


class finboxRequest:

    def __init__(self):
        self.url = "https://api.finbox.io/beta"
        self.headers = {
            'authorization': "Bearer 509e960d5d374b8958f00bd5e977d13f001925fe",
            'accept': "application/json",
            'content-type': "application/json"
        }

        self.data = json.dumps({
            "data": {
                "profile": {
                "symbol": "AAPL.ticker",
                "name": "AAPL.company_name",
                "description": "AAPL.description",
                "historicals": {
                    "revenue": "AAPL.total_revenue[FY-9:FY]",
                    "ebit": "AAPL.adjusted_ebit[FY-9:FY]",
                    "assets": "AAPL.total_assets[FY-9:FY]"
                },
                "market": {
                    "year_high": "AAPL.year_range_high",
                    "year_low": "AAPL.year_range_low",
                    "beta": "AAPL.beta",
                    "price": "AAPL.stock_price"
                }
                }}
            })

    def getUrl(self, extension=None):
        return (self.url + extension)


fRequest = finboxRequest()

response = requests.post(fRequest.getUrl('/data/batch'),
                         data=fRequest.data, headers=fRequest.headers)

print(response.text)
