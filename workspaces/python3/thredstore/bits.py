import itertools

# just like an int, except it prints in binary
# no reason to think base 10 is special in this context
class Bits(int):
    def __repr__(self):
        return '{:b}'.format(self)

    def __str__(self):
        return '{:b}'.format(self)

def numbers_to_data(numbers, base=26):
    number = 0
    for i, n in enumerate(reversed(numbers)):
        number += n * (base**i)
    return Bits(number)

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
        numbers.append(digit)
        data -= digit * place
    return numbers
