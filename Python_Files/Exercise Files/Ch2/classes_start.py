#
# Example file for working with classes
#


class myClass():
    def method1(self):
        print("My class method")

    def method2(self, someString):
        print("myClass method2 " + someString)


class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")

    def method2(self, someString):
        print("anotherClass method2 " + someString)


def main():
    c = myClass()
    c.method1()
    c.method2("StringY!")
    c2 = anotherClass()
    c2.method1()
    c2.method2("String here!")


if __name__ == "__main__":
    main()
