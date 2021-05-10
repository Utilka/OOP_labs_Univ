class DellHello(type):

    def __new__(cls, clsname, bases, dct):
        if "sayHello" in dct:
            del dct["sayHello"]
        return super(DellHello, cls).__new__(cls, clsname, bases, dct)

class testClass(metaclass=DellHello):
    def sayHello(self):
        print("Hello")

    def sayHell(self):
        print("Hell")

if __name__ == '__main__':
    test = testClass()
    print(dir(test))
    test.sayHell()
    test.sayHello()
