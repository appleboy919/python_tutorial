class Animal:
    # def __init__(self, type, name, sound):
    # self._type = type
    # self._name = name
    # self._sound = sound

    # using **kwargs with default values
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'Living thing'
        self._name = kwargs['name'] if 'name' in kwargs else 'No Name'
        self._sound = kwargs['sound'] if 'sound' in kwargs else '(Mute)'

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
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
    a2 = Animal(type='Dog', name='Moly', sound='Woof-woof')
    print_animal(a2)
    a3 = Animal()
    print_animal(a3)


if __name__ == '__main__':
    main()

### Note ###
# __init__: constructor which initialize an object
# object variables such as _type, _name, have _, which blocks the users to access these variables directly
