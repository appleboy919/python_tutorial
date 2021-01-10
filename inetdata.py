import urllib.request


def main():
    webUrl = urllib.request.urlopen("http://www.google.com")
    print("result code: " + str(webUrl.getcode()))

    # html code for Google hompage
    data = webUrl.read()
    print(data)


if __name__ == "__main__":
    main()
