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
	euro_lines = input("How many lines for Euromillions would you like to generate? ")

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

	try:
		val = int(lotto_lines)
		return val
	except ValueError:
		print()
		print("Not a valid number - please enter an integer")
		print()
		return get_lotto()

def euromillions(lines):

	if lines <= 0:
		print("----**No lines generated**----")
	else:
		for i in range(lines):
			main= random.sample(range(1, 51), 5) #range is not inclusive
			aux = random.sample(range(1,13), 2) #range is not inclusive
			main.append(aux)
			print(main)

def lotto(lines):

	if lines <= 0:
		print("----**No lines generated**----")
	else:
		for i in range(lines):
			main = random.sample(range(1, 60), 6) #range is not inclusive
			print(main)

if __name__ == '__main__':
	print()
	euro_range = get_euro()
	print()
	lotto_range = get_lotto()
	print()
	print("Here are the euromillions numbers: ")
	print()
	euromillions(euro_range)
	print()
	
	print("Here are the lotto numbers: ")
	print()
	lotto(lotto_range)
	
	question = input("""
	Would you like to generate numbers again?

	1. Yes

	2. No

	Answer: """)
	if question == "1":
		os.system("clear")
		os.system("python3 lottery.py")
	else:
		os.system("clear")
		sys.exit()
