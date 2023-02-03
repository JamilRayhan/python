def hof(fn):
    print(fn.__name__)
    fn()


def greet():
    print("Hello World!")


def hello():
    print("Hello you!!")


# hof(hello)

li = [1, 2, 3, 4, 5, 6]


def myFilter(fn, l):
    newL = []
    for i in l:
        if fn(i):
            newL.append(i)
    return newL


newList = list(filter(lambda x: x % 2 == 1, li))
print(newList)
