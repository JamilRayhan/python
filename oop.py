def add(x,y):
    return x+y


class A:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello From class A")


class B:
    def __init__(self, job):
        self.job = job


class C(A, B):
    def __init__(self, name, job):
        A.__init__(self, name)
        B.__init__(self, job)

    def hello(self):
        A.hello(self)
        print(f"{self.name} is a {self.job}")


obj = C("Jamil", "Student")
obj.hello()
