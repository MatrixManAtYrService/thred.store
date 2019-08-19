# coding: utf-8
import operator
from functools import reduce
from itertools import cycle, islice

oneway = { 'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 
           'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 
           'X': 23, 'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 
           'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44,
           't': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50, 'z': 51, '0': 52, '1': 53, '2': 54, '3': 55,
           '4': 56, '5': 57, '6': 58, '7': 59, '8': 60, '9': 61, '+': 62, '/': 63} 
           
otherway = { v: k for k, v in oneway.items() }

def show(l):
    if type(l[0]) == str:
        print(l)
    else:
        print(', '.join(['[{:02d}]'.format(i) for i in l]))
        
def as_intlist(string):
    return [ oneway[c] for c in string ]
    
def as_string(intlist):
    result = ''
    for val in intlist:
       result += otherway[val]
    return result

def combine(given_strings):

    used_chars = []

    # keep the string of longest length
    # circularly repeat shorter one so all strings are same length
    maxlen = max(map(len,given_strings))
    fixed_len_strings = []
    for string in given_strings:
        newstring = ""
        for char in  islice(cycle(string), maxlen):
            newstring += char
            used_chars.append(char)
        fixed_len_strings.append(newstring)

    # print the map
    printed_chars = set()
    for char in used_chars:
        if char not in printed_chars:
            printed_chars.add(char)
            print("{} = {}".format(char, oneway[char]))
    print()
    
    # print the strings
    for string, intlist in zip(given_strings, map(as_intlist, given_strings)):
       print("'{}' = ".format(string), end='')
       show(intlist)
    
    # convert them to lists of integers
    intlists = []
    for string in fixed_len_strings:
       intlist = as_intlist(string)
       intlists.append(intlist)
    print()
       
    # print a summary
    print(' XOR '.join(map(lambda x: "'{}'".format(x), fixed_len_strings)))
       
    # both represent, and calculate the xor
    expansion = []
    evaluation = []
    for place in zip(*intlists):
        expansion.append(' ^ '.join(map(lambda x : f'{x:02d}',place)))
        val = reduce(operator.xor, place)
        evaluation.append(val)
    print(' = ', end='')
    show(expansion)
    print(' = ', end='')
    show(evaluation)
    
    # turn the result back into a string
    print("'{}'".format(as_string(evaluation)))
    
    
