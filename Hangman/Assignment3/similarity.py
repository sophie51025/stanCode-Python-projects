"""
File: similarity.py
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program finds the most similar sequence of short sequence from long sequence
    """
    long_dna = input('Please give me a DNA sequence to search:')
    long_dna = long_dna.upper()
    short_dna = input('What DNA sequence would you like to match?')
    short_dna = short_dna.upper()
    length_long = len(long_dna)
    length_short = len(short_dna)

    # the variable save total match count of certain piece of long DNA
    match_count = 0
    max_count = match_count
    for i in range(length_long - (length_short - 1)):
        match_count = 0
        mapping = long_dna[i:i + length_short]  # the certain piece of long DNA to be mapped
        for j in range(length_short):
            ch = mapping[j]
            if ch == short_dna[j]:
                match_count += 1
        if match_count > max_count:
            max_count = match_count
            max_match_dna = long_dna[i:i + length_short]
    print('')
    print('The best match is ' + max_match_dna)
    print('Total match ' + str(max_count) + ' letter(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
