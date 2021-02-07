def main():
    infile = open('File_IO/uw_madison.jpeg', 'rb')
    outfile = open('File_IO/uw-copy.jpeg', 'wb')
    while True:
        buf = infile.read(10240)    # use 10KB = 10240 as the buffer
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else:
            break
    outfile.close()
    print('\nDone.')


if __name__ == '__main__':
    main()
