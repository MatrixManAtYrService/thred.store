import base26
import base4
import bits
from bits import Bits

def assert_equal(a, b):
    if a == b:
        print("[SUCCESS]")
    else:
        print("[FAIL: {} != {}]".format(a, b))

def equivalent(a, morphism, b):
    a_image = morphism(a)
    print(a, "--" + morphism.__name__ + "-->", a_image)
    assert_equal(a_image, b)

def base16(func):
    def func2(x):
        return func(x, base=16)
    func2.__name__ = func.__name__ + "_base16"
    return func2

def main():
    equivalent(0, base26.data_to_numbers, [])
    equivalent(1, base26.data_to_numbers, [1])
    equivalent(27, base26.data_to_numbers, [1,1])

    equivalent(1000, base16(bits.data_to_numbers), [3,14,8])

    equivalent(5, base4.data_to_washers, [1,1])
    equivalent(18, base4.data_to_washers, [1,0,2])
    equivalent(26, base4.data_to_washers, [1,2,2])

    equivalent([1,1], base4.washers_to_data, 5)
    equivalent([1,0,2], base4.washers_to_data, 18)
    equivalent([1,2,2], base4.washers_to_data, 26)

    equivalent(Bits(0b11001100), base16(bits.data_to_numbers), [12, 12])

    equivalent([[1]], base4.washer_segments_to_numbers, [1])
    equivalent([[0,0,0]], base4.washer_segments_to_numbers, [0])
    equivalent([[1], [2], [1,2,2]], base4.washer_segments_to_numbers, [1, 2, 26])

if __name__ == "__main__":
    main()