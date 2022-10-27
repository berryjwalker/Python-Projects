import time

def primeBattle(low, high):
    #We have to create an empty list.
    pblst = []

    #we will write an for loop to circle through low and high then
    #we write a if statement to find numbers that are divisible by 
    #7. However, not by 5 and they need to be positive numbers.
    for i in range(low) and range(high):
        if i % 7 == 0 and not i % 5 == 0 and i > 0:
            pblst.append(i)
    #Return said list
    return pblst

#Factorial as covered in class
def facRec(n):
    if n <= 1:
        return 1
    else:
        return n*facRec(n-1)

def facWhileLoop(n):
    #create a variable called, dns and num.
    dns = 1
    num = n
    #We write a while loop to check if num is higher then 0
    #Then if it is. It take 1 time num to store in the variable dns.
    #Then we return dns
    while(num > 0):
        dns = dns * num
        num = num - 1
    return dns

def facForLoop(n):
    #Create a variable called, bns
    bns = 1
    #Write a for loop that will time 1 times i then 
    #put it in the variable bns. We return bns
    for i in range(1, n+1):
        bns = bns * i
    return bns

def testFactorialTimes():
    """
    This is a handy function which will print the output and times of each method.
    Feel free to use this to test your methods and compare how long they take.
    Which one is the fastest? 
    """
    n = 5
    print('Testing Recursion...')
    start = time.time()
    results = facRec(n)
    end = time.time()
    print('Total Time: ', end-start, 'Results: ', results)

    print('Testing While Loop...')
    start = time.time()
    results = facWhileLoop(n)
    end = time.time()
    print('Total Time: ', end-start, 'Results: ', results)

    print('Testing For Loop...')
    start = time.time()
    results = facForLoop(n)
    end = time.time()
    print('Total Time: ', end-start, 'Results: ', results)



def coolMatrix(x, y):
    #we write an if statement to check if x and y is lower then 0.
    #It will return an empty list if it is true.
    if(x <= 0 or y <= 0):
        return []
    #Create a list matrix
    matrix  = []
    #Write a for loop that hold a list flst. Then we write another
    #for loop that will add the result of i-j. 
    for i in range(x):
        flst = []
        for j in range(y):
            flst.append(i-j)
        #We add flst to list matrix
        matrix.append(flst)
    #Return matrix
    return matrix
