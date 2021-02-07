def main():
    f = open('File_IO/line.txt', 'r')
    for line in f:
        print(line.rstrip())


if __name__ == '__main__':
    main()

# Note
# open function returns a file object which is a iterator
# 'r'- read mode / 'w' - write mode: empties the file and ! writes over !
# / 'a' - append mode / '+' / 'b' or 't' : binary / text(DEFAULT) mode
