"""
File: complement.py
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This App provides complement sequence of DNA
    """
    dna = input('Please give me a DNA strand and I\'ll find the complement:')
    dna = dna.upper()
    complement_dna = find_complement(dna)

    print('The complement of ' + dna + ' is ' + complement_dna)


def find_complement(dna):
    """

    :param dna: str, DNA consequence provided by user to be compared
    :return: str, complement DNA consequence for given DNA consequence
    """
    complement = ''
    for i in range(len(dna)):
        ch = dna[i]
        if ch == 'A':
            complement += 'T'
        elif ch == 'T':
            complement += 'A'
        elif ch == 'C':
            complement += 'G'
        else:
            complement += 'C'
    return complement

###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
