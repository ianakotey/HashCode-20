from readFromFile import parsedata
from writeTofile import saveTofile

currentFile = 'books/c_incunabula.txt'
totalBooks, totalLibraries, totalDays, scores, libraries = parsedata(
    currentFile)


libraries.sort(key=lambda x: x.tRatio, reverse=True)
currentFile1 = currentFile.split('.')[0]+'_sol.txt'
saveTofile(currentFile1, libraries)
