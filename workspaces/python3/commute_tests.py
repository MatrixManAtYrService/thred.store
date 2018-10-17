# coding: utf-8
from functools import reduce
import base26
import spaced_symbols

# given n morphisms, run the object through all of them and ensure it is unchanged afterwards
def commute_test(obj, *morphisms):

    # given two morphisms, return a composition that prints the intermediate result
    def compose_with_message(f, g):
        def composition(x):
            print(g.__name__ + "-->", g(x), end=' ')
            print(" --" + f.__name__ + "-->", end=' ')
            return f(g(x))
        composition.__name__ = g.__name__
        return composition


    print(obj, "--", end='')
    composition = reduce(compose_with_message, reversed(morphisms))
    image = composition(obj)
    print(image)

    if obj == image:
        print("    SUCCESS")
    else:
        print("    FAIL")


commute_test('ZEBRAS', base26.letters_to_numbers,
                       base26.numbers_to_letters )

commute_test([26, 5, 2, 18, 1, 19], base26.numbers_to_letters,
                                    base26.letters_to_numbers )

commute_test('ZEBRAS', base26.letters_to_numbers,
               spaced_symbols.numbers_to_washers,
               spaced_symbols.washers_to_numbers,
                       base26.numbers_to_letters )
