import time
import math

prime_range = 101
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
            prime.append( i )
            k = k + 1
            while True:
                j = j + i
                if j >= n:
                    break
                primeflag[j] = False
    return k

#prime_count = find_prime(prime_range)    
    
def solve_29( n ):
    count = 0
    m = int(math.log(n) / math.log(2))
    m = m * n
    nflag = [False]*(n+1)
    for i in range( 2, n+1 ):
        if nflag[i] == True:
            continue
        t = 1
        step = 0
        iflag = [False]*(m+1)
        while True:
            t = i * t
            step = step + 1
            if t > n:
                break
            nflag[t] = True
            for j in range( 2, n+1 ):
                iflag[j*step] = True

        for j in range( 2, m+1 ):
            if iflag[j] == True:
                count = count + 1
    print count
    
start = time.time()

solve_29( 5 )
solve_29( 100 )

print "It took %f seconds."% (time.time() - start)
    
