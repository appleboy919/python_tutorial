def print_list(o):
    for x in o:
        print(x, end=' ')
    print()


seq = range(11)
print_list(seq)

# list comprehension
seq2 = [x*2 for x in seq]
print_list(seq2)

seq3 = [x for x in seq if x % 3 != 0]
print_list(seq3)

# list of tuples
seq4 = [(x, x**2) for x in seq]
print_list(seq4)

# dictionaries
seq5 = {x: x**2 for x in seq}
print(seq5)

# sets
seq6 = {x for x in 'South Korea' if x in 'North Korea'}
print_list(seq6)

### Note ####
# List comprehension: list created based on another list or iterator
