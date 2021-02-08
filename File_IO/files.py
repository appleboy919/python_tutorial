def main():
    # open a file for writing and create it if it doesn't exist
    # f = open("python_tutorial/textfile.txt", "w+")

    # open the file for appending text to the end
    # f = open("python_tutorial/textfile.txt", "a")
    f = open("python_tutorial/textfile.txt", "r")

    # write some lnes of data to the file
    # for i in range(10):
    #     f.write("This is line " + str(i)+"\r\n")

    # close the file when done
    # f.close()

    # open the file back up and read the contents
    if f.mode == 'r':
        # contents = f.read()
        # print(contents)
        fl = f.readlines()
        for x in fl:
            print(x)


if __name__ == "__main__":
    main()

### Note ###
# 1: "a" mode append data to the end of the file
# 2: readlines() reads the file line by line
