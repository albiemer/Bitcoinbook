"""

This is the information the function from external file that implemented into
bitcoinsys.py see the meaning according to the number declared in multi comment

1. clrscr()
    This is actually os.system("clear") its functionalized as clrscr() inspired
    as C language clear screen and located in note.py from external file
2. title()
    It is the title functionalized located from note.py
3. opthead()
    this is an option that functionalized and located in note.py and this is only
    to print option for opt variable input
4. noteonly()
    This is the function to print current bitcoin price in the market and
    it is located from external file named note.py
5. nofoundrecordnote()
    Th/is is the function to print "NO FOUND RECORDS" in search function.
6. getbitcoinprice()
    This is the function that print the current bitcoin price. This function are
    located from external file named bitcoinprice.py
7. foundrecordnote()
    The foundrecordnote() function is use to give a notice that record was found
    This function are located from external file named note.py
8. getbitcoinprice()
    The getbitcoinprice function is the function get real time bitcoin rate
    on the internet

"""

from time import sleep

import sqlite3
from prettytable import PrettyTable, from_db_cursor
from bitcoinprice import getbitcoinprice
from note import noteonly, title, clrscr, nofoundrecordnote, foundrecordnote, opthead, entryinvalid
from forex_python.converter import CurrencyRates
from mypredict import totalpredict, myvisual, dbtocsvproc, update_progress, entryalgo
import threading

x = PrettyTable()
errmain = 0
key = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXzZ7890'
keydataprint = 'aAbBcCdDeEfFgGhHiIjJkKlLmMoOpPqQrRsStTuUvVwWxXzZ1234567890'
 

c = CurrencyRates()
Currency = c.get_rate('USD', 'PHP')  #convert USD to EURO



###########MAIN MODULE############
class classconn:
    #connection for database that use sqlite3
    def mainconn():
        global conn, c
        conn = sqlite3.connect('bitcoindb.db')
        c = conn.cursor()

    def dataprintoptcontrol():
        printlastinput = input("[y/n]PRINT LAST RECORD?")
        if printlastinput == 'y' or printlastinput == 'Y':
            printlastrecord()
        elif printlastinput == 'n' or printlastinput == 'N':
            main()
        elif printlastinput == 'y' or printlastinput == 'Y':
            printlastrecord()
        elif printlastinput in keydataprint:
            printlastrecord()
        else:
            dataprint()
            

    def mycoloptcontrol(mysearch):
        print("[U]pdate [D]elete [L]ast Record [A]ddnew Record [P]RINT STARTED ID")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("To exit and back to main menu type [n] or type [exit]")
        
        toexit = input("SEARCH RECORD? ")
            
        if toexit == 'y' or toexit == 'Y':
            searchrecord()
            del toexit, mysearch

        elif toexit == 'n' or toexit == 'N' or toexit == 'exit' or toexit == 'EXIT':
            try:
                main()
                del toexit, mysearch
            except:
                exit()

        elif toexit == 'u' or toexit == 'U':
            updaterecord(mysearch)
        elif toexit == 'd' or toexit == 'D':
            deleterecord(mysearch)
        elif toexit == 'l' or toexit == 'L':
            printlastrecord()
        elif toexit == 'a' or toexit == 'A':
            entryrecord()
        elif toexit == 'p' or toexit == 'P':
            dataprint()
        else:
            searchrecord(None, toexit)
            print("toexit")
            del mysearch
    
    def updateoptlabel():
        print("[1]BTC RATE\n[2]BTC BALANCE\n[3]DOLLAR COST\n[4]PHP BALANCE\n[5]PROFIT / LOSS\n[6]Volume")


# you can use this as one function but its not necessary
def connclose():
    conn.commit()
    conn.close()

