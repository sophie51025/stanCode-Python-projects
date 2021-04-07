"""
File: hailstone.py
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, as defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    When user keys in a number, the app will show Hailstone sequences till it reaches 1, and shows steps.
    """
    print('This program computes Hailstone sequences.')
    print()
    number = int(input('Enter a number: '))
    # count: to count how many steps to reach 1
    count = 0
    if number == 1:
        print('it took ' + str(count) + ' step to reach 1')
    if number <= 1:
        print('Please enter number that is >= 1')
    else:
        while True:
            if number == 1:
                break
            elif number % 2 != 0:
                updated_number = 3*number + 1
                count += 1
                print(str(number) + ' is odd, so I make 3n+1: ' + str(updated_number))
                number = updated_number
            else:
                updated_number = number // 2
                count += 1
                print(str(number) + ' is even, so I make half: ' + str(updated_number))
                number = updated_number



        print('it took ' + str(count) + ' step(s) to reach 1')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
