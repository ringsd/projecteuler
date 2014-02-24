import time
import math

prime_range = 2000000
prime = [0]*prime_range
primeflag = [True]*prime_range

def find_prime(n):
    k = 0
    primeflag[0] = False
    primeflag[1] = False
    for i in range( 2, n ):
        j = i
        if primeflag[i] == True:
#            print i
#            prime.append( i )
            k = k + 1
            while True:
                j = j + i
                if j >= n:
                    break
                primeflag[j] = False
    return k


start = time.time()

prime_count = find_prime( prime_range )

print "It took %f seconds."% (time.time() - start)

print "The max prime is prime[%d]"%(prime_count-1)

def solve_27():
    max_n = 0
    product = 0
    a = -999
    while True:
        a = a + 1
        if a >= 1000:
            break
        b = -1000
        while True:
            b = b + 1
            if b >= 1000:
                break
            n = 0
            m = 0
            while True:
                m = n * n + a * n + b
                if m > 0 and primeflag[m] == True:
                    n = n + 1
                else:
                    break
            if n > max_n:
                product = a * b
                max_n = n
                print "%d, %d, %d"%(max_n, a, b)
            
    print "%d, %d"%(max_n, product)
    
start = time.time()

solve_27()

print "It took %f seconds."% (time.time() - start)
