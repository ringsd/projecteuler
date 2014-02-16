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

def div_eachn_remainder( num ):
    answerlist = []
    answer = 1
    for i in range(0, num + 1):
        answerlist.append(0)
    for i in range(1, num + 1):
        t = 0
        k = i
        print "number:%d" %(i)
        while True:
            p_count = 0
            print prime[t]
            if k < prime[t]:
                break
            while k % prime[t] == 0:
                k = k / prime[t]
                p_count = p_count + 1
            if p_count > answerlist[prime[t]]:
                answerlist[prime[t]] = p_count
            if k < prime[t]:
                break
            t = t + 1
    for i in range(1, num + 1):
        answer = answer * int(math.pow( i, answerlist[i] ))
    print answer

number = 10
find_prime(number + 1)
div_eachn_remainder(number)