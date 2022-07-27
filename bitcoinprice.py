
import requests, json

def getbitcoinprice():
    
    URL = 'https://www.bitstamp.net/api/ticker/'
    
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")
        return None