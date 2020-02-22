from readFromFile import parsedata
from writeTofile import saveTofile

files = ['a_example.txt',  'b_read_on.txt', 'c_incunabula.txt',
         'd_tough_choices.txt', 'e_so_many_books.txt', 'f_librabries_of_the_world.txt']
for currentFile in files:
    currentFile0 = "books/" + currentFile
    totalBooks, totalLibraries, totalDays, scores, libraries = parsedata(
        currentFile0)

    libraries.sort(key=lambda x: x.tRatio, reverse=True)
    currentFile1 = "solutions/" + currentFile
    saveTofile(currentFile1, libraries)
