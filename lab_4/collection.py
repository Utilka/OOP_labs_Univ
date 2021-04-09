from collections.abc import Collection
from main import MyCipher

from typing import Iterator, Iterable, Optional


class MyCipherColl(Collection):

    def __init__(self, cypher_list: Iterable[MyCipher]):
        for item in cypher_list:
            if not isinstance(item, MyCipher):
                raise TypeError("all objects in collection must be of type MyCipher")
        self._list = list(cypher_list)

    def __contains__(self, item: object) -> bool:
        return self._list.__contains__(item)

    def __iter__(self) -> Iterator[MyCipher]:
        return self._list.__iter__()

    def __len__(self) -> int:
        return self._list.__len__()


if __name__ == '__main__':
    import main

    c = MyCipherColl([main.MyAES(), main.MyRSA(), main.MyVigenere(), main.MyVigenere()])
    for i in c:
        enc = i.encrypt(b"Mytext")
        dec = i.decrypt(enc)
        print(enc)
        print(dec)

    for i in c:
        enc = i.encrypt(b"Mytext")
        dec = i.decrypt(enc)
        print(enc)
        print(dec)
