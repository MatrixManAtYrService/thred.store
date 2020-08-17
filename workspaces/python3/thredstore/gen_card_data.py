# coding: utf-8
import json
from alphanum import (
    data_to_base64,
    base64_to_data,
    data_to_numbers,
    numbers_to_data,
    symbols,
)
from washers import data_to_base4
from collections import OrderedDict
from copy import deepcopy
import random
import IPython

orange = "#ff5b03"
purple = "#cba6e3"
teal = "#61c5e6"

seed = 1

shuffled_symbols = deepcopy(symbols)
random.Random(seed).shuffle(shuffled_symbols)

symbols_meta = []
coincidences = []
for subject_char, object_char in zip(symbols, shuffled_symbols):

    print('subject: ', subject_char,
          'object: ', object_char)

    symbol_meta = {}
    symbol_meta['symbol'] = subject_char

    # front stuff
    base_10 = "{0:0>2}".format(data_to_numbers(base64_to_data(subject_char))[0])
    base_4 = "{0:0>3}".format(data_to_base4(base64_to_data(subject_char)))
    base_2 = "{0:0>6}".format(str(base64_to_data(subject_char)))

    symbol_meta["front"] = {
        "base_64": {"val": subject_char},
        "base_10": {"val": base_10},
        "base_4": {"val": base_4},
        "base_2": {"val": base_2},
        "washers": {"val": base_4},
    }

    symbol_meta["back"] = []

    def cell_for(subj_char, output_char):

        val = {"left": subj_char, "right": output_char, "middle": False}

        # display in middle:
        # c + o = s
        #     o = s - c
        # c : card char
        # o : object char (randomly chosen to be an example for this card)
        # s : sum/subctraction
        if output_char == object_char:
            c = data_to_numbers(base64_to_data(subj_char))[0]
            o = data_to_numbers(base64_to_data(output_char))[0]
            s = data_to_base64(numbers_to_data([c + o % 64]))[0]
            val["middle"] = {"left": o, "right": s}

        return val

    a = base64_to_data(subject_char)
    for char2 in symbols:
        b = base64_to_data(char2)
        s = (a + b) % 64
        s_char = data_to_base64(s)
        symbol_meta["back"].append(cell_for(subject_char, s_char))

    symbols_meta.append(symbol_meta)


with open("cards_data.json", "w+") as f:
    f.write(json.dumps(symbols_meta, indent=2, sort_keys=True))
    f.write("\n")
