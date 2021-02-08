x = (1, 2, 3, 4, 5)
print(x, len(x))
y = list(reversed(x))
for i in y:
    print(i)
sum = sum(x, 10)  # sum of x + 10

# any, all
print(any((0, 0, 0, 0)))
print(all((1, 1, 0)))

# zip returns each items
z = zip(x, y)
for a, b in z:
    print(f'{a} - {b}')

# enumerate returns an index and a value
x = ('cat', 'dog', 'rabbit', 'velociraptor')
for i, v in enumerate(x):
    print(f'{i}: {v}')
