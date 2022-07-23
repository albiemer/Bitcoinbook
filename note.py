import os
from bitcoinprice import getbitcoinprice

def title():
    print("////////////////////////////////////////////////////////////////////////////////////////////////////////")
    print("////////////////////////////////////////// BITCOIN BOOK SYSTEM /////////////////////////////////////////")
    print("///////////////////////////////// A BITCOIN MONITORING COMMAND SYSTEM //////////////////////////////////")
    print("////////////////////////////////////////////////////////////////////////////////////////////////////////\n")

def foundrecordnote():
    os.system("clear")
    title()
    print("CURRENT BITCOIN PRICE: ", getbitcoinprice(), "\nNote: FOUND RECORDS")

    
def nofoundrecordnote():
    os.system("clear")
    title()
    print("CURRENT BITCOIN PRICE: ", getbitcoinprice(), "\nNote: NO FOUND RECORDS")

def noteonly():
    print("CURRENT BITCOIN PRICE: ", getbitcoinprice(), "\nNote: ")


def opthead():
    print("[1] SEARCH RECORD")
    print("[2] DATA REPORT")
    print("[3] ADDNEW RECORD")
    print("[4] UPDATE RECORD")
    print("[5] VISUALIZATION")
    print("[6] DELETE ALL RECORDS")
    print("[7] EXIT")
    
def clrscr():
    os.system("clear")

#def clrche():
 #   os.system("sudo apt clean")
    
def rstrt():
    os.system("python3 bitcoinsys.py")
    
def entryinvalid():
    os.system("clear")
    title()
    print("CURRENT BITCOIN PRICE: ", getbitcoinprice(), "\nNote: ENTRY NOT RECORDED, INVALID INPUT!")