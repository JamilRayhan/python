def hof(fn):
    fn()


def greet():
    print("Hello World!")


def hello():
    print("Hello you!!")


hof(hello)
