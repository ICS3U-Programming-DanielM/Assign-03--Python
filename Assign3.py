#!/usr/bin/env python3
# Created By: Daniel Momoh
# Date: Oct 14th, 2022
# this program checks if a alphabet is lowercase or uppercase


def main():
    # Ask user to input the Letter that needs to be tested
    letter = input("Enter the Letter: ")
    letter_as_int = ord(letter)
    print(letter_as_int)

    # check to see if the letter is either upper or lower case letters
    if letter >= "A" and letter <= "Z":
        print(letter, " is an Uppercase letter")
    elif letter >= "a" and letter <= "z":
        print(letter, " is a Lowercase letter")
    else:
        print(letter, " is not an Alphabet")


if __name__ == "__main__":
    main()
