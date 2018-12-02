import bip39
import alphanum
import washers
import bits
import bip39
from bits import Bits
from copy import deepcopy

def assert_equal(a, b):
    if a == b:
        print("[SUCCESS]")
    else:
        print("[FAIL: {} != {}]".format(a, b))
    print()

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
    equivalent([32], alphanum.numbers_to_data, bits.Bits(32))

    equivalent(0, alphanum.data_to_numbers, [])
    equivalent(1, alphanum.data_to_numbers, [1])
    equivalent(65, alphanum.data_to_numbers, [1,1])


    equivalent(1000, base16(bits.data_to_numbers), [3,14,8])

    equivalent(5, washers.data_to_base4, "11")
    equivalent(18, washers.data_to_base4, "102")
    equivalent(26, washers.data_to_base4, "122")

    equivalent("11", washers.base4_to_data, 5)
    equivalent("102", washers.base4_to_data, 18)
    equivalent("122", washers.base4_to_data, 26)

    equivalent(Bits(0b11001100), base16(bits.data_to_numbers), [12, 12])

    equivalent("1", washers.base4_to_numbers, [1])
    equivalent("000", washers.base4_to_numbers, [0, 0, 0])

    def base_64_to_offset(letters):
        return bip39.numbers_to_offsets(alphanum.base64_to_numbers(letters))

    equivalent('AAAAAAAAAA', base_64_to_offset, [0])
    equivalent('AAAAAAAAAB', base_64_to_offset, [1])
    equivalent('AAAAAAAAABAAAAAAAAA', base_64_to_offset, [1])
    equivalent('AAAAAAAAABAAAAAAAAAC', base_64_to_offset, [1, 2])
    equivalent('//////////', base_64_to_offset, [2047])
    equivalent('///////////////////+', base_64_to_offset, [2047, 2046])

    def offset_by_0(word):
        return bip39.offset_by(word, 0)

    def offset_by_1(word):
        return bip39.offset_by(word, 1)

    def offset_by_2047(word):
        return bip39.offset_by(word, 2047)

    equivalent('abandon', offset_by_0, 'abandon')
    equivalent('abandon', offset_by_1, 'ability')
    equivalent('abandon', offset_by_2047, 'zoo')
    equivalent('bread', offset_by_2047, 'brave')

    mnemonic = ['merit', 'average', 'fragile', 'smart', 'end', 'mom',
                'knock', 'bid', 'era', 'crisp', 'romance', 'grace']

    bitstream = bip39.mnemonic_to_bitstream(mnemonic)

    equivalent(deepcopy(bitstream), bip39.bitstream_to_mnemonic, mnemonic)
    equivalent(mnemonic, bip39.mnemonic_to_bitstream, deepcopy(bitstream))


if __name__ == "__main__":
    main()
