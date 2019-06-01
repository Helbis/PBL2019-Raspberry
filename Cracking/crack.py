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
    and prints out hashes for combinations of them.
    Compares to the guessed hash
    """

    rainbowTable = {elem : passToHash(elem) for elem in kwargs}
    hashed = genGuess();
    # print("hashed = {}\ntype : {}".format(hashed, type(hashed))) # DEBUG

    for word in kwargs:
        for word2 in kwargs:
            rainbowTable[word + word] = passToHash(word + word)
            rainbowTable[word + word2] = passToHash(word + word2)
            rainbowTable[word2 + word] = passToHash(word2 + word)

    compCheck = compareHashAndGuess(hashed, rainbowTable)
    print("hash value : {}\n".format(hashed))

    if any(compCheck):
        print("Match found!")
    else:
        print("No match found\nExiting...")
        exit(0)

    # print("Comparision check : {}".format(compCheck))

    i = 0
    for key, value in rainbowTable.items():
        if compCheck[i]:
            print("==> {} : {} : {}".format(compCheck[i], key, value))
        else:
            print("{} : {} : {}".format(compCheck[i], key, value))
        i += 1

    # pprint.pprint(rainbowTable, width=1)
    # print("Lenght = {}".format(len(rainbowTable.keys()))) # DEBUG


def main():
    parser = argparse.ArgumentParser(description="Cracking tool")
    parser.add_argument("Keywords", metavar='K', type=str, nargs='+', help="Keywords that will be used for cracking the hash")
    args = parser.parse_args().Keywords
    # print(args) # DEBUG
    crack(args)


if __name__ == "__main__":
    main()
