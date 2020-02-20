def saveTofile(filename, orderedLibraries):
    with open(filename, mode='w') as file:
        file.write(f'{len(orderedLibraries)}\n')
        for library in orderedLibraries:
            books = ""
            for i in library.books:
                books += books + i
                books = books[1:]

            file.write(f'{library.id} {len(library.books)}\n {books}')
