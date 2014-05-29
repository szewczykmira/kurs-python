__author__ = 'Mira'
import re
import urllib.request
import html.parser
seen = [] #lista na ktora wchodza przejrzane strony
wanna_see = ['http://www.python.org/',] #lista stron do przejrzenia
class MyParser(html.parser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag=='a': #jezeli argument jest 'a':
            for (attr,value) in attrs:
                if attr == 'href': #sprawdzamy czy atrybut jest adresem i jezeli jest poprawny (z 'http://') to wrzucamy na liste wanna see
                    if (not (value in wanna_see) or not (value in seen)) and '://' in value and len(wanna_see)<10:
                        wanna_see.append(value)
    def handle_data(self, data): #przeszukujemy w danych wzorców ze slowem 'Python'
        for sentence in data.split('.'):
            if re.search('Python', sentence):
                print(sentence+'.')

my_parser = MyParser()
for strona in wanna_see:
    sock = urllib.request.urlopen(strona) #otwieranie strony - w zeszlym tygodniu mialam wlasnie problem ze znalezieniem tej biblioteki
    seen.append(strona)
    my_parser.feed(sock.read().decode('utf-8'))
