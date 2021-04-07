"""
File: boggle.py
Name: Sophie
----------------------------------------
TODO: after key in 16 letters with correct formate, app will show possible voc whose letters is longer than 3 letters.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

#globle variable
dic_list = {'a': [], 'b': [], 'c': [],'d': [],'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [],
            'm': [], 'n': [],'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [],
            'y': [], 'z': []}

#this control if 16 letters are key in with correct format
complete = None


def main():
	"""
	TODO: after key in 16 letters with correct formate, app will show possible voc whose letters is longer than 3 letters.
	"""
	read_dictionary()
	letter_list = []
	row_num = 1
	if input_boggle(row_num, letter_list) is False:
		pass
	else:
		print('Searching....')
		found_voc_list = []
		for i in range(len(letter_list)):
			current_list = letter_list.copy()
			voc_string = ''
			found_boggle(i, 0, voc_string, current_list, letter_list, found_voc_list, [])
		print(f'There are {len(found_voc_list)} words in total.')


def found_boggle(start_position, steps_moved, current_string, current_list, letter_list, found_voc_list, possible_route):
	if len(current_string) >= 4 and current_string in dic_list[current_string[0]] and current_string not in found_voc_list:
		print(f'Found "{current_string}"')
		found_voc_list.append(current_string)
		#explore
		found_boggle(start_position, steps_moved, current_string, current_list, letter_list, found_voc_list, possible_route)
		current_string = current_string[0:len(current_string) - 1]
		pass
		#un-chose
	else:
		if len(current_string) == 0:
			current_string += current_list[start_position]
			current_list[start_position] = '1'

		#defined possible moving route
		if start_position == 0 or start_position == 4 or start_position == 8 or start_position == 12:
			possible_route = [-4, -3, 1, 4, 5]
		elif start_position == 3 or start_position == 7 or start_position == 11 or start_position == 15:
			possible_route = [-5, -4, -1, 3, 4]
		else:
			possible_route = [-5, -4, -3, -1, 1, 3, 4, 5]

		for next_position in possible_route:
			#choose
			if 15 >= start_position + next_position >= 0:
				if current_list[start_position + next_position] != '1':
					next_letter = current_list[start_position + next_position]
					current_string += next_letter

					if len(current_string) == 3:
						if has_prefix(current_string) is False:
							current_string = current_string[0:len(current_string) - 1]
							pass
						else:
							current_list[start_position + next_position] = '1'
							steps_moved = next_position
							found_boggle(start_position + steps_moved, steps_moved, current_string, current_list, letter_list,
										 found_voc_list, possible_route)
							current_string = current_string[0:len(current_string) - 1]
							current_list[start_position + next_position] = letter_list[start_position + next_position]
					# explore
					else:
						current_list[start_position + next_position] = '1'
						steps_moved = next_position
						found_boggle(start_position + steps_moved, steps_moved, current_string, current_list, letter_list, found_voc_list, possible_route)
						# un-choose
						current_string = current_string[0:len(current_string)-1]
						current_list[start_position + next_position] = letter_list[start_position + next_position]


def input_boggle(row_num, letter_list):
	"""
	This function ask user to key in letters as a start of boggle game
	:param row_num: how many rows have been key in
	:param letter_list: current letter list provided
	:return: True or False
	"""
	global complete
	if row_num == 5:
		complete = True
		return complete
	else:
		row = input(str(str(row_num) + ' row of letters:'))
		if 8 > len(row) >= 7:
			if row[1] and row[3] and row[5] != (' '):
				print('Illegal input')
				complete = False
				return complete
			else:
				for i in range(0, 7, 2):
					letter = row[i].lower()
					letter_list.append(letter)
				row_num += 1
				input_boggle(row_num, letter_list)
				if complete is True:
					return True
				else:
					return False

		elif len(row) >= 8:
			for i in range(len(row)-7):
				if row[7+i] != (' '):
					print('Illegal input')
					complete = False
					return complete
			for i in range(0, 7, 2):
				letter = row[i].lower()
				letter_list.append(letter)
			row_num += 1
			input_boggle(row_num, letter_list)
		else:
			print('Illegal input')
			complete = False
			return complete


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dic_list
	with open(FILE, 'r') as f:
		for line in f:
			line_1 = line.split()
			voc = line_1[0]
			first_letter = voc[0]
			dic_list[first_letter].append(voc)



def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	search_letter = sub_s
	start_letter = search_letter[0]
	search_range = dic_list[start_letter]
	for voc in search_range:
		match = voc.startswith(search_letter)
		if match is True:
			return True
		elif voc == search_range[len(search_range) - 1] and match is False:
			return False


if __name__ == '__main__':
	main()
