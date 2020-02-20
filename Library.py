import math

scores = [1, 2, 3, 4, 5] 
 
class Library:

    def __init__(self, booksList,signUp,numberOfBooks, booksPerDay):
        self.booksList = booksList
        self.signUp = signUp
        self.numberOfBooks = numberOfBooks
        self.booksPerDay = booksPerDay

    def totalDays(self):
        return (math.ceil(self.numberOfBooks / self.booksPerDay) + self.signUp )

    def totalScore(self):
        return sum(map(lambda x: scores[x], self.booksList))

    def ratio(self):
        return self.totalScore()/self.totalDays()
        

if __name__ == "__main__":
    lib = Library([0,2,3], 3, 3, 2)
    print(lib.totalDays())
    print(lib.totalScore())
    print(lib.ratio())