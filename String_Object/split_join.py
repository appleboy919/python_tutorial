# split function split words with spaces and new lines
s = 'this is a long string with a bunch of words in it.'
l = s.split()
print(l)
print(s.split('i'))

# join function concats list or tuples of strings with the given arg
s2 = ':'.join(l)
print(s2)
