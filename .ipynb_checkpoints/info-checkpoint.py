def sese():
    print("SESE is great!")

def asu():
    print("ASU is great!")

def ave(x):
    return sum(x)/len(x)
def factorial(n):
    value=1
    for i in range(1,n+1):
        value=value*i
    return value

def tang(x):
    import numpy as np
    return np.sin(x)/np.cos(x)