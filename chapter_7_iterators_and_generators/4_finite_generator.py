def finite_generator():
    yield "Python"
    yield "rocks"
    yield "So do you!"

if __name__ == '__main__':
    gen = finite_generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))