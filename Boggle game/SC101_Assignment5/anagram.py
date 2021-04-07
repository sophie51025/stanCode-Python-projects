"""
File: anagram.py
Name: Sophie
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

#globle variable
dic_list = {'a': [], 'b': [], 'c': [],'d': [],'e': [],'f': [],'g': [],'h': [],'i': [], 'j': [], 'k': [], 'l': [],
            'm': [], 'n': [],'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [],
            'y': [], 'z': []}

#how many arrangements have been listed
count = 0

def main():
    global count
    read_dictionary()
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        target_voc = str(input('Find anagrams for: '))
        if target_voc == EXIT:
            break
        else:
            print('Searching...')
            find_anagrams(target_voc)
            count = 0


def read_dictionary():
    global dic_list
    with open(FILE, 'r') as f:
        for line in f:
            line_1 = line.split()
            voc = line_1[0]
            first_letter = voc[0]
            dic_list[first_letter].append(voc)


def find_anagrams(s):
    """
    :param s:word assigned to find anagram from
    """
    matched_voc = []
    matched_num = 0
    #check if there's duplicate letter. If yes, change it into ste(number)

    letter_compo =[]
    change_list = {}
    duplicate_num = 1
    for letter in s:
        if letter not in letter_compo:
            letter_compo.append(letter)
        else:
            letter_compo.append(str(duplicate_num))
            change_list[str(duplicate_num)] = letter
            duplicate_num += 1
    new_s = ''
    for l in letter_compo:
        new_s += l

    total_arrangement = factorial(len(new_s))
    possible_list = []
    find_anagrams_helper(new_s, '', possible_list, total_arrangement)

    #change back the right letter
    right_anagram = []
    for voc in possible_list:
        right_voc = ''
        for ch in voc:
            if ch in change_list:
                correct_letter = change_list[ch]
                right_voc += correct_letter
            else:
                right_voc += ch
        right_anagram.append(right_voc)

    #remove duplicate voc
    remove_anagram = []
    for v in right_anagram:
        if v not in remove_anagram:
            find_match = has_prefix(v[0:1])
            if find_match is True:
                remove_anagram.append(v)

    #check vov exists in dic
    for arrangement in remove_anagram:
        if arrangement in dic_list[arrangement[0]]:
            matched_voc.append(arrangement)
            matched_num += 1
            print('Found:', arrangement)
            print('Searching...')
    print(matched_num,'anagrams:',matched_voc)


def find_anagrams_helper(search_voc, current, possible_list, total_arrangement):
    """

    :param search_voc: vocabulary key-in by user
    :param current: start string
    :param possible_list: possible anamgrams
    :param total_arrangement: check how many composition of letters
    :return: find all possible arrangements for key-in word
    """
    global count
    if len(current) == len(search_voc):
        if count < total_arrangement - 1:
            possible_list.append(current)
            count += 1
        else:
            possible_list.append(current)
            count += 1
            return possible_list

    else:
        for letter in search_voc:
            if letter not in current:
                #choose
                current += letter
                #explore
                find_anagrams_helper(search_voc, current, possible_list, total_arrangement)
                #un-choose
                current = current[0:len(current)-1]
        if count == total_arrangement:
            return


def has_prefix(sub_s):
    """
    :param sub_s: quick search keywords
    :return: False (if no voc starts with sub_s) True(if there's voc starts with sub_s)
    """
    search_letter = sub_s
    start_letter = search_letter[0]
    search_range = dic_list[start_letter]
    for voc in search_range:
        match = voc.startswith(sub_s)
        if match is True:
            return match
        elif voc == search_range[len(search_range)-1] and match is False:
            return match

def factorial(letter_qty):
    """
    :param letter_qty: how many letters are key in
    :return: total arrangement qty
    """
    if letter_qty == 0:
        return 1
    else:
        temp = letter_qty * factorial(letter_qty - 1)
        return temp


def change_letter(duplicate_num):
    """
    :param duplicate_num: how many letters are found to appear more than once
    :return: str(num) to replace duplicate letter
    """

    return

if __name__ == '__main__':
    main()
