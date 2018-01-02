
def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer

if __name__ == '__main__':
    c= counter()
    print(c())
    print(c())
    print(c())
    print(c())
    print(c())
