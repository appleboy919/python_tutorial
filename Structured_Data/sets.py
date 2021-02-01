def print_set(o):
    print('{', end='')
    for x in o:
        print(x, end='')
    print('}')


a = set("My name is David Oh")
b = set("What is your name?")
print_set(a)
print_set(sorted(a))
print_set(b)
print_set(sorted(b))

# Set operators
print('set operators:')
print_set(a-b)      # a-b
print_set(a & b)    # a and b
print_set(a | b)    # a or b
print_set(a ^ b)    # a xor b

# Note
# 1: Set does not allow duplicates
