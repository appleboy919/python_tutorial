class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'Living thing'
        self._name = kwargs['name'] if 'name' in kwargs else 'No Name'
        self._sound = kwargs['sound'] if 'sound' in kwargs else '(Mute)'

    # provides string representation --> allows to simply use print() function
    def __str__(self):
        return f'Type: {self.type()}\tName: {self.name()}\tSound: {self.sound()}'

    # setter and getter
    def type(self, t=None):
        if t:
            self._type = t
        return self._type

    def name(self, n=None):
        if n:
            self._name = n
        return self._name

    def sound(self, s=None):
        if s:
            self._sound = s
        return self._sound


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print(f'Type: {o.type()}\tName: {o.name()}\tSound: {o.sound()}')


def main():
    # a0 = Animal('Dog', 'Moly', 'Woof-woof')
    # a1 = Animal('Cat', 'Mery', 'Meow')
    # print_animal(a0)
    # print_animal(a1)
    # print_animal(Animal('Human', 'David', 'Hu---man'))
    a1 = Animal(type='Human', name='David', sound='Hu---man')
    print_animal(a1)
    print(a1.sound('Hello!'))
    print_animal(a1)
    a2 = Animal(type='Dog', name='Moly', sound='Woof-woof')
    print_animal(a2)
    a3 = Animal()
    print_animal(a3)
    print('using print function', a1)


if __name__ == '__main__':
    main()

### Note ###
# __init__: constructor which initialize an object
# object variables such as _type, _name, have _, which blocks the users to access these variables directly
