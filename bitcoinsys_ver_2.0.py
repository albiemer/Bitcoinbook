
from forex_python.converter import CurrencyRates
from prettytable import PrettyTable
from bitcoinprice import getbitcoinprice
from note import title, clrscr, opthead, nofoundrecordnote, foundrecordnote, \
     noteonly, entryinvalid
from mypredict import sqlqueryprintallrecord, sqlquerysearch, \
     sqlqueryprintupdaterecord, sqlquery, sqlquerydataprint, \
     sqlqueryprintlastrecord, entryalgo, sqlqueryinsertrecord, dbtocsvproc, \
     myvisual, sqlquerydeleteallrecords, sqlqueryuserconfirm, csvwipe, \
     sqlquerydeleterecord
import getpass

x = PrettyTable()
key = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXzZ7890'
keydataprint = 'aAbBcCdDeEfFgGhHiIjJkKlLmMoOpPqQrRsStTuUvVwWxXzZ1234567890'

c = CurrencyRates()
Currency = c.get_rate('USD', 'PHP')  #convert USD to PHP peso

def printallrecord():
    sqlqueryprintallrecord()
    
def updateoptlabel():
    print("[1]BTC RATE\n[2]BTC BALANCE\n[3]DOLLAR COST\n[4]PHP BALANCE\n[5]PROFIT / LOSS\n[6]PHP CURRENCY")

def mycoloptcontrol(mysearch):
    print("[U]pdate [D]elete [L]ast Record [A]ddnew Record [P]RINT STARTED ID")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("To exit and back to main menu type [n] or type [exit]")
        
    toexit = input("SEARCH RECORD? ")
            
    if toexit == 'y' or toexit == 'Y':
        searchrecord(None, None)
        del toexit, mysearch

    elif toexit == 'n' or toexit == 'N' or toexit == 'exit' or toexit == 'EXIT':
        main()
        del toexit, mysearch
    elif toexit == 'u' or toexit == 'U':
        updaterecord(mysearch, None)
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

def dataprintoptcontrol():
    printlastinput = input("[y/n]PRINT LAST RECORD?")
    if printlastinput == 'y' or printlastinput == 'Y':
        printlastrecord()
    elif printlastinput == 'n' or printlastinput == 'N':
        main()
    elif printlastinput in keydataprint:
        printlastrecord()
    else:
        dataprint()

def main():
    dbtocsvproc()
    clrscr()
    title()
    printallrecord()
    opthead()
    
    opt = input("ENTER OPTION: ")
    
    if opt == '1':
        searchrecord(None, None)
    elif opt == '2':
        dataprint()
    elif opt == '3':
        entryrecord()
    elif opt == '4':
        updaterecord(None, None)
    elif opt == '5':
        dbtocsvproc()
        myvisual()
        main()
    elif opt == '6':
        deleteallrecords()
    elif opt == '7':
        csvwipe()
        exit()
    else:
        main()

def entryrecord():
    # declaring global the variable volume
    clrscr()    #1
    title()     #2
    noteonly()  #4
    
    # assigning getbitcoinprice to btcrate
    btcrate = getbitcoinprice()
    # Printallrecord() function is to display a 15 records that started from 1 as
    # A initialized record data report from print all record
    printallrecord()
    try:
        showrows = sqlqueryprintlastrecord()
        try:
            # getting the value of row[2] which is the BTC_Rate
            btcbalance = showrows[2]#float(input("\nENTER BTC BALANCE: "))
            dollarcost = showrows[3]#float(input("ENTER PHP COST: "))
            if showrows[6] == None:
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
    sqlqueryinsertrecord(btcrate, btcbalance, dollarcost, phpbalance, profitorloss, currency, mypredict)
    printlastrecord()

def dataprint():
    clrscr()    #1
    title()     #2
    # in case error in try then it will raise to except
    try:
        # Input id to start selected id to display record
        strtid = input("ENTER START ID: ")
        # classconn.mainconn is a connection for sqlite3 database bitcoindb.db
        print(sqlquerydataprint(strtid))
        # classconn.dataprintoptcontrol() are located above inside class classconn    
        dataprintoptcontrol()
        del strtid
        
    # in case theres an error in try it will execute except
    except:
        # The main() function are located at the top next from connclose()
        # function
        main()
    
#--------------dataprint end-------------#

def printlastrecord():
    clrscr()   #1
    # global declaration for variable row
    # This SQL execution is to select last record and only disply 1 row
    # which is the last record
    showrows = sqlqueryprintlastrecord()
    print(showrows)
    # calling mycol(None) function with None or empty parameters
    mycol(showrows)

# dataprint() function is to display selected started number of row to las record

