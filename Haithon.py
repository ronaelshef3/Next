lstzoo = []
class Animal:
    def __init__(self, type, name,hunger):
        self._type =type
        self._name=name
        self._hunger= hunger
        lstzoo.append(self)

    def get_name(self):
        return self._name

    '''return is hungry >0 '''
    def is_hungry(self):
        return self._hunger > 0

    ''' decrees on point  '''
    def feed (self):
        if self.is_hungry():
            self._hunger-=1

    def talk (self):
        if False :
            pass

        elif isinstance(self,Dog):
            return "woof"

        elif isinstance(self,Cat):
            return "mioooow"

        elif isinstance(self,Skunk):
            return "Dear lord!	"

        elif isinstance(self,Unicorn):
            return "I’m not your toy..."

        elif isinstance(self,Dragon):
            return "$@#$#@$	"

    def __str__(self):
        return  {
            "Type":self._type,
            "Name" :self._name,
            "Hunger":self._hunger,
            "Talk":self.talk()
        }.__str__()

class Dog(Animal):

    def __init__(self, name, hunger):
        super().__init__('Dog', name, hunger)





class Cat(Animal):
    def __init__(self, name, hunger):
        super().__init__('Cat', name, hunger)

class Skunk(Animal):
    def __init__(self, name, hunger):
        super().__init__('Skunk', name, hunger)

class Unicorn(Animal):
    def __init__(self, name, hunger):
        super().__init__('Unicorn', name, hunger)

# noinspection PyArgumentList
class Dragon(Animal) :
    def __init__(self, name, hunger,color = "Green" ):
        super().__init__('Dragon', name, hunger)
        self._color =color

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, color: {self._color}"


c=Cat("Mizzi", 43)
d =Dog("Lucht",54)
u = Unicorn("Noa kirel", 345)
s =Skunk ("sss", 42)
dr =Dragon("Tranp ",6666 )

for i  in lstzoo :
    print(i)


