from collections.abc import Collection
from main import MyCipher


class MyCipherColl(Collection):

    def __init__(self, cypher_list):
        for item in cypher_list:
            if not isinstance(item, MyCipher):
                raise TypeError("all objects in collection must be of type MyCipher")
        self._list = list(cypher_list)
        self.__index = 0

    def __contains__(self, item):
        return (item in self._list)

    def __iter__(self):
         # self.__index = 0
        return self._list.__iter__()

    # def __next__(self):
    #     if self.__index == len(self._list):
    #         raise StopIteration
    #     x = self._list[self.__index]
    #     self.__index += 1
    #     return x

    def __len__(self):
        return len(self._list)

if __name__ == '__main__':
    import main
    c= MyCipherColl([main.MyAES(),main.MyRSA(),main.MyVigenere(),main.MyVigenere()])
    for i in c:
        enc=i.encrypt(b"Mytext")
        dec=i.decrypt(enc)
        print(enc)
        print(dec)

    for i in c:
        enc = i.encrypt(b"Mytext")
        dec = i.decrypt(enc)
        print(enc)
        print(dec)

