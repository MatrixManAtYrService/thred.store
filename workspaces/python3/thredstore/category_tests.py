from functools import reduce
from morphism_tests import assert_equal
import alphanum
import washers

# just pretty printing stuff
class Step:
    def __init__(self, preimage, func, image):
        self.preimage = str(preimage)
        self.func_name = " --" + func.__name__ + "--> "
        self.image = str(image)

# just pretty printing stuff
class PathReport:
    def __init__(self):
        self.steps = []

    def add(self, preimage, func_name, image):
        self.steps.append(Step(preimage, func_name, image))

    def go(self):
        col_1_width = max(map(lambda x: len(x.preimage), self.steps))
        col_2_width = max(map(lambda x: len(x.func_name), self.steps))
        col_3_width = max(map(lambda x: len(x.image), self.steps))

        for step in self.steps:
            preimage = step.preimage
            func_name = step.func_name
            image = step.image
            print(f'{preimage: >{col_1_width}} '
                    + f'{func_name: ^{col_2_width}}'
                    + f' {image: <{col_3_width}}')

# given n morphisms, run the object through all of them and ensure it is unchanged afterwards
def commute_test(obj, *morphisms):

    # populate these during test
    results = PathReport()

    # given two morphisms, return a composition that supplies a message about the intermediate result
    def compose_with_message(f, g):
        def composition(x):
            results.add(x, g, g(x))
            results.penultimate_obj = g(x)
            return f(g(x))
        composition.__name__ = f.__name__
        return composition

    # build a composition for all morphisms
    composition = reduce(compose_with_message, reversed(morphisms))

    # print the path
    image = composition(obj)
    results.add(results.penultimate_obj, composition, image)

    results.go()

    # look for changes
    assert_equal(obj, image)
    print()

def main():

    # ZEBRAS --base64_to_numbers--> [26, 5, 2, 18, 1, 19] --numbers_to_base64--> ZEBRAS
    commute_test('ZEBRAS', alphanum.base64_to_numbers,
                           alphanum.numbers_to_base64 )

    commute_test('ZEBRAS', alphanum.base64_to_data,
                           washers.data_to_base4 )

    commute_test('ZEBRAS', alphanum.base64_to_numbers,
                           alphanum.numbers_to_data,
                           washers.data_to_base4,
                           washers.base4_to_data,
                           alphanum.data_to_numbers,
                           alphanum.numbers_to_base64 )


    commute_test('THRED', alphanum.base64_to_data,
                          washers.data_to_base4,
                          washers.base4_to_data,
                          alphanum.data_to_base64 )

    commute_test('STORE', alphanum.base64_to_data,
                          washers.data_to_base4,
                          washers.base4_to_data,
                          alphanum.data_to_base64 )

if __name__ == "__main__":
    main()
