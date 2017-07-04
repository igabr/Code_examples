#Ibrahim Gabr
import random
import os
import sys

"""
Simple script that will generate random lottery numbers for Euromillions and National
Lottery. Both games played in the UK. Think of this script as being the same as 'Lucky Dip'.

Usage:
	Go to terminal and type "python3 lottery.py"

Enjoy
"""

def get_euro():
	print()
	euro_lines = input("How many lines for Euromillions would you like to generate? ")
	print()
	print("Here are the euromillions numbers: ")
	print()

	try:
		val = int(euro_lines)
		return val
	except ValueError:
		print()
		print("Not a valid number - please enter an integer!")
		print()
		return get_euro()


def get_lotto():

	lotto_lines = input("How many lines for National Lottery would you like to generate? ")
	print()
	print("Here are the lotto numbers: ")
	print()

	try:
		val = int(lotto_lines)
		return val
	except ValueError:
		print()
		print("Not a valid number - please enter an integer")
		print()
		return get_lotto()


def euromillions():

	for i in range(get_euro()):
		main = random.sample(range(1,51), 5)
		aux = random.sample(range(1,13), 2)
		main.append(aux)
		print(main)
	print()

def lotto():

	for i in range(get_lotto()):
		main = random.sample(range(1,60), 6)
		print(main)



if __name__ == '__main__':
	euromillions()
	lotto()
	
	question = input("""
	Would you like to generate numbers again?

	1. Yes

	2. No

	Answer: """)
	if question == "1":
		os.system("clear")
		os.system("python3 lottery_test.py")
	else:
		os.system("clear")
		sys.exit()
