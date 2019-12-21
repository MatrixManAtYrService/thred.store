import bits

# base64, see RFC4648
symbols = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']

def numbers_to_data(number_list):
    return bits.numbers_to_data(number_list, base=64)

def data_to_numbers(number_list):
    if number_list:
        return bits.data_to_numbers(number_list, base=64)
    else:
        return [0]

def base64_to_numbers(string):
    number_list = []
    for char in string:
        number_list.append(symbols.index(char))
    return number_list

def numbers_to_base64(number_list):
    string = ""
    for number in number_list:
        try:
            string += symbols[number]
        except IndexError as e:
            raise ValueError("{} is not one of {}".format(number, symbols)) from e
    return string

def base64_to_data(string):
    return numbers_to_data(base64_to_numbers(string))

def data_to_base64(data):
    return numbers_to_base64(data_to_numbers(data))
