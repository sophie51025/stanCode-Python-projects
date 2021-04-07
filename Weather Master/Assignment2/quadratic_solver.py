"""
File: quadratic_solver.py
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	When user input a,b,c variables, the app will show the roots of equation ax^2 + bx + c = 0
	"""
	print('Hi, welcome to stanCode Quadratic Solver!')
	print('let me help you calculate the roots of equation ax^2 + bx + c = 0 ')
	print('Give me a,b,c')
	a = int(input('your a ?'))
	b = int(input('your b ?'))
	c = int(input('your c ?'))

	discriminant = b*b - 4 * a * c
	if discriminant < 0:
		print('sorry! No real roots')
	elif discriminant == 0:
		x = -b/(2*a)
		print('one root: ' + str(x))
	else:
		discriminant_root = math.sqrt(discriminant)
		x1 = (-b + discriminant_root)/(2*a)
		x2 = (-b - discriminant_root)/(2*a)
		print('Two roots: ' + str(x1) + ' & ' + str(x2))



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
