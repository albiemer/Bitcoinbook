
import os
import sqlite3
from prettytable import from_db_cursor
import pandas as pd
import matplotlib.pyplot as plt
#import time

"""def mainconn():
    global conn, c
    conn = sqlite3.connect('bitcoindb.db')
    c = conn.cursor()"""

class sqlquery:
    def __init__(self, toupdate, idselection):
        self.toupdate = toupdate
        self.idselection = idselection
    
    def btcrateupdate(self):
        conn = sqlite3.connect('bitcoindb.db')
        c = conn.cursor()
        c.execute("update BITCOIN_TABLE set BTC_Rate = ? where ID = ?", (self.toupdate, self.idselection))
        conn.commit()
        conn.close()

    def btcbalanceupdate(self):
        conn = sqlite3.connect('bitcoindb.db')
        c = conn.cursor()
        c.execute("update BITCOIN_TABLE set BTC_Balance = ? where ID = ?", (self.toupdate, self.idselection))
        conn.commit()
        conn.close()

    def dollarcostupdate(self):
        conn = sqlite3.connect('bitcoindb.db')
        c = conn.cursor()
        c.execute("update BITCOIN_TABLE set DOLLAR_Cost = ? where ID = ?", (self.toupdate, self.idselection))
        conn.commit()
        conn.close()

    def phpbalanceupdate(self):
        conn = sqlite3.connect('bitcoindb.db')
        c = conn.cursor()
        c.execute("update BITCOIN_TABLE set PHP_Balance = ? where ID = ?", (self.toupdate, self.idselection,))
        conn.commit()
        conn.close()

    def profitupdate(self):
        conn = sqlite3.connect('bitcoindb.db')
        c = conn.cursor()
        c.execute("update BITCOIN_TABLE set Profit_Or_Loss = ? where ID = ?", (self.toupdate, self.idselection))
        conn.commit()
        conn.close()

    def phcurrencyupdate(self):
        conn = sqlite3.connect('bitcoindb.db')
        c = conn.cursor()
        c.execute("update BITCOIN_TABLE set PH_Currency = ? where ID = ?", (self.toupdate, self.idselection))
        conn.commit()
        conn.close()



def mypredictdata():
    conn = sqlite3.connect('bitcoindb.db')
    c = conn.cursor()
    c.execute("select sum(BTC_RAte) from BITCOIN_TABLE")
    row = c.fetchone()
    return row[0]
    
def todevide():
    conn = sqlite3.connect('bitcoindb.db')
    c = conn.cursor()
    c.execute("select count(ID) from BITCOIN_TABLE order by ID desc limit 1")
    row = c.fetchone()
    return row[0]
    
def totalpredict():
    #btcrate = getbitcoinprice()
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

def csvwipe():
    os.system("rm BITCOIN_TABLE.csv")

"""def loadbar(progress):
    print("\r {0}>".format('>>>'*(progress//10), progress), end='')"""

"""def update_progress():
    print("\n\n\n\n\n\nLOAD:"), loadbar(100),time.sleep(10)"""
    
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
    conn = sqlite3.connect('bitcoindb.db')
    c = conn.cursor()
    # This is to execute to find record from the database using sqlite3
    c.execute("select * from BITCOIN_TABLE where ID=?",(mysearch,))
    row = c.fetchone()
    conn.rollback()
    # To close database after execute from searchfunction()
    conn.close()
    return row
#print(sqlquerysearch(2)[0])

def sqlqueryprintallrecord():
    # mainconn() is a connection for sqlite3 database bitcoindb.db
    conn = sqlite3.connect('bitcoindb.db')
    c = conn.cursor()
    # This is the execution to select from BITCOIN_TABLE in sqlite3 database
    c.execute("select * from BITCOIN_TABLE limit 15")

    x = from_db_cursor(c)
    conn.close()
    print(x)

def sqlqueryprintlastrecord():
    # classconn.mainconn is a connection for sqlite3 database bitcoindb.db
    conn = sqlite3.connect('bitcoindb.db')
    c = conn.cursor()
    # This SQL execution is to select last record and only disply 1 row
    # which is the last record
    c.execute("select * from BITCOIN_TABLE order by ID desc limit 1")
    # assigning c.fetchone to row
    row = c.fetchone()
    # Closing the sqlite3 database connection 
    conn.commit()
    conn.close()
    return row

#print(sqlqueryprintlastrecord())

def sqlquerydataprint(strtid):
    # classconn.mainconn is a connection for sqlite3 database bitcoindb.db
    conn = sqlite3.connect('bitcoindb.db')
    c = conn.cursor()
    # This sql command is for selecting record 100 row but started id setoff
    # by strtid
    c.execute("select * from BITCOIN_TABLE LIMIT 100 OFFSET {offid}".format(offid=strtid))
    # assigning cursor c to x 
    x = from_db_cursor(c)
    # displaying x that resulted from the following above processs to display record 
    conn.commit()
    conn.close()
    return x

#print(sqlquerydataprint(2))

def sqlqueryinsertrecord(btcrate, btcbalance, dollarcost, phpbalance, \
                         profitorloss, currency, mypredict):
    conn = sqlite3.connect('bitcoindb.db')
    c = conn.cursor()
    # this is an insert record execute for insert record function
    c.execute("insert into BITCOIN_TABLE(BTC_Rate, BTC_Balance, DOLLAR_Cost, PHP_Balance, Profit_Or_Loss, PH_Currency, BTC_Predict) values (?,?,?,?,?,?,?)", (btcrate, btcbalance, dollarcost, phpbalance, profitorloss, currency, mypredict))
    print("\nINSERTED DATA SUCCESSFULLY")
    input()
    conn.commit()
    conn.close()

def sqlqueryprintupdaterecord(mysearch):
    conn = sqlite3.connect('bitcoindb.db')
    c = conn.cursor()
    c.execute("select * from BITCOIN_TABLE where ID=?",(mysearch,))
    row = c.fetchone()
    conn.rollback()
    conn.close()
    return row

#print(sqlqueryprintupdaterecord(21)[0])

def sqlquerydeleterecord(todelete):
    conn = sqlite3.connect('bitcoindb.db')
    c = conn.cursor()
    c.execute("delete from BITCOIN_TABLE where ID = ?", (todelete,))
    conn.commit()
    conn.close()
    print("\nDELETED SUCCESSFUL, PRESS ENTER TO REFRESH THE RECORD")
    input()

def sqlqueryuserconfirm(uname, pword):
    conn = sqlite3.connect('bitcoindb.db')
    c = conn.cursor()
    c.execute("select * from USER where Username=? and Password=?",(uname, pword,))
    row = c.fetchone()
    conn.rollback()
    conn.close()
    return row

def sqlquerydeleteallrecords():
    conn = sqlite3.connect('bitcoindb.db')
    c = conn.cursor()
    c.execute("delete from BITCOIN_TABLE")
    conn.commit()
    conn.close()

#we = sqlqueryuserconfirm('albiemer', 'albi3mer')
#print(we[1], we[2])

#sqlquerydeleteallrecords()
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