__author__ = 'Mira'
import re
import urllib.request
import html.parser
import threading
#wszystko tak samo jak w wersji z listy 5 poza watkami;
seen = []
wanna_see = ['http://www.python.org/',]
class MyParser(html.parser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag=='a':
            for (attr,value) in attrs:
                if attr == 'href':
                    if (not (value in wanna_see) or not (value in seen)) and '://' in value and len(wanna_see)<10:
                        wanna_see.append(value)
    def handle_data(self, data):
        for sentence in data.split('.'):
            if re.search('Python', sentence):
                print(sentence+'.')

my_parser = MyParser()
def ogarnianie(strona):
    sock = urllib.request.urlopen(strona)
    seen.append(strona)
    my_parser.feed(sock.read().decode('utf-8'))
for strona in wanna_see:
    threading.Thread(target=ogarnianie(strona)).start() #wstawianie watkow
