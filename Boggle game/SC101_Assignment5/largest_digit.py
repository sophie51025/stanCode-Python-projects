"""
File: largest_digit.py
Name: Sophie
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:a number to be filtered
	:return:largest digit of the number
	"""
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, current_largest):
	if int(n/10) == 0 and current_largest == 0:
		if 0 <= n:
			return(n)
		else:
			return(-n)
	elif n == 0:
		return (current_largest)
	else:
		if n < 0:
			n = -n
		last_digit = n % 10
		if last_digit > current_largest:
			current_largest = last_digit
		return find_largest_digit_helper(n//10, current_largest)

if __name__ == '__main__':
	main()
