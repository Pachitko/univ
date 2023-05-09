
fileName = input("Enter a file name: ")

f = None
try:
    f = open(fileName, "r")
    n = int(f.readline())
    for _ in range(n):
        line = f.readline().rstrip(" \0\n")
        if line:
            print(line)
except IOError as e:
    print(e)
finally:
    if f:
        f.close()
