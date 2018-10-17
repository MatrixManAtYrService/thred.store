from alphabase import washers_to_data, data_to_washers

def washers_to_numbers(washers):
    numbers = []
    for washer in washers:
        numbers.append(washers_to_data(washer))
    return numbers

def numbers_to_washers(numbers):
    washers = []
    for number in numbers:
        washers.append(data_to_washers(number))
    return washers
