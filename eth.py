'''Short script I wrote to check the current price of Ethereum through your terminal! 
Saves you having to check online websites'''

import requests
import os
import sys
r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD')
price = r.json()['USD']
print()
print("The current price of 1 ETH is: {}".format(price))
print()

q = input('''
	What type of conversion would you like to do:

	1. ETH to USD

	2. Conversion from USD

	3. Exit program 
	
	Option Selection: ''')
print()

if q == "1":
    eth = input("Please type in an ETH amount for conversion to USD:  ")
    USD = price*float(eth)
    print()
    print("{} ETH is approx {} USD".format(eth, USD))
    print()
    question = input('''Would you like to perform another conversion?
    	1. Yes
    	2. No 
    	Option Selection: ''')
    if question == '1':
    	os.system('python3 eth.py')
    else:
    	print()
    	print("Have a great day!")
    	print()
    	sys.exit()
elif q == "2":
    USD = input("Please type in a US amount for a conversion to ETH:  ")
    eth = float(USD)/price
    print("{} USD is approx {} ETH".format(USD, eth))
    print()
    question = input('''Would you like to perform another conversion?
    	1. Yes
    	2. No 
    	Option Selection: ''')
    if question == '1':
    	os.system('python3 eth.py')
    else:
    	print()
    	print("Have a great day!")
    	print()
    	sys.exit()
else:
	print()
	print("Have a great day!")
	print()
	sys.exit()
