import json
from oandapyV20 import API    # the client
import oandapyV20.endpoints.pricing as pricing
import oandapyV20.definitions.instruments as instruments

access_token = "c3c92f7311f6dfe61e38abe308649e64-1d862e8e1e2451e1fa965122fc1b00a9"
accountID = "101-004-14379136-001"
client = API(access_token=access_token)

params = {"instruments": "USD_RUB"}
r = pricing.PricingInfo(accountID, params=params)
rv = client.request(r)
print(rv)