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
    letters = []
    for number in numbers:
        letters.append(str(chr(number + 64)))
    return numbers
        
def numbers_to_data(numbers, base=26):
    number = 0
    for i, n in enumerate(reversed(numbers), 1):
        number += (n * base)**i 
    return numbers
    
import IPython
def data_to_numbers(data, base=26):

    # how many numbers will it take?
    counter = itertools.count(start=1)
    places = []
    while True:
        place = base**next(counter)
        places.append(place)
        if place > data:
            break
            
    print(digit_powers)
    
    # which numbers are they?
    numbers = []
    for power in reversed(digit_powers):
        place = base**power
        digit_value = data % place
        digit = digit_value / place
        numbers.append(digit)
        data -= digit_value
        
    return numbers
    
def washers_to_data(numbers):
    return numbers_to_data(numbers, base=4)
    
def data_to_washers(data):
    return data_to_numbers(numbers, base=4)

data_to_numbers(13, base=4)
