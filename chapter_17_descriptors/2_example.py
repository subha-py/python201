from weakref import WeakKeyDictionary

class Drinker:
    def __init__(self):
        self.req_age = 21
        self.age = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.age.get(instance,self.req_age)

    def __set__(self, instance, value):
        if value < 21:
            msg = '{name} is too young to legally imbibe'.format(name = instance.name)
            raise Exception(msg)
        self.age[instance] = value
        print('{name} can legally drink in USA'.format(name=instance.name))

    def __delete__(self, instance):
        del self.age[instance]

class Person:
    drinker_age = Drinker()

    def __init__(self,name,age):
        self.name = name
        self.drinker_age = age

if __name__ == '__main__':
    p = Person('Miguel', 30)
    p = Person('Niki', 21)

# weak reference is an object that get destroyed if there is no strong instance of the object exists.