# this is the main block of the system
def main():
    clrscr()    #1
    global mysearch, x
    title()     #2
    # The function printallrecord() are located below next to mycol() function
    printallrecord()
    opthead()   #3
    
    # this is input to choose option from main function
    opt = input("ENTER OPTION: ")
    if opt == '1':
        # the function searchrecord() are located below next from main() function
        searchrecord(None, None)

    elif opt == '2':
        # the function dataprint are located below next from printlastrecord()
        dataprint()

    elif opt == '3':
        # the function entryrecord are located below next from dataprint()
        entryrecord()

    elif opt == '4':
        # the function updaterecord(None) are located below next from insertrecord()
        # the argument in updaterecord(None) should be initialized as None to avoid
        # error parameter sequence
        updaterecord(None)
    elif opt == '5':
        # A dbtocsvproc() function are located in mypredict.py
        # The purpose of dbtocsvproc() function is to export csv file from sqlite3 database 
        dbtocsvproc()
        # myvisual() is a function that show bar graph analyzation for BTC_rate column
        myvisual()
        # After process of dbtocsvproc() and myvisual() its automatically directed to main()
        main()
    elif opt == '6':
        # this is an option to exit when you are at the main() function
        exit()
    elif opt == 'y' or opt == 'Y':
        clrscr()   #1
        main()
        
    # the key are declared at the top
    # the purpose of this key is to be sure that any letter that you input in
    # variable opt from main function couldn't trigger error when memory is too much heavy
    # when you entry a letter that are in key, it could return to main menu or main()
    elif opt in key:
        clrscr()    #
        print("Invalid Key")
        main()
    
    # in case when you input special or unique character it will also work as key
    # to return in main() function
    else:
        main()

############SEARCH RECORD###########                                                                                  #

# This is the function of searchrecord(), it is initialized declared in opt input
# at the top inside main() fuction
def searchrecord(asearch, toexit):
    try:
        clrscr()    #1
        title()     #2
        noteonly()  #4
        
        # The printallrecord are located below next from mycol
        printallrecord()
        
        # this is an input to search record
        if asearch == None and toexit == None:
            mysearch = input("\n[n] to main MENU\nSEARCH RECORD: ")
        elif toexit == None:
            # if asearch not not none then it will
            # Assign asearch to mysearch that comes from parameter
            # searchrecord(asearch, toexit)
            mysearch = asearch
        else:
            # toexit is not None from searchrecord(asearch, toexit) then
            # toexit will assign to mysearch variables
            mysearch = toexit
        global row
        
        # The mainconn function are located at the top inside of class classconn()
        classconn.mainconn()
        
        # This is to execute to find record from the database using sqlite3
        c.execute("select * from BITCOIN_TABLE where ID=?",(mysearch,))
        row = c.fetchone()
        conn.rollback()
        # To close database after execute from searchfunction()
        conn.close()
        
        # if you are at the menu of searchrecord() function and instead
        # of searching, you input 'n' or 'N' rather than input number and exit and,
        # it will bring you back to the main() function
        if mysearch == 'n' or mysearch == 'N':
            # it
            main()
            
            # Need to delete the value of mysearch when going back to main menu
            # of main() function and to decrease memory that carry by the system
            # using variables value
            del mysearch
        
        # This is to continue next process function aside going back to the
        # main() function
        else:
            # The mycol() function are located below next from searchrecord()
            # function
            # The purpose of putting variable mysearch in mycol(parameter) is to
            # bring variable mysearch into mycol() function instead of declaring
            # another mysearch variable inside mycol() function 
            mycol(mysearch)
    
    # When record can't be found from the database then it falls to except as the
    # next process
    except:
        nofoundrecordnote()    #5
        # This printallrecord() function are located below next from mycol() function
        printallrecord()
        
        # After processed not record found the variable searchagain input will
        # appear 
        searchagain = input("\n[n]To MAIN MENU\n[enter] SEARCH RECORD:")
        
        # If record not found from the database you can still exit from
        # searchrecord() function by input 'n' or 'N' and back to the main()
        # function
        if searchagain == 'n' or searchagain == 'n':
            # The main() function are located at the top next from connclose()
            # function
            main()
        
        # When fall from except because record are not found and when not input
        # 'n' or 'N' for going back to main() instead user end are pressing enter
        # it will recursed to searchrecord() function to give you another option
        # to find a record
        else:
            # The functio searchrecord() functon are located at the top next from
            # main() functon
            searchrecord(searchagain, None)
            del toexit

###########SEARCH MODULE END###########


#---------------mycol--------------#

