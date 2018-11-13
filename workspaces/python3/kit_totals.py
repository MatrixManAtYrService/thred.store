import base26
import base4
import random
from washerfrequency import frequency
import numpy as np

words = 13 # 12 seed, 1 to identify which currency
washers_per = 3
words_per = 2
washer_d = 1.15 # mm
fender_d = 1.45
nut_d = 3
extra_space = 10

fenders_per = words_per + 1

import IPython
def thread_length(words):
    val = len("".join(words)) * washers_per * washer_d \
            + fenders_per * fender_d \
            + 2 * nut_d \
            + extra_space
    #IPython.embed()
    return val

def divide_across_bolts(words):
    for i in range(0, len(words), words_per):
        yield words[i:i + words_per]


with open("bip39.txt", "r") as f:
    words = set(map(lambda x : x.strip(), f.readlines()))

usage_across_messages = {}

for i in range(5000):
    choice = random.sample(words, 13)
    message = ''.join(choice)
    for washer, freq in frequency(message).items():
        usage_across_messages.setdefault(washer, [])
        usage_across_messages[washer].append(freq)

    bolts = divide_across_bolts(choice)
    for bolt in bolts:
        if len(bolt) == words_per:
            usage_across_messages.setdefault("mm", [])
            usage_across_messages["mm"].append(thread_length(bolt))

for washer, frequencies in usage_across_messages.items():
    print("washer {}: ".format(washer))
    print("          average consumption:", np.percentile(frequencies, 50))
    print("  99.5 percentile consumption:", np.percentile(frequencies, 99.5))
    print("              max consumption:", max(frequencies))

