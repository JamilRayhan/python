def myWrapper(fn):
    def test():
        print("Before")
        fn()
        print("After")

    return test


@myWrapper
def hello():
    print("Hello World!")


hello()
