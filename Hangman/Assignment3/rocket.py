"""
File: rocket.py
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# the size design the wide of rocket
SIZE =5


def main():
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	"""
	This function made the head of rocket in assigned size
	"""

	for i in range(SIZE):
		for j in range(i,SIZE):
			print(' ', end='')
		for k in range(i+1):
			print('/', end='')
		for l in range(i + 1):
			print('\\', end='')
		print('')


def belt():
	"""
	This function made the belt of rocket in assigned size
	"""
	print('+', end='')
	for j in range(SIZE * 2):
			print('=', end='')
	print('+')


def upper():
	"""
	This function madd the upper body of rocket in assigned size
	"""
	for i in range(SIZE):
		print('|', end='')
		for j in range(i,SIZE-1):
			print('.', end='')
		for k in range(i+1):
			print('/', end='')
			print('\\', end='')
		for j in range(i,SIZE-1):
			print('.', end='')
		print('|')


def lower():
	"""
	This function made the lower body of rocket in assigned size
	"""
	for i in range(SIZE):
		print('|', end='')
		for k in range(i):
			print('.', end='')
		for k in range(i,SIZE):
			print('\\', end='')
			print('/', end='')
		for k in range(i):
			print('.', end='')
		print('|')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()