import hashlib


def passToHash(password):
    """ Those functions accept only byte arrays and output objects.
        It is neccesary to use str.encode() to change from string to byte arrays
        and hexdigest() to get from object to hex value."""
    return hashlib.sha256(str.encode(password)).hexdigest()


def compareHashAndGuess(hashed, guess):
    if hashed == guess:
        return True
    else:
        return False


def genGuess():
    return "5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8".lower()


def main():
    password = "password"
    # Correct hash : "5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8"

    hashed = passToHash(password)
    guess = genGuess()
    compResult = compareHashAndGuess(hashed, guess)

    pstr = f"Password : {password}\nhashed : {hashed} \
        \nguess  : {guess}\ncompResult : {compResult}"
    print(pstr)


if __name__ == '__main__':
    """Runs main if program is run standalone"""
    main()
