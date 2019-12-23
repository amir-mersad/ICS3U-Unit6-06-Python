#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: December 2019
# This program return hexa decimal

import random


def Hexadecimal(word):
    characters = []
    hexa = {'a': 61,
            'b': 62,
            'c': 63,
            'd': 64,
            'e': 65,
            'f': 66,
            'g': 67,
            'h': 68,
            'i': 69,
            'j': "6a",
            'k': "6b",
            'l': "6c",
            'm': "6d",
            'n': "6e",
            'o': "6f",
            'p': "70",
            'q': "71",
            'r': "72",
            's': "73",
            't': "74",
            'u': "75",
            'v': "76",
            'w': "77",
            'x': "78",
            'y': "79",
            'z': "7a",
            }
    # Findinf the hexadecimal equivelent
    for element in word:
        if element in hexa.keys():
            characters.append(hexa[element])
        else:
            return "-1"
    return characters


def main():
    # This function gets the input and passes it to another function
    # Input
    word = input("Please enter the word (only small letters): ")
    # Passing to another function
    if word != "":
        result = Hexadecimal(word)
    # Output
    if result == "-1":
        print("Wrong input !!!")
        return
    for each in result:
        print(each, end=" ")


if __name__ == "__main__":
    main()
