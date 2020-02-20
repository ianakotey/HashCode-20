def saveTofile(filename: str, orderedLibraries: list):
    addBooks = []
    with open(filename, mode='a') as file:
        file.write(f'{len(orderedLibraries)}\n')
        for library in orderedLibraries:

            books = ' '.join(list(map(lambda x: str(x), library.booksList)))

            file.write(
                f'{library.libraryId} {len(library.booksList)}\n{ books } \n'
            )

            books = ""
            for t in library.booksList:
                addBooks.append(t)
