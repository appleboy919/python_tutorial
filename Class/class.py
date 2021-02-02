class Dog:
    sound = 'woof-woof'
    legs = 4

    def bark(self):
        print(self.sound)

    def how_many_legs(self):
        print(f'Has {self.legs} legs')


def main():
    moly = Dog()
    moly.bark()
    moly.how_many_legs()


if __name__ == '__main__':
    main()


### Note ###

# first argument(usually named as 'self') is a reference to the object of a class
# . dereferences the object
