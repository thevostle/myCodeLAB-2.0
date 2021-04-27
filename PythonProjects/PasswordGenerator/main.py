import string
from random import sample, choice

def getChars():
    s = getSettings()
    chars = string.ascii_lowercase
    if (s['UseNumbers?']):
        chars += string.digits
    if (s['UseUppercase?']):
        chars += string.ascii_uppercase
    if (s['UseSpecial?']):
        chars += "!_#?/"
    return chars

def generatePassword():
    s = getSettings()
    return ''.join([choice(getChars()) for i in range(s['Length'])])

def getSettings():
    settings = {
        'Length': 10,
        'UseNumbers?': True,
        'UseUppercase?': True,
        'UseSpecial?': True,
        }
    return settings


if __name__ == '__main__':
    print(generatePassword())
