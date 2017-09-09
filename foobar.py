def isPrime(a):
    for y in range (2,a):
        while y < a:
            if (a % y != 0):
                y += 1
            else:
                return False
        return True

def foo_bar(start,finish):

    next_square = 1

    for i in range (1,start):
        if i == next_square * next_square:
            next_square += 1

    while start < finish:
        if isPrime(start): 
            print "Foo" + str(start)
        elif start == next_square * next_square:
            print "Bar" + str(start)
            next_square += 1
        else:
            print "FooBar" + str(start)
        start += 1

foo_bar(10,50)
