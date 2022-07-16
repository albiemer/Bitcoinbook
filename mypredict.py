
import os
import sqlite3
from bitcoinprice import getbitcoinprice
import pandas as pd
import matplotlib.pyplot as plt

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
    c.execute("select count(ID) from BITCOIN_TABLE order by ID desc limit 1")
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

def myvisual():
    # reading the database
    data = pd.read_csv("BITCOIN_TABLE.csv")
  
    # hostogram of total_bills
    plt.hist(data['BTC_Rate'])
  
    plt.title("Myprediction Analysis")
  
    # Adding the legends
    plt.show()
    
def dbtocsvproc():
    mainconn()
    # This is only applicable for linux with installed sqlite3
    os.system("sqlite3 -header -csv bitcoindb.db \"select * from BITCOIN_TABLE;\" > BITCOIN_TABLE.csv")
    
dbtocsvproc()
#myvisual()
#print(totalpredict())