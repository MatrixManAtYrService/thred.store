import itertools

def numbers_to_data(numbers, base=26):
    number = 0
    for i, n in enumerate(reversed(numbers)):
        number += n * (base**i)
        print(base**i,n,number)
    return number

def data_to_numbers(data, base=26):

    # how many numbers will it take?
    counter = itertools.count(start=0)
    places = []
    while True:
        place = base**next(counter)
        if place > data:
            break
        else:
            places.append(place)

    # which numbers are they?
    numbers = []
    for place in reversed(places):
        digit = int(data / place)
        numbers.insert(1,digit)
        data -= digit * place
        print(place, digit, data)
    return numbers

def washers_to_data(numbers):
    return numbers_to_data(numbers, base=4)

def data_to_washers(data):
    # most significant bit goes left
    return data_to_numbers(data, base=4)
