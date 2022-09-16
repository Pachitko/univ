
import re

regex = re.compile("[,.!?\n\0]*", re.IGNORECASE)

with open("data.txt", "r") as inputFile:
    text = inputFile.read().lower()
    text = regex.sub("", text)
    words = set(text.split(" "))
    with open("count.txt", "w") as outputFile:
        words = sorted(words)
        outputFile.write("\n".join(words))
