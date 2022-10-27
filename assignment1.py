import time
def milesToKilo(miles):
    """_Implement this method_
    Write a function that will convert miles to kilometers and return the result"""
    
    kilo = miles * 1.609344
    return kilo

    pass
def milesToKiloTest(value, test):
    """_Implement this method_
    Write a function that will comapre the milesToKilo() function result with
    the parameter test. If they are the same, then return true. Otherwise, false"""

    miles = milesToKilo(value)
    print(milesToKilo(value))
    if miles == test:
        return True
    else:
        return False

    pass
def builtIn1(x):
    """_Implement this method_
    Calculate x to the power of 3"""

    third = pow(x,3)
    return third

    pass
def builtIn2(x):
    """_Implement this method_
    Convert x to an integer by truncating"""

    turn = int(x)
    return turn

    pass
def builtIn3(x):
    """_Implement this method_
    Convert x to an integer by rounding"""

    lost = int(round(x))
    return lost

    pass
def builtIn4(x):
    """_Implement this method_
    Take the absolute value of x and convert it to a floating point number."""

    bobby = float(abs(x))
    return bobby

    pass