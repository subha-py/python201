class Doubler:
    """
    An infinite iterator
    """
    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        Doubles the number each time next is called and returns it
        :return:
        """
        self.number = 1
        return self.number*self.number
    def __str__(self):
        return str(self.number)

if __name__ == '__main__':
    doubler = Doubler()
    count = 0
    for number in doubler:
        print(doubler)
        if count > 5:
            break
        count+=1