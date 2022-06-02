import locale
from random import choice

def generateBs(locale):
    returnString = ""
    locales = {
        "en" : [["Found nothing, ", "Empty, "], ["just ", "except for "], ["words", "more words"]]
    }
    if locale not in locales:
        return ""
    parts = locales[locale]
    for part in parts:
        returnString += choice(part)
    return returnString

if __name__ == "__main__":
    locale = input("Insert locale: ")
    generatedString = generateBs(locale)
    while (not generatedString):
        locale = input("Invalid locale, try again: ")
        generatedString = generateBs(locale) 
    print(generatedString)