class XOREncryption:
    def __init__(self, key):
        self._key = key
        self.encrypted_key = format(self._key, 'b')

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    def to_ascii(self, char):
        return format(ord(char), 'b')

    def from_ascii(self, asci):
        return int(str(asci), 2)
