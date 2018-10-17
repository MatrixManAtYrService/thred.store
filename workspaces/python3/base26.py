# coding: utf-8
import itertools

def letters_to_numbers(string):
    numbers = []
    for char in string:
        it = ord(char.upper()) - 64
        if it < 1 or it > 26:
            raise ValueError("A to Z doesn't include: " + char)
        numbers.append(it)
    return numbers

def numbers_to_letters(numbers):
    string = ""
    for number in numbers:
        string += chr(number + 64)
    return string
