# list
x = [1, 2, 3, 4]  # list is created with [] brackets
x[0] = 0  # list is mutable
for i in x:
    print("i is {}".format(i))
print("list x is {}".format(x))

# tuple
y = (1, 2, 3, 4)  # tuple is created with () parentheses
for j in y:
    print("j is {}".format(j))
print("tuple y is {}".format(y))
# y[0] = 0  # this line is an error -> tuple is immutable

# range()
z = range(5)  # range function creates a sequence from 0 to n-1
for k in z:
    print("k is {}".format(k))
# z[0] = 0 # this line is also an error -> range sequence is immutable
print("range(5, 30, 5) is {}".format(range(5, 30, 5)))


# dictionary: searchable sequence with key value pairs
w = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# prints only keys
for l in w:
    print('l is {}'.format(l))
# prints out tuple of key and value
for k, v in w.items():
    print('k: {}, v: {}'.format(k, v))


### NOTE ###
# 1: List, dictionariy are mutable -> can reassign
# 2: range(start, end, step)    ex) range(5,30,5) -> 5, 10, 15, 20, 25
