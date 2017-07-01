import requests
import os
import sys
from datetime import datetime

"""
This is a simple script that allows you to check on your Ethereum Stash via Terminal. Saves you having to go online!

Be sure to enter your wallet address in the variable entitled url

Be sure to enter the total amount you have invested in the variable entitled investment_amount. This should be in integer/float format and NOT a string

I am assuming that you have all relevant packages installed ahead of time.

required libraries:
	- requests
	- os
	- sys
	- datetime

Usage:
	Go to terminal and type python3 eth.py

	Follow on screen instructions.

Let me know if you spot any errors or have comments/suggestions for improvement! This was my first attempt!

If you wish to tip me with Ethereum, please send ETH to: 0x959aA35f8fa56A54E9984EaEE08BDa583C82C0e0
"""

CONSTANT = 1000000000000000000

url = "https://api.etherscan.io/api?module=account&action=balance&address=INSERT YOUR WALLET ADDRESS HERE&tag=latest"

investment_amount = #TYPE TOTAL AMOUNT YOU HAVE INVESTED SO FAR HERE IN NUMBERS

buy_price = float(requests.get('https://api.coinbase.com/v2/prices/ETH-USD/buy')
	.json()['data']['amount'])

sell_price = float(requests.get('https://api.coinbase.com/v2/prices/ETH-USD/sell')
	.json()['data']['amount'])

eth_stash = int(requests.get(url).json()['result'])/CONSTANT

current_valuation = sell_price * eth_stash

return_percentage = ((current_valuation-investment_amount)/(investment_amount))*100



def get_info():

	print()
	print("-------------Coinbase Info-------------")
	print()
	print(datetime.now().strftime("%d-%m-%Y %H:%M"))
	print()
	print("ETH stash: ", eth_stash, "ETH")
	print()
	print("The current buy price of 1 ETH is: ${}".format(buy_price))
	print()
	print("The current sell price of 1 ETH is: ${}".format(sell_price))
	print()
	print("Your current stock is worth: ${:,}".format(int(current_valuation)))
	print()
	print("Your current rate of return is: {0:.2f} %".format(return_percentage))
	print()


def conversion(parameter_1, parameter_2):

	amount = input("Please type in an {} amount for conversion to {} : ".format(parameter_1, parameter_2))

	try:
		float_amount = float(amount)
	except ValueError:
		print()
		print("This is not a valid amount")
		print()
		conversion(parameter_1, parameter_2)

	if parameter_1 == "ETH":
		USD_value = sell_price * float_amount
		print()
		print("{} ETH is approx {} USD".format(float_amount, USD_value))
		print()

	if parameter_1 == "USD":
		eth_value = float_amount/buy_price
		print()
		print("{} USD is approx {} ETH".format(float_amount, eth_value))
		print()

	question = input("""Would you like to perform another {}-{} conversion?
		
		1. Yes

		2. Switch to {}-{} conversion

		Press any key to exit.

		Option Selection: """.format(parameter_1, parameter_2, parameter_2, parameter_1))

	if question == "1":
		print()
		conversion(parameter_1, parameter_2)
	elif question == "2":
		print()
		conversion(parameter_2, parameter_1)
	else:
		os.system("clear")
		sys.exit()


if __name__ == '__main__':
	print()
	get_info()

	question = input('''What type of conversion would you like to do:
    
    	1. ETH to USD

    	2. USD to ETH

    	Press any key to exit.

    	Option Selection: ''')

	print()

	if question == "1":
		from_ = "ETH"
		to = "USD"

		conversion(from_, to)

	elif question == "2":
		from_ = "USD"
		to = "ETH"

		conversion(from_, to)

	else:

		os.system("clear")
		sys.exit()

