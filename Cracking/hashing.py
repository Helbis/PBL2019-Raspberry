#!/usr/bin/env python
try:
    from myHashUtils import *
except ImportError:
    print("ImportError in " + __file__)
    exit(1)


def main():
    password = "password"
    # Correct hash : "5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8"

    hashed = passToHash(password)
    guess = genGuess()
    compResult = compareHashAndGuess(hashed, guess)

    pstr = "Password : {}\nhashed : {} \
        \nguess  : {}\ncompResult : {}".format(password, hashed, guess, compResult)
    print(pstr)


if __name__ == '__main__':
    """Runs main if program is run standalone"""
    main()
