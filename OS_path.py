import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # print the name of the OS
    print(os.name)

    # check for item existence and type
    print("Item exists: " + str(path.exists("textfile.txt")))
    print("Itme is a file: " + str(path.isfile("textfile.txt")))
    print("Item is a directory: " + str(path.isdir("textfile.txt")))

    # work with file paths
    print("Item path: " + str(path.realpath("textfile.txt")))
    print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))

    # get the modification time
    # using time class to convert modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    # construct datetime object using fromtimestamp function
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

    # calculate how long ago the tiem was modified
    td = datetime.datetime.now(
    ) - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It has been " + str(td)+" since the file was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")


if __name__ == "__main__":
    main()
