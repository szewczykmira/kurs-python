import os
from urllib.request import urlopen, HTTPError, URLError
from html.parser import HTMLParser

class TagsParser(HTMLParser):
    URL = {
        'img': 'src',
        'a': 'href'
    }
    def is_active_link(self, link):
        """Check if link is active"""
        try:
            code = urlopen(link).getcode()
        except (HTTPError, URLError):
            return False
        return bool(code)

    def handle_starttag(self, tag, attrs):
        self.handle_tag(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        self.handle_tag(tag, attrs)

    def handle_tag(self, tag, attrs):
        if tag.lower() in self.URL.keys():
            attrs = dict(attrs)
            link = attrs[self.URL[tag.lower()]]
            if link is not '#':
                is_active = self.is_active_link(link)
                print("{} is active? {}".format(link, is_active))

class ServerChercker(object):
    def __init__(self, path):
        self._path = path
        self.html_parser = TagsParser()

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    def check_file(self, root, filename):
        if filename.endswith('.html'):
            with open(os.path.join(root, filename), 'r') as e:
                content = e.read()
                self.html_parser.feed(content)

    def crawl(self):
        for root, _, files in os.walk(self.path):
            for fi in files:
                self.check_file(root, fi)

abs_path = '/home/mira/Git/Praca/eds'
srv = ServerChercker(abs_path)
