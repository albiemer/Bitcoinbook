
import requests, json
from time import sleep

import os
import sqlite3
from prettytable import PrettyTable, from_db_cursor
import sys

x = PrettyTable()
errmain = 0

def getBitcoinPrice():
    URL = 'https://www.bitstamp.net/api/ticker/'
    try:
        r = requests.get(URL)
        priceFloat = float(json.loads(r.text)['last'])
        return priceFloat
    except requests.ConnectionError:
        print ("Error querying Bitstamp API")

bitcoinprice = getBitcoinPrice()
		


###########MAIN MODULE############

def main():
	#os.system("clear")
	global mysearch, x
	printallrecord()
	
	def opthead():
		print("[1] SEARCH RECORD")
		print("[2] DATA REPORT")
		print("[3] ADDNEW RECORD")
		print("[4] UPDATE RECORD")
		print("[5] DELETE OPTION")
		print("[ENTER] to exit:")
	opthead()
		
	opt = input("ENTER OPTION: ")
	if opt == '1':
		#os.system("clear")
		searchrecord()
			
	elif opt == '2':
		dataprint()
			
	elif opt == '3':
		entryrecord()
		
	elif opt == '4':
		updaterecord()
		
	elif opt == '5':
		deleterecord()
			
	else:
		print("exit")
		#main()
		#print("invalid input")
		#invalidput = input("please enter
	
##########MAIN MODULE#############
def myexit():
	uexit = input("EXIT BITCOIN SYSTEM?")
	if uexit == 'y' or uexit == 'Y':
		exit()
	else:
		exit()

############SEARCH RECORD##########
#                                                                                  #

def searchrecord():
	try:
		#os.system("clear")
		printallrecord()
		mysearch = input("SEARCH RECORD: ")
		global row, conn, c
		conn = sqlite3.connect('bitcoindb.db')
		c = conn.cursor()
		c.execute("select * from BITCOIN_TABLE where ID=?",(mysearch,))
		row = c.fetchone()
		conn.rollback()
		conn.close()
		mycol()
			
	except:
		print("Result Not Found")
		searchagain = input("[y/n SEARCH AGAIN?:")
		if searchagain == 'y' or searchagain == 'Y':
			searchrecord()
			x=None
		else:
			x=None
			main()

		
#                                                                                  #
##########SEARCH MODULE###########

#---------------mycol--------------#

def mycol():
	global x
	printallrecord()
	print("RESCENT FOUND RECORDS AND CURRENT FOUND RECORD OR PRINT LAST RECORD")
	x.field_names = ["ID", "BTC RATE", "BTC BALANCE", "PHP COST", "PHP BALANCE", "PROFIT"]
	x.add_row([row[0], row[1], row[2], row[3], row[4], row[5]])
	
	print(x)
	
	print("Note: to exit and back to main menu press [n] or type [exit]")
	toexit = input("[y/n] SEARCH ANOTHER RECORD? ")
	if toexit == 'y' or toexit == 'Y':
		searchrecord()
		
	elif toexit == 'n' or toexit == 'N':
		try:
			x=None
			main()
		except:
			exit()	
			
	else:
		searchrecord()
		print("toexit")

#---------------mycol--------------#
                 

#------------printallrecord------------#

def printallrecord():
	os.system("clear")
	print("////////////////////////////////////////")
	print("//////// BITCOIN FINANCIAL RECORD //////")
	print("////////////////////////////////////////\n")
	global conn, c
	
	conn = sqlite3.connect('bitcoindb.db')
	c = conn.cursor()
	
	c.execute("select * from BITCOIN_TABLE limit 5")
	
	x = from_db_cursor(c)
	print(x)
	#	exitprintallrecord()
	
	conn.close()
	
#-----------printallrecord-------------#

#########SEARCH MODULE END##########


##########DATA REPORT BEGIN##########

#-------------dataprint--------------#

def dataprint():
	os.system("clear")
	print("////////////////////////////////////////")
	print("//////// BITCOIN FINANCIAL RECORD //////")
	print("////////////////////////////////////////\n")
	global conn, c
	
	conn = sqlite3.connect('bitcoindb.db')
	c = conn.cursor()
	c.execute("select * from BITCOIN_TABLE")
	
	x = from_db_cursor(c)
	
	print(x)
	
	printlastinput = input("[y/n]PRINT LAST RECORD?")
	if printlastinput == 'y' or printlastinput == 'Y':
		printlastrecord()
	elif printlastinput == 'n' or printlastinput == 'N':
		main()
	else:
		dataprint()
	
#	exitprintallrecord()

#--------------dataprint-------------#


#------------printlastecord-----------#

