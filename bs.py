from random import choice

def generateBs():
    part1 = ["Found nothing, ", "Empty, "]
    part2 = ["just ", "except for "]
    part3 = ["words", "more words"]
    return (choice(part1) + choice(part2) + choice(part3))

if __name__ == "__main__":
    print(generateBs())