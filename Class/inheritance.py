class Animal:
    # no default value for child classes
    def __init__(self, **kwargs):
        if 'type' in kwargs:
            self._type = kwargs['type']
        if 'name' in kwargs:
            self._name = kwargs['name']
        if 'sound' in kwargs:
            self._sound = kwargs['sound']

    def type(self, t=None):
        if t:
            self._type = t
        try:
            return self._type
        except AttributeError:
            return None

    def name(self, n=None):
        if n:
            self._name = n
        try:
            return self._name
        except AttributeError:
            return None

    def sound(self, s=None):
        if s:
            self._sound = s
        try:
            return self._sound
        except AttributeError:
            return None


class Duck(Animal):     # Duck inherits Animal class
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)

    def swim(self, s):  # Own function
        print(f'{self.name()} is swimming in {s}')


class Dog(Animal):      # Dog inherits Animal class
    def __init__(self, **kwargs):
        self._type = 'dog'
        if 'type' in kwargs:
            del kwargs['type']
        super().__init__(**kwargs)


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print(f'Type: {o.type()}\tName: {o.name()}\tSound: {o.sound()}')


def main():
    a0 = Duck(name='Donald', sound='Kwawk-kwawk')
    a1 = Dog(name='Moly', sound='Woof-woof')
    print_animal(a0)
    print_animal(a1)
    a0.swim('lake')


if __name__ == '__main__':
    main()

# Note
# super().__init__ --> call the parent's constructor
# can extend built-in classes
