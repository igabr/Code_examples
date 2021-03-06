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

def euromillions(val):
	print()
	print("Here are the euromillions numbers: ")
	print()

	for i in range(val):
		main = random.sample(range(1,51), 5)
		aux = random.sample(range(1,13), 2)
		main.append(aux)
		print(main)
	print()

def lotto(val):
	print()
	print("Here are the lotto numbers: ")
	print()

	for i in range(val):
		main = random.sample(range(1,60), 6)
		print(main)


if __name__ == '__main__':
	euro_lines = input("How many lines for Euromillions would you like to generate? ")

	if euro_lines == "0":
		pass
	else:
		try:
			euromillions(int(euro_lines))
		except ValueError:
			print()
			print("Not a valid number - please enter an integer")
	
	lotto_lines = input("How many lines for National Lottery would you like to generate? ")

	if lotto_lines == "0":
		pass
	else:
		try:
			lotto(int(lotto_lines))
		except ValueError:
			print()
			print("Not a valid number - please enter an integer")
	
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
