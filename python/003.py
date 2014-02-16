import math

prime = []
primeflag = []

def find_prime(n):
    k = 0
    for i in range( 0, n ):
        primeflag.append( True )
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

ask = 600851475143
num = int(math.sqrt( ask ))
primecount = find_prime( num )

i = primecount - 1
while True:
    if ask % prime[i] == 0:
        print prime[i]
        break
    i = i - 1
