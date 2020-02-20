import math

class Library:
    '''Class to hold library data'''

    def __init__(self, booksList, signUp, numberOfBooks, booksPerDay, scores):
        self.booksList = booksList
        self.signUp = signUp
        self.numberOfBooks = numberOfBooks
        self.booksPerDay = booksPerDay
        self.scores = scores
        self.tScore = self.totalScore()
        self.tDays = self.totalDays()

    def totalDays(self) -> int:
        return (math.ceil(self.numberOfBooks / self.booksPerDay) + self.signUp)

    def totalScore(self) -> int:
        return sum(map(lambda x: self.scores[x], self.booksList))

    def ratio(self) -> float:
        return self.totalScore()/self.totalDays()

    def __repr__(self):
        return f'\n\tLibrary: \t numberOfBooks: {self.numberOfBooks} \t No. of Signup days: {self.signUp} \t booksPerDay: {self.booksPerDay} \t Total book score: {self.tScore} \n'


if __name__ == "__main__":
    lib = Library([0, 2, 3], 3, 3, 2, [0,1,2, 3])
    print(lib.totalDays())
    print(lib.totalScore())
    print(lib.ratio())
