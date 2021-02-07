def main():
    infile = open('File_IO/line.txt', 'rt')
    outfile = open('File_IO/line-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)  # flush=True flushes the output buffer
    outfile.close()     # buffering -> prevent data loss
    print('\ndone.')


if __name__ == "__main__":
    main()
