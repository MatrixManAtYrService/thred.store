import bip39
from bitstream import BitStream
from copy import deepcopy

def assert_equal(a, b):
    if a == b:
        print("[SUCCESS]")
    else:
        print("[FAIL: {} != {}]".format(a, b))
    print()

daedalus = ['merit', 'average', 'fragile', 'smart', 'end',
        'mom', 'knock', 'bid', 'era', 'crisp', 'romance', 'grace']

# https://iancoleman.io/bip39/#english
ian = [ 'crumble', 'scheme', 'section', 'own', 'fade', 'quote', 'spawn',
        'material', 'jar', 'size', 'earth', 'candy', 'screen', 'uniform', 'educate' ]

def break_fix():

    payload, checksum = bip39.split(ian)
    assert(bip39.checksum_is_good(ian))

    combined = deepcopy(payload)
    combined.write(checksum.read())
    assert(bip39.checksum_is_good(bip39.bitstream_to_mnemonic(combined)))

def main():
    break_fix()


if __name__ == "__main__":
    main()
