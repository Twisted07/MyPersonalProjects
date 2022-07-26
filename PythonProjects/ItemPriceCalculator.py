

from asyncio.format_helpers import extract_stack
from curses import tparm

#Takes input of workers
workers = input("How many workers does it take to produce this item? \n")
try:
    nworkers = int(workers)
except:
    print("That is not a number")

materials = input("How much did you spend on materials and packaging? \n")
try:
    nmaterials: float(materials)
except:
    print("Insert the amount it cost you to produce this item.\n")
transport = input("How much did you spend on transportation during production? \n")

#Takes input of workmanship
workmanship = input("How much would you like to include as workmanship? \n")
try:
    nworkmanship = float(workmanship)
except:
    print("Please insert an amount in digits. \n")

extras = input("How much would you like to include for extra costs? \n")
try:
    nextras = float(extras)
except:
    print("Please insert digits only. \n")

profit = input("How much profit would you like to make on this item? \n")
try:
    nprofit = float(profit)
except:
    print("Insert profit in digits only.")