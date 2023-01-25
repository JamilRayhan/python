from functools import reduce

li = [1, 2, 3, 4, 2, 3, 4]


def func(x, y):
    return x + y


sum = reduce(lambda x, y: x + y, li)
print(sum)
