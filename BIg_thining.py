from traceback import print_tb


class BigThing:
    def __init__(self, p1):
        self._p1 =p1
    def size(self):
        if type(self._p1)==int :
            return self._p1
        elif type(self._p1)==dict or \
            type (self._p1 )==list or \
            type(self._p1)==set :
            return len(self._p1)


class BigCat(BigThing):
    def __init__(self,p1):
        super().__init__(p1)

    def size(self):
        if type(self._p1)==int :
            return  super().size()
        else:
            return  "OK"



w = BigThing(15)
print(w.size())
x = BigThing([1, 1, 1, 1, ])
print(x.size())
z = BigThing({1, 4, 6, 8, 5})
print(z.size())
w = BigThing({"rbtrv": "gtgr", "rgreg": 'gregetg'})
print( w.size())

g = BigCat(157)
print(g.size())
h= BigCat (['','',''])
print(h.size())