class MyIterator:
    def __init__(self,letters):
        self.letters = letters
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.letters):
            raise StopIteration
        letter = self.letters[self.position]
        self.position +=1
        return letter

if __name__ == '__main__':
    i = MyIterator('abcd')
    for letter in i:
        print(letter)