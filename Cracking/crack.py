#!/usr/bin/env python

try:
    from myHashUtils import *
    import pprint, argparse
except ImportError:
    print("ImportError in " + __file__)
    exit(1)


def crack(kwargs):
    """
    crack(kwargs)
    accepts any number of inputs
    and returns correct [key, value] pair or [None, None].
    Compares to the guessed hash
    """

    rainbowTable = {elem : passToHash(elem) for elem in kwargs}
    hashed = genGuess();

    #Scramble the words
    for word in kwargs:
        for word2 in kwargs:
            rainbowTable[word + word] = passToHash(word + word)
            rainbowTable[word + word2] = passToHash(word + word2)
            rainbowTable[word2 + word] = passToHash(word2 + word)

    compCheck = compareHashAndGuess(hashed, rainbowTable)

    i = 0
    for key, value in rainbowTable.items():
        if compCheck[i]:
            return [key, value]
        i += 1
    return [None, None]


def main():
    parser = argparse.ArgumentParser(description="Cracking tool")
    parser.add_argument("Keywords", metavar='K', type=str, nargs='+', help="Keywords that will be used for cracking the hash")
    args = parser.parse_args().Keywords
    # print(args) # DEBUG
    crack(args)


if __name__ == "__main__":
    main()
