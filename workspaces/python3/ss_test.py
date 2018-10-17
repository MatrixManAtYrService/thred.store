# coding: utf-8
from spaced_symbols import numbers_to_washers as n2w
from spaced_symbols import washers_to_numbers as w2n
from base26 import letters_to_numbers as l2n
from base26 import numbers_to_letters as n2l

message = 'zebras'
print("encoding...")
print("letters:", message)
print(" base26:", l2n(message))
print("washers:", n2w(l2n(message)))
print("...done")

# output:

# message: zebra
#  base26: [26, 5, 2, 18, 1]
# washers: [[1, 2, 2], [1, 1], [2], [1, 2, 0], [1], [1, 3, 0]]

washers = [[1, 2, 2], [1, 1], [2], [1, 2, 0], [1], [1, 3, 0]]
print("decoding...")
print("washers:", washers)
print(" base26:", w2n(washers))
print("letters:", n2l(w2n(washers)))
print("...done")
