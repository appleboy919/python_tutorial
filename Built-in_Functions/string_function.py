class bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f'repr: the number of bunnies is {self._n} 😷'

    def __str__(self) -> str:
        return f'str: the number of bunnies is {self._n}'


s = 'Hello world.'
print(repr(s))

# repr, str of a class object
x = bunny(47)
print(x)        # default: str
print(repr(x))  # repr: prints out the emoji
# ascii also calls repr, but escape values(Unicodes) are printed out
print('ascii=>', ascii(x))

# ascii vs chr
print(ord('😷'))
print(chr(128567))

# Note
# repr() returns the best representation of a value or object
# if No repr() nor str(): no string representation
# print() calls the __str__, but if DNE: calls repr()
