def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
    print()


# list is mutable
list_a = ['a', 'b', 'c']
print(', '.join(list_a))  # output: a, b, c
print_list(list_a)

#tuple is immutable
tuple_a = ('1', '2', '3')
# tuple_a.append('4')   # this occurs an error
