class MyParentClass():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return str(self.x)

class SubClass(MyParentClass):
    def __init__(self,x,y):
        super().__init__(x,y)

if __name__ == '__main__':
    parent = MyParentClass(x='parent_x',y='parent_y')
    child = SubClass(x='child_x', y='child_y')
    print(parent)
    print(child)