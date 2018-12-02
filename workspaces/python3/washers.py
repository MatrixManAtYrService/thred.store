import bits

# base 4
symbols = [ '0', '1', '2', '3' ]

def numbers_to_data(number_list):
    return bits.numbers_to_data(number_list, base=4)

def data_to_numbers(number_list):
    return bits.data_to_numbers(number_list, base=4)

def base4_to_numbers(string):
    number_list = []
    for char in string:
        number_list.append(symbols.index(char))
    return number_list

def numbers_to_base4(number_list):
    string = ""
    for number in number_list:
        try:
            string += symbols[number]
        except IndexError as e:
            raise ValueError("{} is not one of {}".format(number, symbols)) from e

    return string

def base4_to_data(string):
    return numbers_to_data(base4_to_numbers(string))

def data_to_base4(data):
    return numbers_to_base4(data_to_numbers(data))
