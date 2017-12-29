from itertools import islice
def double_generator():
    number = 2
    while True:
        yield number
        number *= number

if __name__ == '__main__':
    doubler = double_generator()
    for turn in islice(doubler,5):
        print(turn)
