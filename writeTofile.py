def saveTofile(filename, orderedLibraries):
    with open(filename, mode='w') as file:
        file.write(f'{len(orderedLibraries)}')
