import bits

# just bits
def washers_to_data(washers):
    return bits.numbers_to_data(washers, base=4)

def data_to_washers(data):
    return bits.data_to_numbers(data, base=4)

# spaced symbols representation
def washer_segments_to_numbers(washer_segments):
    numbers = []
    for segment in washer_segments:
        numbers.append(int(washers_to_data(segment)))
    return numbers

def numbers_to_washer_segments(numbers):
    washers = []
    for number in numbers:
        washers.append(data_to_washers(number))
    return washers
