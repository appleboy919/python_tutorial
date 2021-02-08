class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + someString)


class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")

    def method2(self, someString):
        print("another Class method2 ")


def main():
    # instantiate a class
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()  # inherited method
    c2.method2("This is a new string")  # override method


if __name__ == "__main__":
    main()


# Note
# 1 "self" == "this" in c/java
# 2 No need to supply self keword (automatically handled by run time)
