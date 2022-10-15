#!/usr/bin/env python3
# Created By: Daniel Momoh
# Date: Oct 14th, 2022
# this program checks if a alphabet is lowercase or uppercase


letter = input("Enter the Letter: ")
if (letter >= 'A' and letter <= 'Z'):
    print(letter, " is an Uppercase letter")
elif (letter >= 'a' and letter <= 'z'):
    print(letter, " is a Lowercase letter")
else:
    print(letter, " is not an Alphabet")
