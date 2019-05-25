#!/usr/bin/env python

from myHashUtils import *
import pprint, argparse


def crack(kwargs):
    """
    crack(*kwargs)
    accepts any number of inputs
    and prints out hashes for combinations of them.
    Compares to the guessed hash
    """

    rainbowTable = {elem : passToHash(elem) for elem in kwargs}
    hashed = genGuess();
    # print(f"hashed = {hashed}\ntype : {type(hashed)}") # DEBUG
    print(f"hash value : {hashed}")

    for word in kwargs:
        for word2 in kwargs:
            rainbowTable[word + word] = passToHash(word + word)
            rainbowTable[word + word2] = passToHash(word + word2)
            rainbowTable[word2 + word] = passToHash(word2 + word)

    compCheck = compareHashAndGuess(hashed, rainbowTable)
    print(f"Comparision check : {compCheck}")

    # print(f"Lenght = {len(rainbowTable.keys())}") # DEBUG
    pprint.pprint(rainbowTable, width=1)


def main():
    parser = argparse.ArgumentParser(description="Cracking tool")
    parser.add_argument("Keywords", metavar='K', type=str, nargs='+', help="Keywords that will be used for cracking the hash")
    args = parser.parse_args()
    print(args)
    # crack(args)


if __name__ == '__main__':
    main()
