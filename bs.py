from random import choice

def generateBs():
    returnString = ""
    parts = [["Found nothing, ", "Empty, "], ["just ", "except for "], ["words", "more words"]]
    for part in parts:
        returnString += choice(part)
    return returnString

if __name__ == "__main__":
    print(generateBs())