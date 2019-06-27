from datetime import datetime


class Person():

    def __init__(self):
        self.__birthday=datetime.now()
        self._name=None

    def set_name(self, nsme):
        self._name=name

    def get_name(self):
        return self._name

    def get_birthday(self):
        return self.__birthday


class Human(Person):

    def __init__(self, name):
        super().__init__()
        self._name=name


class Man(Human):
    __sex = "M"

    def get_sex(self):
        return self.__sex


class Woman(Human):
    __sex = "F"

    def get_sex(self):
        return self.__sex

    @classmethod
    def test(cls, arg):
        print(arg)


if __name__=='__main__':
    vasya = Man("Vasya")
    masha = Woman("Masha")

    print(masha.get_sex())
    print(vasya.get_sex())

    print(masha.get_name())
    print(vasya.get_birthday())

    Woman.test(56)
    
