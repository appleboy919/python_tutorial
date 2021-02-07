# subclass of string object
class MyString(str):
    def __str__(self):
        return self[::-1]


print('Hello World.'.upper())
print('hi'.capitalize())
print('David Oh'.swapcase())

print('42 x 7 {}'.format(42*7))
print("""
    Hello,
    World
""")

s = 'hello'
print(f'{s} -> {MyString(s)}')

# strings are immutable
print(f'{s}: {id(s)}')
print(f'{s.upper()}: {id(s.upper())}')


### Note ###
# strings are immutable -> methods returns a ! NEW OBJECT !
