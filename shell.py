import os
from os import path
import shutil
import datetime
from datetime import date, time, timedelta
import time
from shutil import make_archive
from zipfile import ZipFile


def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt"):
        # get the path to the file in the current directory
        src = path.realpath("textfile.txt")

        # let's make a backup copy by appending "bak" to the name
        dst = src + ".bak"

        # copy over the permissions, modification times, and other info
        shutil.copy(src, dst)  # copy the contents of a file
        shutil.copystat(src, dst)  # copy metadata from a file
        print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
        print(datetime.datetime.fromtimestamp(
            path.getmtime("textfile.txt.bak")))

        # rename the original file
        # os.rename("textfile.txt", "newfile.txt")

        # now put things into a ZIP archive
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir)

        # more fine-grained control over ZIP files
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("textfile.txt")
            # testzip file will have only these two files
            newzip.write("textfile.txt.bak")


if __name__ == "__main__":
    main()


### Notes ###
# 1: "with" keyword create a local scope which simplifies working with objects
