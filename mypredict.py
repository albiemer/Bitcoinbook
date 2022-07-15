
import sqlite3
from bitcoinprice import getbitcoinprice

def mainconn():
    global conn, c
    conn = sqlite3.connect('bitcoindb.db')
    c = conn.cursor()
    

def mypredictdata():
    mainconn()
    c.execute("select sum(BTC_RAte) from BITCOIN_TABLE")
    row = c.fetchone()
    return row[0]
    
def todevide():
    mainconn()
    c.execute("select ID from BITCOIN_TABLE order by ID desc limit 1")
    row = c.fetchone()
    return row[0]
    
def totalpredict():
    btcrate = getbitcoinprice()
    try:
        result = mypredictdata() / todevide()
        result = round(result, 2)
        return result
    except:
        result = 0
        return result

#print(totalpredict())