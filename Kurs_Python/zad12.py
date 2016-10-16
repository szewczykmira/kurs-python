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
        self.encrypted_key = format(self.key, 'b')

    def to_ascii(self, char):
        return format(ord(char), 'b')

    def xor(self, char):
        return chr(int(self.to_ascii(char), 2) ^ int(self.encrypted_key, 2))

    def encrypt(self, string):
        encrypt = map(lambda x: self.xor(x), string)
        return ''.join(i for i in list(encrypt))
