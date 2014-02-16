import time

prime = []
primeflag = []

def find_prime(n):
    k = 0
    start = time.time()
    for i in range( 0, n ):
        primeflag.append( True )
    print "It took %f seconds."% (time.time() - start)    
    start = time.time()
    primeflag[0] = False
    primeflag[1] = False
    for i in range( 2, n ):
        j = i
        if primeflag[i] == True:
#            print i
            prime.append( i )
            k = k + 1
            j = i * i
            while True:
                if j >= n:
                    break
                primeflag[j] = False
                j = j + i
    print "It took %f seconds."% (time.time() - start)    
    return k

count = find_prime(2000000)
sum = 0
for i in range( 0, count ):
    sum = sum + prime[i]
print sum