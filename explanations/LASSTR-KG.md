# LASSTR-KG

This document describes a key derivation algorithm.  It generates secret strings of characters in the Base 64 Alphabet (see RFC 4648) for cryptographic use. The algorithm aims to have the following properties:

## Low Arithmetical Sophistication

Both the computational and theoretical components of the algorithm should be simple enough that a typical high school graduate should be able to:

    - Start with entropy sources (dice, a dictionary, and an arbitrary book) and make the key components for a new keystream.
    - Start with pencil, paper, and the key components, use them to generate the keystream, and subsequently use it to encrypt a message.
    - Be reasonably confident that no mathematical backdoors exists that undermine the strength of the encrypted message.

## Socially Triggered Recovery

This means that a given keystream can be re-derived from components which can be distributed in various ways to support various recovery situations:

    - The primary keyholder is dead or incapactated, but has provided components to his deputies so that they can derive the keystream in such cases.
    - The primary keyholder is deriving a key under duress, and wants the under-duress key to uncover different messages

LASSTR-KG is intended to generate keys which encrypt messages that go into a message-storage scheme: DGOOSECHASE-MS.
On its own, the only scenario where deputies can derive the keystream is the one where they are all present.
Support for n-of-m-surviving-deputies scenarios requires proper implementation of DGOOSECHASE-MS.
Similarly, an under-duress key will hard to pass of as authentic unless details in that protocol are followed.

# Concepts

Below are some related concepts and descriptions of how they relate to LASSTR-KG.

## XOR Cipher

### How it works

Given a key alphabet with 64 characters and cleartext alphabet also with 64 characters, simple character-wise XOR can be used to encode a message.

From the base64 alphabet:

    K = 10
    e = 30
    y = 50
    m = 38
    s = 44
    a = 26
    g = 32

A key and a message:

    'Key' = [10], [30], [50]
    'message' = [38], [30], [44], [44], [26], [32], [30]

XOR them (cycle the shorter string):

    'KeyKeyK' XOR 'message'
      = [10 ^ 38], [30 ^ 30], [50 ^ 44], [10 ^ 44], [30 ^ 26], [50 ^ 32], [10 ^ 30]
      = [44], [0], [30], [38], [4], [18], [20]
      = 'sAemESU'

To decrypt, XOR the key again:

    'KeyKeyK' XOR 'sAemESU'
      = [10 ^ 44], [30 ^ 00], [50 ^ 30], [10 ^ 38], [30 ^ 04], [50 ^ 18], [10 ^ 20]
      = [38], [30], [44], [44], [26], [32], [30]
      = 'message'

### Relevance

Appropriated features:

- The base64 alphabet makes it easy to correlate a symbol with a numerical value.
- The cypher is simple.
- Order doesn't matter.
- If you have multiple keys, you can stack them.
- Single-character mistakes only corrupt that character in the result, which is helpful for finding mistakes in pencil-and-paper computations.

Another Example:

    'KeyA' = [10], [30], [50], [00]
    'BKey' = [01], [10], [30], [50]
    'themessage' = [45], [33], [30], [38], [30], [44], [44], [26], [32], [30]

    'KeyAKeyAKe' XOR 'BKeyBKeyBK' XOR 'themessage'
      = ['10 ^ 01 ^ 45', '30 ^ 10 ^ 33', '50 ^ 30 ^ 30', '00 ^ 50 ^ 38', '10 ^ 01 ^ 30', '30 ^ 10 ^ 44', '50 ^ 30 ^ 44', '00 ^ 50 ^ 26', '10 ^ 01 ^ 32', '30 ^ 10 ^ 30']
      = [38], [53], [50], [20], [21], [56], [00], [40], [43], [10]
      = 'm1yUV4AorK'

    'KeyAKeyAKe' XOR 'm1yUV4AorK' XOR 'BKeyBKeyBK'
      = ['10 ^ 38 ^ 01', '30 ^ 53 ^ 10', '50 ^ 50 ^ 30', '00 ^ 20 ^ 50', '10 ^ 21 ^ 01', '30 ^ 56 ^ 10', '50 ^ 00 ^ 30', '00 ^ 40 ^ 50', '10 ^ 43 ^ 01', '30 ^ 10 ^ 10']
      = [45], [33], [30], [38], [30], [44], [44], [26], [32], [30]
      = 'themessage'

## One Time Pad

### How it works

