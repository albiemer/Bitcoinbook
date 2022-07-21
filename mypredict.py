
import os
import sqlite3
from bitcoinprice import getbitcoinprice
from prettytable import PrettyTable, from_db_cursor
import pandas as pd
import matplotlib.pyplot as plt
import time

def mainconn():
    global conn, c
    conn = sqlite3.connect('bitcoindb.db')
    c = conn.cursor()

def connclose():
    conn.commit()
    conn.close()

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
    # This command is only applicable for linux with installed sqlite3
    # the sqlite3 are actual installed on the linux system as a terminal application
    # aside from sqlite3 installed in pip3
    os.system("sqlite3 -header -csv bitcoindb.db \"select * from BITCOIN_TABLE;\" > BITCOIN_TABLE.csv")

def loadbar(progress):
    print("\r {0}>".format('>>>'*(progress//10), progress), end='')

def update_progress():
    print("\n\n\n\n\n\nLOAD:"), loadbar(10),time.sleep(1),loadbar(20),time.sleep(1),loadbar(30)
    time.sleep(1),loadbar(40), time.sleep(1),loadbar(50), time.sleep(1)
    loadbar(60),time.sleep(1),loadbar(70), time.sleep(1),loadbar(80)
    time.sleep(1),loadbar(90), time.sleep(1),loadbar(100)

def entryalgo(btcrate, btcbalance, currency, dollarcost):
    dollarbalance = btcrate * btcbalance
    phpbalance = float(dollarbalance) * currency
    profitorloss = float(phpbalance) - (float(dollarcost) * currency)
    #phpbalance = int(phpbalance)
        
    mypredict = round(totalpredict(), 2)
    currency = round(currency, 2)
    dollarcost = round(dollarcost, 2)
    phpbalance = round(phpbalance, 2)
    profitorloss = round(profitorloss, 2)
    
    return mypredict, currency, dollarcost, phpbalance, profitorloss

def sqlquerysearch(mysearch):
    # mainconn() is a connection for sqlite3 database bitcoindb.db
    mainconn()
    # This is to execute to find record from the database using sqlite3
    c.execute("select * from BITCOIN_TABLE where ID=?",(mysearch,))
    row = c.fetchone()
    conn.rollback()
    # To close database after execute from searchfunction()
    conn.close()
    return row

def sqlqueryprintallrecord():
    # mainconn() is a connection for sqlite3 database bitcoindb.db
    mainconn()
    # This is the execution to select from BITCOIN_TABLE in sqlite3 database
    c.execute("select * from BITCOIN_TABLE limit 15")

    x = from_db_cursor(c)
    conn.close()
    return x

def sqlqueryprintlastrecord():
    # classconn.mainconn is a connection for sqlite3 database bitcoindb.db
    mainconn()
    # This SQL execution is to select last record and only disply 1 row
    # which is the last record
    c.execute("select * from BITCOIN_TABLE order by ID desc limit 1")
    # assigning c.fetchone to row
    row = c.fetchone()
    # Closing the sqlite3 database connection 
    connclose()
    return row
    

def sqlquerydataprint(strtid):
    # classconn.mainconn is a connection for sqlite3 database bitcoindb.db
        mainconn()
        # This sql command is for selecting record 100 row but started id setoff
        # by strtid
        c.execute("select * from BITCOIN_TABLE LIMIT 100 OFFSET {offid}".format(offid=strtid))
        # assigning cursor c to x 
        x = from_db_cursor(c)
        # displaying x that resulted from the following above processs to display record 
        connclose()
        return x

def sqlqueryinsertrecord(btcrate, btcbalance, dollarcost, phpbalance, \
                         profitorloss, currency, mypredict):
    mainconn()
    # this is an insert record execute for insert record function
    c.execute("insert into BITCOIN_TABLE(BTC_Rate, BTC_Balance, DOLLAR_Cost, PHP_Balance, Profit_Or_Loss, PH_Currency, BTC_Predict) values (?,?,?,?,?,?,?)", (btcrate, btcbalance, dollarcost, phpbalance, profitorloss, currency, mypredict))
    print("\nINSERTED DATA SUCCESSFULLY")
    input()
    connclose()

def sqlquerybtcrateupdate(btcrateupdate, idselection):
    mainconn()
    c.execute("update BITCOIN_TABLE set BTC_Rate = ? where ID = ?", (btcrateupdate, idselection))
    connclose()

def sqlquerybtcbalanceupdate(btcbalanceupdate, idselection):
    mainconn()
    c.execute("update BITCOIN_TABLE set BTC_Balance = ? where ID = ?", (btcbalanceupdate, idselection))
    connclose()

def sqlquerydollarcostupdate(dollarcostupdate, idselection):
    mainconn()
    c.execute("update BITCOIN_TABLE set DOLLAR_Cost = ? where ID = ?", (dollarcostupdate, idselection))
    connclose()

def sqlqueryphpbalanceupdate(phpbalanceupdate, idselection):
    mainconn()
    c.execute("update BITCOIN_TABLE set PHP_Balance = ? where ID = ?", (phpbalanceupdate, idselection,))
    connclose()

def sqlqueryprofitupdate(profitupdate, idselection):
    mainconn()
    c.execute("update BITCOIN_TABLE set Profit_Or_Loss = ? where ID = ?", (profitupdate, idselection))
    connclose()
    
def sqlqueryphcurrencyupdate(phcurrencyupdate, idselection):
    mainconn()
    c.execute("update BITCOIN_TABLE set PH_Currency = ? where ID = ?", (phcurrencyupdate, idselection))
    connclose()

def sqlqueryprintupdaterecord(mysearch):
    mainconn()
    c.execute("select * from BITCOIN_TABLE where ID=?",(mysearch,))
    row = c.fetchone()
    conn.rollback()
    conn.close()
    return row

def sqlquerydeleterecord(todelete):
    mainconn()    
    c.execute("delete from BITCOIN_TABLE where ID = ?", (todelete,))
    connclose()
    print("\nDELETED SUCCESSFUL, PRESS ENTER TO REFRESH THE RECORD")
    input()

#print(sqlqueryprintupdaterecord(2))

#print(sqlquerybtcrateupdate(1,5))
#print(sqlqueryinsertrecord(5,5,5,5,5,5,5))

#print(sqlquerydataprint())
#print(sqlqueryprintlastrecord())
#print(sqlqueryprintallrecord())
#print(sqlquerysearch())
#t = entryalgo(10,10,10,10)
#print(t[1])

#update_progress()
#dbtocsvproc()
#myvisual()
#print(totalpredict())