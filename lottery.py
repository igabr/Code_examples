#Ibrahim Gabr
import random
import os
import sys

"""
Simple script that will generate random lottery numbers for Euromillions and National
Lottery. Both games played in the UK. Think of this script as being the same as 'Lucky Dip'.

The script will generate 5 lines for each lottery.

Usage:
	Go to terminal and type "python3 lottery.py"

Enjoy
"""

def euromillions():

	for i in range(5):
		main= random.sample(range(1, 51), 5) #range is not inclusive
		aux = random.sample(range(1,13), 2) # 2 lucky stars
		main.append(aux)
		print(main)

def lotto():

	for i in range(5):
		main = random.sample(range(1, 60), 6)
		print(main)

if __name__ == '__main__':
	print()
	print("Here are the euromillions numbers: ")
	print()
	euromillions()
	print()
	print("Here are the lotto numbers: ")
	print()
	lotto()
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
