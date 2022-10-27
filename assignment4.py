def squareOdds(x):
    #This function will return odd
    #numbers squared in an list.

    #Empty list
    sol = []

    #checks to see if it is odd then
    #adds it to the list then returns
    #said list
    for i in x:
        if i % 2 == 1:
            sol.append(i**2)
            
        
    return sol

def spaces(x):
    

    #We create an empty list
    spalst = []

    #We write a for loop with an if
    #statement that will look for spaces
    #in the string then add them to the
    #empty list
    for i in x:
        if ' ' in i:
            spalst.append(i)
    #We return the list
    return spalst

def specialChars(x):
    
    #Empty list
    spchl = []
    #we write two for loop then a if statement that checks to see if there is 
    #any word with special characters. Then the index of string and the postition
    #of the character string.
    for i, cti in enumerate(x, start=0):
        for f in range(len(cti)):
            if cti[f] == '!' or cti[f] == '@' or cti[f] == '&' or cti[f] == '$':
                b = str(i)+str(f)
                spchl.append(b)
    return spchl

def evenIndex(x):
    
    #Create an empty list
    evinlst = []
    
    #Write a for loop then an if statement that
    #checks to see if the number is even and the 
    #index is also even then adds it to the list
    #then returns it.
    for i in range(len(x)):
        if i % 2 == 0 and x[i] % 2 ==0:
            evinlst.append((i))
    return evinlst

def main():

    a = [1, 2, 3, 4]
    print(squareOdds(a))
    
    d = 'how are you today?'
    print(spaces(d))

    e = ['he!!o', 'w@rld']
    print(specialChars(e))

    f = [2, 4, 3, 3, 4, 5]
    print(evenIndex(f))

if __name__ == '__main__':
    
    main()
