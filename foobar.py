def foo_bar(start,finish):

    next_square = 1

    prime_list = []

    def isPrime(a):
        if a == 1:
            return False
        for y in prime_list:
            if (y * y > a):
                break
            if (a % y == 0):
                return False
        prime_list.append(a)
        return True

    for i in range (1,start):
        isPrime(i)
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

foo_bar(10,100000)
