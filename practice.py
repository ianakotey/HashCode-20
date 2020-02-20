from itertools import islice

def parsedata(filepath):
    with( open(filepath, 'r' ) ) as file:

        totalBooks, totalLibraries, totalDays = map(lambda x:eval(x), file.readline().split() )
        # print(totalBooks, type(totalBooks), totalLibraries, type(totalLibraries), totalDays, type(totalDays))
        scores = dict( enumerate( 
                                map(lambda x:eval(x), file.readline().split() ),
                                start=0) 
                    )
        # print(scores, type(scores[0]))
        
        libraries = []
        sampleLibrary = {}

        while True:
            libraryData = {}

            # read the first line of library data
            data = file.readline()
            if not data: break

            libraryData['numberOfBooks'], libraryData['signupDays'], libraryData['booksPerDay'] = map(lambda x:eval(x), data.split() )

            # read the second line of library data
            data = file.readline()
            if not data: break

            libraryData['libraryBooks'] = map(lambda x:eval(x), data.split() )

            libraries.append(libraryData)


    return totalBooks, totalLibraries, totalDays, scores, libraries



if __name__ == "__main__":
    totalBooks, totalLibraries, totalDays, scores, libraries = parsedata('books\\a_example.txt')

    print(totalBooks, totalLibraries, totalDays, scores, libraries, sep='\n\n')

