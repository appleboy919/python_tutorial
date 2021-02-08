# Add a simplehtml.html file before run

from html.parser import HTMLParser

metacount = 0


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        # when comment is encountered
        print("Encountered comment: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_starttag(self, tag, attrs):
        # when start tag is encountered
        global metacount
        if tag == 'meta':
            metacount += 1
        print("Encountered tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

        # print if attribute exists
        if attrs.__len__() > 0:
            print("\t Attributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])

    def handle_endtag(self, tag):
        # when end tag is encountered
        print("Encountered tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_data(self, data):
        if data.isspace():
            # skip white spaces
            return
        print("Encountered data: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])


def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    f = open("samplehtml.html")
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)
    print("Meta tags found: " + str(metacount))


if __name__ == "__main__":
    main()


### NOTE ###
# 1: www.python.org for more HTML functions and features
