import re
import urllib.request
import html.parser


class MyParser(html.parser.HTMLParser):
    def __init__(self):
        self.seen = []
        self.to_see = ['http://www.python.org']
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attr, value) in attrs:
                if attr == 'href':
                    if (not (value in self.to_see) or not (value in self.seen)) and \
                        '://' in value and len(self.to_see) < 10:
                        self.to_see.append(value)
    
    def handle_data(self, data): #przeszukujemy w danych wzorców ze slowem 'Python'
        for sentence in data.split('.'):
            if re.search('Python', sentence):
                print(sentence + '.')

my_parser = MyParser()

for strona in my_parser.to_see:
    sock = urllib.request.urlopen(strona)
    my_parser.seen.append(strona)
    my_parser.feed(sock.read().decode('utf-8'))