def printlastrecord():
	os.system("clear")
	global row
	global conn, c
	
	conn = sqlite3.connect('bitcoindb.db')
	c = conn.cursor()
	c.execute("select * from BITCOIN_TABLE order by ID desc limit 1")
	
	row = c.fetchone()
	
	mycol()
	
	conn.commit()
	conn.close()
	

#------------printlastrecord-----------#

##########DATA PRINT END###########

###########ADDNEW RECORD##########

def entryrecord():
	global btcrate
	global btcbalance
	global phpcost
	global phpbalance
	global profitorloss
	
	os.system("clear")
	
	btcrate = bitcoinprice
	btcbalance = float(input("ENTER BTC BALANCE: "))
	phpcost = float(input("ENTER PHP COST: "))
	phpbalance = btcrate * btcbalance
	profitorloss = int(phpbalance) - int(phpcost)
	phpbalance = int(phpbalance) * 50.40
	phpbalance = int(phpbalance)
	insertrecord()
	
def insertrecord():
	global conn, c
	
	conn = sqlite3.connect('bitcoindb.db')
	c = conn.cursor()
	c.execute("insert into BITCOIN_TABLE(BTC_Rate, BTC_Balance, PHP_Cost, PHP_Balance, Profit_Or_Loss) values (?,?,?,?,?)", (btcrate, btcbalance, phpcost, phpbalance, profitorloss))
	
	print("INSERTED DATA SUCCESSFULLY")
	
	conn.commit()
	
	conn.close()
	
	exitinsertrecord = input("[y/n] EXIT: ")
	
	if exitinsertrecord == 'y' or exitinsertrecord == 'Y':
		main()
		
	elif exitinsertrecord == 'n' or exitinsertrecord == 'N':
		entryrecord()
	
########ADDNEW RECORD END##########

###########UPDATE RECORD###########

def updaterecord():
	os.system("clear")
	os.system("clear")
	print("////////////////////////////////////////")
	print("//////// BITCOIN FINANCIAL RECORD //////")
	print("////////////////////////////////////////\n")
	printallrecord()
	idselection = int(input("ENTER ID TO UPDATE: "))
	os.system("clear")
	printallrecord()
	print("[1] BTC RATE")
	print("[2] BTC BALANCE")
	print("[3] PHP COST")
	print("[4] PHP BALANCE")
	print("[5] PROFIT / LOSS")
	
	myupdate = int(input("ENTER OPTION TO UPDATE: "))
	
	if myupdate == 1:
		
			btcrateupdate = float(input("ENTE NEW BTC RATE: "))
			
			c.execute("update BITCOIN_TABLE set BTC_Rate = ? where ID = ?", (btcrateupdate, idselection))
			
			conn.commit()
			conn.close()
			
			while True:
				exitupdate()
				
	elif myupdate == 2:
		
		btcbalanceupdate = float(input("ENTER NEW BTC BALANCE: "))
		
		c.execute("update BITCOIN_TABLE set BTC_Balance = ? where ID = ?", (btcbalanceupdate, idselection))
		
		conn.commit()
		conn.close()
		
		while True:
			exitupdate()
		
	elif myupdate == 3:
		phpcostupdate = float(input("ENTER NEW PHP COST: "))
		
		c.execute("update BITCOIN_TABLE set PHP_Cost = ? where ID = ?", (phpcostupdate, idselection))
		conn.commit()
		conn.close()
		
		while True:
			exitupdate()
		
	elif myupdate == 4:
		phpbalanceupdate = float(input("ENTER NEW PHP BALANCE: "))
		
		c.execute("update BITCOIN_TABLE set PHP_Balance = ? where ID = ?", (phpbalanceupdate, idselection,))
		
		conn.commit()
		conn.close()
		
		while True:
			exitupdate()
		
	elif myupdate == 5:
		profitupdate = float(input("ENTER NEW PROFIT: "))
		
		c.execute("update BITCOIN_TABLE set Profit_Or_Loss = ? where ID = ?", (profitupdate, idselection))
		
		conn.commit()
		conn.close()
		
		while True:
			exitupdate()

##########UPDATE RECORD END########

###########DELETE RECORD###########

def deleterecord():
	os.system("clear")
	printallrecord()
	todelete = int(input("ENTER ID TO DELETE: "))
	
	global conn, c
	
	conn = sqlite3.connect('bitcoindb.db')
	c = conn.cursor()
	
	c.execute("delete from BITCOIN_TABLE where ID = ?", (todelete,))
	
	conn.commit()
	conn.close()
	
	print("DELETED SUCCESSFUL")
	
	while True:
		exitdelete()
		
def exitdelete():
	exitq = input("[y/n] EXIT? :")
	
	if exitq == 'n' or exitq == 'N':
		deleterecord()
		
	elif exitq == 'y' or exitq == 'Y':
		main()
		
	else:
		print("please choose the right option")

##########DELETE RECORD END#########

if __name__=="__main__":
	main()
	
