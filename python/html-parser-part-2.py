from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data :
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data != "\n":
            print(">>> Data")
            print(data)


parser = MyHTMLParser()

page = ""
for _ in range(int(input())):
    page += input() + "\n"

parser.feed(page)
parser.close()
