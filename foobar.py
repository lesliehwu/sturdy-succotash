def isPrime(a):
    for y in range (2,a):
        while y < a:
            if (a % y != 0):
                y += 1
            else:
                return False
        return True

def isSquare(b):
    for z in range (2,b):
        while z < b:
            if (z * z != b):
                z += 1
            else:
                return True
        return False

def foo_bar(start,finish):
    while start < finish:
        if isPrime(start): 
            print "FooPRIME" + str(start)
        elif isSquare(start):
            print "BarSQUARE" + str(start)
        else:
            print "FooBarREGULAR" + str(start)
        start += 1

foo_bar(100,100000)
