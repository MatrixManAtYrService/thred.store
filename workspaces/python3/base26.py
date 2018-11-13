import bits

def numbers_to_data(number_list):
    return bits.numbers_to_data(number_list, base=26)

def data_to_numbers(number_list):
    return bits.data_to_numbers(number_list, base=26)

def letters_to_numbers(string):
    number_list = []
    for char in string:
        it = ord(char.upper()) - 64
        if it < 1 or it > 26:
            raise ValueError("A to Z doesn't include: " + char)
        number_list.append(it - 1)
    return number_list

def numbers_to_letters(number_list):
    string = ""
    for number in number_list:
        string += chr(number + 1 + 64)
    return string

