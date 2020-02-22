def saveTofile(filename: str, orderedLibraries: list):
    addedBooks = []
    currentBooks = []
    with open(filename, mode='w') as file:
        file.write(f'{len(orderedLibraries)}\n')
        for library in orderedLibraries:
            currentBooks = list(
                filter(lambda x: x not in addedBooks, library.booksList))
            books = ' '.join(list(map(lambda x: str(x), currentBooks)))

            file.write(
                f'{library.libraryId} {len(library.booksList)}\n{ books } \n'
            )

            for t in currentBooks:
                addedBooks.append(t)