def updaterecord(mysearch, updatenote):
    clrscr()
    title()
    if updatenote == None:
        noteonly()
    else:
        entryinvalid()
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
    noteonly()
    print("TARGET ID: ", idselection)
    printallrecord()
    updateoptlabel()
    
    myupdate = input("ENTER OPTION TO UPDATE: ")
    try:
        if myupdate == '1':
            btcrateupdate = float(input("ENTER NEW BTC RATE: "))
            sqlquery(btcrateupdate, idselection).btcrateupdate()
            print("RECORD UPDATED, ENTER TO CONTINUE"), input()
            printupdaterecord(idselection)

        elif myupdate == '2':
            btcbalanceupdate = float(input("ENTER NEW BTC BALANCE: "))
            sqlquery(btcbalanceupdate, idselection).btcbalanceupdate()
            print("RECORD UPDATED, ENTER TO CONTINUE"), input()
            printupdaterecord(idselection)

        elif myupdate == '3':
            dollarcostupdate = float(input("ENTER NEW DOLLAR COST: "))
            sqlquery(dollarcostupdate, idselection).dollarcostupdate()
            print("RECORD UPDATED, ENTER TO CONTINUE"), input()
            printupdaterecord(idselection)
        
        elif myupdate == '4':
            phpbalanceupdate = float(input("ENTER NEW PHP BALANCE: "))
            sqlquery(phpbalanceupdate, idselection).phpbalanceupdate()
            print("RECORD UPDATED, ENTER TO CONTINUE"), input()
            printupdaterecord(idselection)

        elif myupdate == '5':
            profitupdate = float(input("ENTER NEW PROFIT: "))
            sqlquery(profitupdate, idselection).profitupdate()
            print("RECORD UPDATED, ENTER TO CONTINUE"), input()
            printupdaterecord(idselection)
            
        elif myupdate == '6':
            phcurrencyupdate = float(input("ENTER NEW PHP CURRENCY: "))
            sqlquery(phcurrencyupdate, idselection).phcurrencyupdate()
            print("RECORD UPDATED, ENTER TO CONTINUE"), input()
            printupdaterecord(idselection)
        
        elif myupdate == 'n' or myupdate == 'N':
            main()

        else:
            invalid = 'err'
            updaterecord(None, invalid)
            del idselection, mysearch, myupdate, btcrateupdate, btcbalanceupdate, \
                dollarcostupdate, phpbalanceupdate, profitupdate
        
    except:
        clrscr()
        title()
        entryinvalid()
        printallrecord()
        print("\nPRESS ENTER TO RECONTINUE FOR THE VALID ENTRY")
        input()
        updaterecord(None, None)
        del idselection, mysearch, myupdate, btcrateupdate, btcbalanceupdate, \
            dollarcostupdate, phpbalanceupdate, profitupdate


def printupdaterecord(idselection):
    showrows = sqlqueryprintupdaterecord(idselection)
    #updaterecord()
    mycol(showrows)
    del idselection

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
        
        showrows = sqlquerysearch(mysearch)
        
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
            
        mycol(showrows)
    
    # When record can't be found from the database then it falls to except as the
    # next process
    except:
        nofoundrecordnote()    #5
        # This printallrecord() function are located below next from mycol() function
        printallrecord()
        
        # After processed not record found the variable searchagain input will
        # appear 
        searchagain = input("\n[n]To MAIN MENU\nSEARCH RECORD:")
        
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

def mycol(showrows):
    clrscr()    #1
    title()     #2
                                     #6
    print("CURRENT BITCOIN PRICE: ", getbitcoinprice())
    foundrecordnote()   #7
    
    # This is from the libarary prettytable to make a design fields and row for
    # the terminal designed system
    x.field_names = ["ID", "BTC_Rate", "BTC_Balance", "DOLLAR_Cost", "PHP_Balance", "Profit_Or_Loss", "PH_Currency", "BTC_Predict"]
    x.add_row([showrows[0], showrows[1], showrows[2], showrows[3], showrows[4], showrows[5], showrows[6], showrows[7]])
    
    # This variable mysearch are reassiged after mysearch from parameter used
    # the mysearch assigned with row[0], row[0] is the data ID of the specific
    #record from the database
    
    # This is printing or output with Fields and rows
    print(x)
    x.clear_rows()
    
    # This mycoloptcontrol(mysearch) is located at the top inside of class classconn
    # The mysearch parameter in mycoloptcontrol is to bring variable into
    # mycoloptcontrol(mysearch)
    mycoloptcontrol(showrows[0])

#---------------mycol--------------#

def deleteallrecords():
    uname = input("ENTER USERNAME: ")
    pword = getpass.getpass("ENTER PASSWORD: ")
    
    toconfirmuser = sqlqueryuserconfirm(uname, pword)
    
    if(toconfirmuser):
        if uname == toconfirmuser[1] and pword == toconfirmuser[2]:
            sqlquerydeleteallrecords()
            print("ALL RECORDS DELETED, GRANTED BY ADMIN ACCOUNT")
            input()
            main()
    else:
        print("WRONG USERNAME OR PASSWORD")
        input()
        main()
        del uname, pword

def deleterecord(mysearch):
    clrscr()
    title()
    noteonly()
    printallrecord()
    if mysearch == None:
        todelete = int(input("\n\nENTER ID TO DELETE: "))
    else:
        todelete = mysearch
        
    sqlquerydeleterecord(todelete)
    searchrecord(None, None)

if __name__ == "__main__":
    main()