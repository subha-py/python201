class Base():
    def __init__(self):
        s= super()
        print(s.__thisclass__)
        print(s.__self_class__)
        s.__init__()

class SubClass(Base):
    pass

if __name__ == '__main__':
    sub = SubClass()