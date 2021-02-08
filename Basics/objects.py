class Dog:
    sound = "Woof-Woof"
    walking = "Walks like a dog"

    def bark(self):
        print(self.sound)

    def walk(self):
        print(self.walking)


def main():
    moly = Dog()
    moly.bark()
    moly.walk()


if __name__ == "__main__":
    main()


### NOTE ###
# 1: self is a reference keyword for object
