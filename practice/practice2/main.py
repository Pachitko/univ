import csv
import re

allBooks = []
#   0    1      2       3      4
# isbn|title|author|quantity|price
with open("books.csv", 'r') as booksCsv:
    csvReader = csv.reader([str.replace(line, "|", ",") for line in booksCsv])
    for row in csvReader:
        allBooks.append(row)


def getBooks(bookName):
    return [b for b in allBooks if re.search(bookName, b[1], re.IGNORECASE)]


def getTotal(books, numToAdd, threshold):
    summuries = [(b[0], int(b[3]) * float(b[4])) for b in books]
    withAddition = [(s[0], f"{s[1] + (numToAdd if s[1] < threshold else 0):.2f}")
                    for s in summuries]
    return withAddition


# [('111-1-11111-111-1', '1.10'),
# ('333-3-33333-333-3', '9.90'),
# ('444-4-44444-444-4', '17.60'),
# ('555-5-55555-555-5', '27.50'),
# ('666-6-66666-666-6', '39.60')]
print(getTotal(getBooks("oK"), 0, 0))

# [('111-1-11111-111-1', '6.10'),
# ('333-3-33333-333-3', '14.90'),
# ('444-4-44444-444-4', '22.60'),
# ('555-5-55555-555-5', '27.50'),
# ('666-6-66666-666-6', '39.60')]
print(getTotal(getBooks("oK"), 5, 20))
