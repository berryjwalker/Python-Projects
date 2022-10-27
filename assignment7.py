def logMessage(logFile, message):
    # open file then append message with newline character.
    # then close file.
    file = open(logFile, "a")
    file.write(message, "\n")
    file.close()

def getLine(inputFile, lineNumber):
    # counter holds one because the first line starts at 1
    # instead of zero.
    counter = 1

    file = open(inputFile)

    for f in file:
        # checks if lineNumber has found match or not
        if counter == lineNumber:
            return f.strip()

        counter += 1
    return None

def writeCSV(outputFile, data):
    file = open(outputFile, 'w')
    # goes through each record in data then write it to a file
    for d in data:
        file.write(str(d[0]) + ',' + str(d[1]) + '\n')

    file.close()


def main():
    logMessage("log.txt", "Have a good day!")
    print(getLine("log.txt", 3))
    writeCSV("datasheet.csv",[['cs', 121], ['cs', 122], ['cs', 223]])


if __name__ == '__main__':
    main()