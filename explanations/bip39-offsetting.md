# A Simplified Model of BIP39-offsetting

## The Simplification

In practice, BIP39-offsetting has a key alphabet of 64^3 values (triples selected from the base64 character set).
The input/output alphabets are 2048 values (selections from a BIP-39 wordlist).
Each offset is a function of a position in the key alphabet raised to the third power modulo 2048.
Since 64^3 % 2048 = 0, mnemonics that start random will offset to just-as-random (by the way, 3 is the lowest power with this property).
Since 64^3 / 2048 = 128, an attacker that compromizes a single pair of input/output offsets still has 128^m candidates to sort through if he wants to guess the offset-key (m is the mnemonic length in words).

Instead of these inconvenient numbers, let's play with a system that functions the same, just smaller:

    key-alphabet: [ '000', '001', '010', '011', '100', '101', '110', '111']
    key-values:   [   0      1      2      3      4      5      6      7  ]

(8 symbols, valued 0 - 7)

    io-alphabet: [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K',  'L',  'M',  'N',  'P',  'Q'  ]
    io-values:   [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15' ]

(16 symbols, valued 1 - 15)

In our simplified case, 8^2 / 16 = 4, so attackers will still have about 5^m key candidates to choose from if they discover an output offset.

## Offset Derivation

Offset derivation starts with a long string that contains characters in the key alphabet, this is called an offset-seed.
Besides the input-mnemonic, this is the only other secret that BIP39-offsetting requires.
Other parameters can be stored somewhere on the blockchain indicated by the input mnemonic.

    o := "10A01 10100B 01 011CDE11 1010000X 101111Y 10110010001"

Remove any characters not in the key alphabet, this is the `cleaned-offset-seed`.

    c := "1001101000101111101000010111110110010001"

Key derivation takes four parameters: hide (_h_), _hidden-omit_ (_oh_), _hidden-take_ (_th_), and _hidden-skip_ (_sh_).
_h_ is used in conjunction with the offset-seed to determine _peek_ (_p_) which is used to un-hide _oh_, _th_, and _sh_ thereby obtaining _o_, _t_, and _s_.
_o_, _t_, and _s_ are used to determine which the subsets of the cleaned-offset-seed will be used to calculate the offsets.

### Example 1

_h_ = 7
_oh_ = 7
_th_ = 37
_sh_ = 11

##### Unhide

Use the first _h_ characters of the cleaned_offset-seed to compute the param key (_p_).
In our simplified system, the io-alphabet characters are base-2 encoded, so we interpret them as binary.
In an actual BIP39-offsetting scenario, the offset-seed characters are assumed to be base-64, so they should be interpreted that way instead.

> _p_ :=(1001101)_2 = (77)_10

To unhide the other parameters...

> _p_ % _oh_ = _o_
> _p_ % _th_ = _t_
> _p_ % _sh_ = _s_

so...

> 77 % 7 = _o_ = 0
> 77 % 37 = _t_ = 3
> 77 % 11 = _s_ = 0

##### Offset Calculation

To determine the offsets, start counting characters from the front of the offset-seed.
The algorithm below will tell you which characters to take:

1. skip _h_ characters
2. skip _o_ characters
3. take _t_ characters, this will be a symbol in the key-alphabet, it's corresponding key-value is the offset
4. skip _s_ characters
5. go to step 3

Given the cleaned-offset-seed above, the parameters _o_ = 0, _t_ = 3, and _s_ = 0 yeild these offsets:

    1001101   **000** **101** **111** **101** **000** **010** **111** **110** **110** **010** **001**
    [            0       5       7       5       0       2       7       6       6       2       1 ]

So the offsets for parameters 0,3,3 are [0,5,7,5,0,2,7,6,6,2,1].
Note that a longer key would have given us more offsets.

Suppose that the input mnemonic is:

    [ 'Q','C','J' ]

Then the corresponding values are:

    [ 7, 3, 9 ]

Since our io-alphabet has 16 symbols, we add the offset to the above values modulo-16 and convert back to symbols:

    output_mnemonic = fix_checksum(input_mnemonic + offsets)
                    = fix_checksum([ 7 + 0, 3 + 5, 9 + 7 ])
                    = fix_checksum([ 7, 8, 0 ])
                    = fix_checksum(['G', 'H', 'A'])

This mnemonic contains a checksum which has been invalidated by the offset.
It is not strictly necessary to fix the checksum.
Whether or not we do so...


TODO: add a final "fixes the checksum" offset as a parameter

### Example 2

_h_ = 9
_oh_ = 9
_th_ = 3
_sh_ = 2
