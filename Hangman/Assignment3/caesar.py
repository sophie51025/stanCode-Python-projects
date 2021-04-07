"""
File: caesar.py
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    When secret codes and secret numbers are provided, the program is able to unveil true message.
    """
    secret_number = int(input('Secret number: '))
    cipher = input('What\'s the ciphered string? ')
    cipher = cipher.upper()
    new_order = ciphered_order(secret_number)
    decipher = real_word(cipher, new_order)

    print('The deciphered string is : ' + decipher)


def ciphered_order(secret_number):
    """
    :param secret_number: int, how many letters moved for ciphered order
    :return: str, ciphered order for deciphering
    """
    new_order = ''
    for i in range(secret_number):
        new_order = ALPHABET[len(ALPHABET)-(i+1)] + new_order
    for j in range(len(ALPHABET)-secret_number):
        new_order += ALPHABET[j]
    return new_order


def real_word(cipher, new_order):
    """
    :param cipher:str, words to be deciphered
    :param new_order: str, ciphered order for deciphering
    :return: real_word delivered by user
    """
    new_word = ''
    for i in range(len(cipher)):
        ch = cipher[i]
        if not ch.isalpha():
            new_word += ch
        else:
            order = new_order.find(ch)
            new_word += ALPHABET[order]
    return new_word


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
