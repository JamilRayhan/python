# map function
def func(n):
    return n * n * n


l = [3, 4, 1, 0, 6]

newL = list(map(lambda n: n * n * n, l))  # newL = [n*n*n for n in l]

l = ['Simanta', 'Bohubrihi', 'Dhaka']

l2 = list(map(list, l))

print(l2)