In the above examples of XOR cyphers, you'll notice key strings 'KeyA', 'BKey', and 'Key' were too short to cover the message.
This exposes the cypher to statistical attacks.
Better would be to use a totally random key as long as the message.

 message:

    "A box without hinges, key, or lid,
    Yet golden treasure inside is hid,"

 key:

    v/QMTFY7eK42cfyGe+R+jm4JNcX0wvT1M0iQV41DhC9AVM8BK21ff

 result:

    'AboxwithouthingeskeyorlidYetgoldentreasureinsideishid' XOR 'v/QMTFY7eK42cfyGe+R+jm4JNcX0wvT1M0iQV41DhC9AVM8BK21ff'
     = vk49jn1a2kVX+4SYyaPMLNdrQEJZQH2oSTP7LiZtKcfn5uhfoaU9C

If you created a document with a very long string of randomness, and then kept it for later, you could take keys from that document that are a as long as your message.
If you take care to cross out each symbol as it was used--then that document would be called a one-time-pad.
It will resist cryptalaysis quite nicely, but nobody is going to remember that key--which means you have to write it down.

### Relevance

If somebody finds a one-time pad, they now know you have secrets to keep--which might not be good if they're willing to use violence against you--so LASSTR-KG doesn't use a one time pad.
But it uses something close.
Go to a library, open a random book to a random page, and start reading characters from the top.
Here you have (almost) a one-time-pad, but which is easy to pass-off as something else.
You can even lose it, and as long as you can find a copy of that book again, all you need to remember is the page number.

Such an encoding would look like this.

 message:

    "A box without hinges, key, or lid,
    Yet golden treasure inside is hid,"

 key:

    "Let's look for objects C for which 'C * C = C.' This asks: Which objects..."

 result:

AboxwithouthingeskeyorlidYetgoldentreasureinsideishid
LetslookforobjectsCforwhichCCCThisasksWhichobjectsCha

    'AboxwithouthingeskeyorlidYetgoldentreasureinsideishid' XOR 'LetslookforobjectsCforwhichCCCThisasksWhichobjectsCha'
     = LFFdVKFF3GGJ5E+CBIctAAVD/E/viq288L3H626PJCDP3BDCPAjDH

LASSTR-KG does something like this--except it is designed to be tolerant of minor differences.
It would be problematic to encode a message starting with page 50 of the paperback, and attempt to decode that message with page 50 of the hardcover.

A couple things to notice:
    - In my example above I just ignored characters that aren't in the Base64 alphabet, LASSTR-KG does this too.
    - A selection from a random book would not be random, but would make sense in the author's language.

In the example above, the lack-of-randomness deficiency happens to be visible in the cyphertext---notice that the only three consecutive lowercase letters 'viq' in the cyphertext happen to line up with the only three consecutive uppercase letters 'CCC' in the key.
This tells us that excerpts from books, however long, are not random enough to be used alone--which is why LASSTR-KG uses a second key component.

## BIP-39

### How it works

BIP-39 is a list of words.  Secrets are made by selecting several of them in sequence.  An example BIP-39 secret looks like this:

    police mercy swing track brown noise wrong zoo ladder custom face

The nice thing about this is that each word acts as its own tiny error correction scheme, consider this phrase:

    polrce meqcy zwing tracw brlwn moise erong zio lawder mustom race

I have inserted an error into each word, but if you consult the BIP-39 wordlist, you'll be able to spot and correct every error except for one.
As it turns out, both 'face' and 'race' are BIP-39 words.
Sometimes you get unlucky.
Still with a bit of thought (and code, propbably), you could reduce the number of keys that are worth trying from "all of them" to just a couple hundred.

### Relevance

As it is used in bitcoin, the indices in the word list are used to come up with a binary value, which is used to derive the bitcoin private key.
LASSTR-KG doesn't use the BIP-39 wordlist because encryption is done character-wise, not via blobs of binary.
We don't want an attacker to somehow know that a key uses 'pr' and then have reason to further guess '-actice' just because 'practice' is a BIP-39 word.

But we do want similar error correcting capabilities, so for one key-component, we will also be chosing words from a list--though to avoid predictability, it will be a much larger list.
Using dice to choose pages numbers from a dictionary, and then to choose words from the page, I came up with this:

    increment runaround tariff currency mindful topography gimlet carpet restraint echelon snoeshoe platinum

By restricting to 6-letter and longer words, I believe I have reduced the likelihood that a single character error will fail to be identified as an error (and subsequently corrected).

There is a weakness to using character-wise encoding here.  It is similar to the weakness described above regarding true one-time-pads vs excerpts from books

Note for later: https://scilogs.spektrum.de/hlf/mental-cryptography-and-good-passwords/
Keystream is XOR-stacked keys, in four char rounds (to ensure conversion to bytes later)
This helps find errors because cipher errors will appear in four character chunks while key errors will be character wise

