def add(x, y):
    return x+y


def length(x):
    return len(x)


def substr(x, i):
    return x[i:]

if __name__ == "__main__":
    print(substr("Hello",2)=="llo")
    print(substr("Hello",2)!="lo")