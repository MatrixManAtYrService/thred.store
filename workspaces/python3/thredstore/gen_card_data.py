# coding: utf-8
import json
from alphanum import data_to_base64, base64_to_data, data_to_numbers, symbols
from washers import data_to_base4
from collections import OrderedDict
import IPython

symbol_meta = {}
for char in symbols:
    symbol_meta[char] = {}
    base_10 = '{0:0>2}'.format(data_to_numbers(base64_to_data(char))[0])
    base_4 = '{0:0>3}'.format(data_to_base4(base64_to_data(char)))
    base_2 = '{0:0>6}'.format(str(base64_to_data(char)))

    example = ((int(base_10 + 1))**2 + 1) % 64

    symbol_meta[char]['values'] = { 'base_64' : char,
                                    'base_10' : base_10,
                                    'base_4'  : base_4,
                                    'base_2'  : base_2 }
    table = char + ' xor _'
    symbol_meta[char][table] = OrderedDict()
    a = base64_to_data(char)
    for char2 in symbols:
        b = base64_to_data(char2)
        val =  a ^ b
        if data_to_numbers(b)[0] == example:
            # one cell will be special
            symbol_meta[char][table]["<operand2>" + char2 + "</operand2>"] = "<result>" + data_to_base64(val) + "</result>"
        symbol_meta[char][table][char2] = data_to_base64(val)

with open('cards_data.json', 'w+') as f:
    f.write(json.dumps(symbol_meta, indent=2))
    f.write('\n')
