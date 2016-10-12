class HtmlObject:
    def html(self):
        html = "<html>"
        for key, value in self.__dicte__.items():
            elem = """<div>
            <h1>{key}</h1>
            <h2>{value}</h2>
            <h3>{type}</h3>
            </div>""".format(key=key, value=value, type=type)
            html += elem
        html +="</html>"
        return html

class Foo(HtmlObject):
    def __init__(self):
        self.a = "Foo"
        self.b = 34
