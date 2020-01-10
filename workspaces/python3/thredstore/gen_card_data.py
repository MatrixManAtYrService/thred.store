# coding: utf-8
import json
from alphanum import data_to_base64, base64_to_data, data_to_numbers, symbols
from washers import data_to_base4
from collections import OrderedDict
import IPython

orange = '#ff5b03'
purple = '#cba6e3'
teal = '#61c5e6'

symbol_meta = {}
for char in symbols:
    symbol_meta[char] = {}

    base_10 = '{0:0>2}'.format(data_to_numbers(base64_to_data(char))[0])
    base_4 = '{0:0>3}'.format(data_to_base4(base64_to_data(char)))
    base_2 = '{0:0>6}'.format(str(base64_to_data(char)))

    symbol_meta[char]['front'] = { 'base_64' : { "val" : char, "color" : orange},
                                   'base_10' : { "val" : base_10 },
                                   'base_4'  : { "val" : base_4 },
                                   'base_2'  : { "val" : base_2 },
                                   'washers' : { "val" : base_4 } }

    symbol_meta[char]['back'] = {}
    symbol_meta[char]['back']['center'] = {}

    # cleartext + key = ciphertext
    symbol_meta[char]['back']['center']['top'] = [
        { "val" : char, "color" : orange, "subscript" : "unlocked_padlock" },
        "+",     { "val" : "key",            "background" : purple },
        "=",     { "val" : "locked_padlock", "background" : teal }]

    # cleartext = ciphertext - key

    symbol_meta[char]['back']['center']['bottom'] = [
                 { "val" : "unlocked_padlock", "background" : purple },
        "=",     { "val" : "key",              "background" : teal },
        "-",     { "val" : char,   "color" : orange, "subscript" : "key" }]

    symbol_meta[char]['back']['left_column'] = { "background" : purple }
    symbol_meta[char]['back']['right_column'] = { "background" : teal }
    symbol_meta[char]['back']['rows'] = []

    a = base64_to_data(char)
    for char2 in symbols:
        b = base64_to_data(char2)
        s =  (a + b) % 64
        s_char = data_to_base64(s)
        symbol_meta[char]['back']['rows'].append([char2, s_char])

with open('cards_data.json', 'w+') as f:
    f.write(json.dumps(symbol_meta, indent=2))
    f.write('\n')
