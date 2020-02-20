from readFromFile import parsedata
from writeTofile import saveTofile
currentFile = 'books\\a_example.txt'
totalBooks, totalLibraries, totalDays, scores, libraries = parsedata(currentFile)


libraries.sort(key=lambda x: x.tRatio, reverse = True)
print(libraries)