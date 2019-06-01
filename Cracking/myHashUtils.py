#!/usr/bin/env python
try:
    import hashlib
except ImportError:
    print("ImportError in " + __file__)
    exit(1)


def passToHash(password):
    """ Those functions accept only byte arrays and output objects.
        It is neccesary to use str.encode() to change from string to byte arrays
        and hexdigest() to get from object to hex value."""
    return hashlib.sha256(str.encode(password)).hexdigest()


def compareHashAndGuess(hashed, guess):
    if isinstance(guess, str):
        if hashed == guess:
            return True
    elif isinstance(guess, dict):
        result = []
        keys = guess.keys()
        values = guess.values()
        for word in guess.values():
            # print(hashed, word) # DEBUG:
            if str(word) == str(hashed):
                result.append(True)
            else:
                result.append(False)
        return result
    else:
        return False


def genGuess():
    """
    password : 5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8
    """
    return passToHash("password")
