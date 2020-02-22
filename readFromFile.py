from itertools import islice
from Library import Library


def parsedata(filepath):
    with(open(filepath, 'r')) as file:

        totalBooks, totalLibraries, totalDays = map(
            lambda x: eval(x), file.readline().split())
        # print(totalBooks, type(totalBooks), totalLibraries, type(totalLibraries), totalDays, type(totalDays))
        scores = dict(enumerate(
            map(lambda x: eval(x), file.readline().split()),
            start=0)
        )
        # print(scores, type(scores[0]))

        libraries = []
        currentId = 0

        while True:

            # read the first line of library data
            data = file.readline()
            if not data.strip():
                break
            numberOfBooks, signUp, booksPerDay = map(
                lambda x: eval(x), data.split())

            # read the second line of library data
            data = file.readline()
            if not data.strip():
                break

            booksList = list(map(lambda x: eval(x), data.split()))

            booksList.sort(key=lambda book: scores[book], reverse=True)

            libraryData = Library(booksList=booksList, signUp=signUp, numberOfBooks=numberOfBooks,
                                  booksPerDay=booksPerDay, scores=scores, libraryId=currentId)

            libraries.append(libraryData)
            currentId += 1

    return totalBooks, totalLibraries, totalDays, scores, libraries


if __name__ == "__main__":
    totalBooks, totalLibraries, totalDays, scores, libraries = parsedata(
        'books\\a_example.txt')

    print(totalBooks, totalLibraries, totalDays, scores, libraries, sep='\n\n')
