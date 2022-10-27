"""
I am sure you are all used to the drill by now,
just submit your assignment6.py to autolab. Make
sure that you include the main function and any
tests that you ran.

Rubric:
20 points backupFile()
20 points addSemester()
20 points reverseLine()
20 points storeTabDelimitedFile()
10 points main() and tests
10 points style and comments 
"""

def backupFile(inputFile, outputFile):
    # use with open() on inputFile then assigned it to fi_n
    with open(inputFile, 'r') as fi_in:
        # use with open again, then change file to add .bak then
        # assign it to bac_f
        with open(outputFile+'.bak', 'w') as bac_f:
            # read() fi_in then put it in the variable new_file
            new_file = fi_in.read()
            # write the new_file in bac_f to create backup File
            bac_f.write(new_file)


def addSemester(inputFile, outputFile):
    # use with open() on inputFile and outputFile then assign them to a variable
    with open(inputFile, 'r') as fil_in:
        
        with open(outputFile, 'w') as fil_out:
            # We have the fall and spring list of CS class
            fall = ['cs 121', 'cs 215', 'cs 223', 'cs 260']
            
            spring = ['cs 122', 'cs 166', 'cs 224', 'cs 251', 'cs 261']
            
            for line in fil_in:
                # this for loop will takeout each of string in the list
                # then will add fall list and spring list to the backend 
                #of said string. It will added to fil.out file on its own line.
                for f in fall:
                    if f == line.strip():
                        line = line.strip() + ' fall'
                        print(line)
                        fil_out.write(line)
                        fil_out.write("\n")
                
                for s in spring:
                    if s == line.strip():
                        line = line.strip() + ' spring'
                        print(line)
                        fil_out.write(line)
                        fil_out.write("\n")


def reverseLine(inputFile, outputFile):
    # empty list
    listResult = []
    # with open() saved as variable fin. It take the inputFile then reverses
    # whatever is in the inputFile then put it in the outputFile.

    with open(inputFile, 'r') as fin:
        for line in fin:
            line = line.rstrip('\r\n')
            listResult.append(line)
    
    with open(outputFile, "w") as out:
        for ls in listResult:
            b = ''
            for i in range(len(ls), 0, -1):
                b += ls[i-1]
                out.write(b + '\n')

def storeTabDelimitedFile(inputFile):
    # empty list
    n = []

    with open(inputFile, 'r') as in_F:
        for lin in in_F:
            ta_line = lin.split('\t')
            n.append(ta_line)
        return n

def main():
    backupFile('classes.txt','backupFile')
    addSemester('classes.txt', 'semestersNames')
    reverseLine('classes.txt','reverseString')
    storeTabDelimitedFile('bobby.txt')


if __name__ == '__main__':
    main()