# mycol() function is to print the result processed from other function
# The purpose of mysearch parameter from mycol(parameter) is to declare variable
# to recontinue the value of mysearch from other function into mycol(mysearch)
# function
def mycol(mysearch):
    global x
    clrscr()    #1
    title()     #2
                                     #6
    print("CURRENT BITCOIN PRICE: ", getbitcoinprice())
    foundrecordnote()   #7
    
    # This is from the libarary prettytable to make a design fields and row for
    # the terminal designed system
    x.field_names = ["ID", "BTC_Rate", "BTC_Balance", "DOLLAR_Cost", "PHP_Balance", "Profit_Or_Loss", "PH_Currency", "BTC_Predict"]
    x.add_row([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
    
    # This variable mysearch are reassiged after mysearch from parameter used
    # the mysearch assigned with row[0], row[0] is the data ID of the specific
    #record from the database
    mysearch = row[0]
    
    # This is printing or output with Fields and rows
    print(x)
    x.clear_rows()
    
    # This mycoloptcontrol(mysearch) is located at the top inside of class classconn
    # The mysearch parameter in mycoloptcontrol is to bring variable into
    # mycoloptcontrol(mysearch)
    classconn.mycoloptcontrol(mysearch)

#---------------mycol--------------#

# Printallrecord() function is to display a 15 records that started from 1 as
# A initialized record data report from print all record
def printallrecord():
    # classconn.mainconn is a connection for sqlite3 database bitcoindb.db
    classconn.mainconn()
    # This is the execution to select from BITCOIN_TABLE in sqlite3 database
    c.execute("select * from BITCOIN_TABLE limit 15")

    x = from_db_cursor(c)
    print(x)
    conn.close()

#------------printlastecord-----------#

# This printlastrecord() is to display last record from sqlite3 database
def printlastrecord():
    clrscr()   #1
    # global declaration for variable row
    global row
    # classconn.mainconn is a connection for sqlite3 database bitcoindb.db
    classconn.mainconn()
    # This SQL execution is to select last record and only disply 1 row
    # which is the last record
    c.execute("select * from BITCOIN_TABLE order by ID desc limit 1")
    # assigning c.fetchone to row
    row = c.fetchone()
    # calling mycol(None) function with None or empty parameters
    mycol(None)
    # Closing the sqlite3 database connection 
    connclose()

# dataprint() function is to display selected started number of row to las record
def dataprint():
    clrscr()    #1
    title()     #2
    # classconn.mainconn is a connection for sqlite3 database bitcoindb.db
    classconn.mainconn()
    # in case error in try then it will raise to except
    try:
        # Input id to start selected id to display record
        strtid = input("ENTER START ID: ")
        # This sql command is for selecting record 100 row but started id setoff
        # by strtid
        c.execute("select * from BITCOIN_TABLE LIMIT 100 OFFSET {offid}".format(offid=strtid))
        # assigning cursor c to x 
        x = from_db_cursor(c)
        # displaying x that resulted from the following above processs to display record 
        print(x)
        # classconn.dataprintoptcontrol() are located above inside class classconn    
        classconn.dataprintoptcontrol()
        # Closing the sqlite3 database connection
        connclose()
    # in case theres an error in try it will execute except
    except:
        # The main() function are located at the top next from connclose()
        # function
        main()
    
#--------------dataprint end-------------#

###########ADDNEW RECORD##########

# The entryrecord function is the function that you are able to entry new record
# that calling first from the main() function and searchrecord() function
def entryrecord():
    # declaring global the variable volume
    global volume
    clrscr()    #1
    title()     #2
    noteonly()  #4
    
    # assigning getbitcoinprice to btcrate
    btcrate = getbitcoinprice()
    # Printallrecord() function is to display a 15 records that started from 1 as
    # A initialized record data report from print all record
    printallrecord()
    try:
        # classconn.mainconn is a connection for sqlite3 database bitcoindb.db
        classconn.mainconn()
        # To execute query to select from sqlite3 dbase which is the last record
        # only selected from this query
        c.execute("select * from BITCOIN_TABLE order by ID desc limit 1")
        # assigning c cursor to row
        row = c.fetchone()
        try:
            # getting the value of row[2] which is the BTC_Rate
            btcbalance = row[2]#float(input("\nENTER BTC BALANCE: "))
            dollarcost = row[3]#float(input("ENTER PHP COST: "))
            if row[6] == None:
                currency = Currency
            else:
                currency = Currency
            
        except:
            btcbalance = float(input("\nENTER BTC BALANCE: "))
            dollarcost = btcrate * btcbalance #float(input("ENTER DOLLAR COST: "))
            currency = Currency
        
        
        toinsert = entryalgo(btcrate, btcbalance, currency, dollarcost)
        insertrecord(btcrate, btcbalance, toinsert[2], toinsert[3], toinsert[4], toinsert[1], toinsert[0])
        
    except:
        searchrecord(None, None)

def insertrecord(btcrate, btcbalance, dollarcost, phpbalance, profitorloss, currency, mypredict):
    global conn, c
    
    classconn.mainconn()
    # this is an insert record execute for insert record function
    c.execute("insert into BITCOIN_TABLE(BTC_Rate, BTC_Balance, DOLLAR_Cost, PHP_Balance, Profit_Or_Loss, PH_Currency, BTC_Predict) values (?,?,?,?,?,?,?)", (btcrate, btcbalance, dollarcost, phpbalance, profitorloss, currency, mypredict))
    print("\nINSERTED DATA SUCCESSFULLY")
    input()
    connclose()
    printlastrecord()
    
#------------------------------------------------------------------------

###########UPDATE RECORD###########

def updaterecord(mysearch):
    clrscr()
    title()
    noteonly()
    printallrecord()
    if mysearch == None:
        try:
            idselection = int(input("\n\nENTER ID TO UPDATE: "))
        except:
            main()
    else:
        idselection = mysearch
    clrscr()
    title()
    noteonly(), print("TARGET ID: ", idselection)
    printallrecord()
    classconn.updateoptlabel()
    
    try:
        myupdate = int(input("ENTER OPTION TO UPDATE: "))
        if myupdate == 1:
            btcrateupdate = float(input("ENTE NEW BTC RATE: "))
            classconn.mainconn()
            c.execute("update BITCOIN_TABLE set BTC_Rate = ? where ID = ?", (btcrateupdate, idselection))
            connclose()
            
            printupdaterecord(idselection)

        elif myupdate == 2:
        
            btcbalanceupdate = float(input("ENTER NEW BTC BALANCE: "))
            classconn.mainconn()
            c.execute("update BITCOIN_TABLE set BTC_Balance = ? where ID = ?", (btcbalanceupdate, idselection))
            connclose()

            printupdaterecord(idselection)

        elif myupdate == 3:
            dollarcostupdate = float(input("ENTER NEW DOLLAR COST: "))
            classconn.mainconn()
            c.execute("update BITCOIN_TABLE set DOLLAR_Cost = ? where ID = ?", (dollarcostupdate, idselection))
            connclose()

            printupdaterecord(idselection)
        
        elif myupdate == 4:
            phpbalanceupdate = float(input("ENTER NEW PHP BALANCE: "))
            classconn.mainconn()
            c.execute("update BITCOIN_TABLE set PHP_Balance = ? where ID = ?", (phpbalanceupdate, idselection,))
            connclose()

            printupdaterecord(idselection)

        elif myupdate == 5:
            profitupdate = float(input("ENTER NEW PROFIT: "))
            classconn.mainconn()
            c.execute("update BITCOIN_TABLE set Profit_Or_Loss = ? where ID = ?", (profitupdate, idselection))
            connclose()

            printupdaterecord(idselection)
            
        elif myupdate == 6:
            volumeupdate = float(input("ENTER NEW Volume: "))
            classconn.mainconn()
            c.execute("update BITCOIN_TABLE set Volume = ? where ID = ?", (volumeupdate, idselection))
            connclose()
            
            printupdaterecord(idselection)

        else:
            searchrecord()
            del idselection, mysearch, myupdate, btcrateupdate, btcbalanceupdate, \
                dollarcostupdate, phpbalanceupdate, profitupdate
    except:
        clrscr()
        title()
        entryinvalid()
        printallrecord()
        print("\nPRESS ENTER TO RECONTINUE FOR THE VALID ENTRY")
        input()
        updaterecord(None)
        del idselection, mysearch, myupdate, btcrateupdate, btcbalanceupdate, \
            dollarcostupdate, phpbalanceupdate, profitupdate

def printupdaterecord(x):
    mysearch = x
    global row
    classconn.mainconn()
    c.execute("select * from BITCOIN_TABLE where ID=?",(mysearch,))
    row = c.fetchone()
    conn.rollback()
    conn.close()
    #updaterecord()
    mycol(mysearch)
    del x

##########UPDATE RECORD END########

###########DELETE RECORD###########

def deleterecord(mysearch):
    clrscr()
    title()
    noteonly()
    printallrecord()
    if mysearch == None:
        todelete = int(input("\n\nENTER ID TO DELETE: "))
    else:
        todelete = mysearch
    classconn.mainconn()    

    c.execute("delete from BITCOIN_TABLE where ID = ?", (todelete,))

    connclose()

    print("\nDELETED SUCCESSFUL, PRESS ENTER TO REFRESH THE RECORD")
    input()
    searchrecord(None, None)

if __name__=="__main__":
    clrscr()
    update_progress(), main()
    
