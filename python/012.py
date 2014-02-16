
prime_range = 100000
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


prime_count = find_prime( prime_range )
print "The max prime is prime[%d]=%d"%(prime_count-1, prime[prime_count-1])

def get_divisors_num(n):
    divisor_num = 1
    prime_divisor = [1]*n
    m = n
    i = 0
    while True:
        while m % prime[i] == 0:
            m = m / prime[i]
            prime_divisor[i] = prime_divisor[i] + 1
        i = i + 1
        if m == 1:
            break
    j = 0
    while j < i:
        divisor_num = divisor_num * prime_divisor[j]
        j = j + 1
    return divisor_num

divisor_list = [0]*prime_range

for i in range(1, prime_range):
    divisor_num = get_divisors_num( i )
    divisor_list[i] = divisor_num

for i in range(1, prime_range):
    n = i * (i + 1) / 2
    divisor_num = 0
    if i % 2 == 0:
        divisor_num = divisor_list[i/2]*divisor_list[i+1]
    else:
        divisor_num = divisor_list[i]*divisor_list[(i+1)/2]
    if divisor_num >= 100:
        print "%d %d"%(n, divisor_num)
    if divisor_num >= 500:
        print "%d %d\n"%(n, divisor_num)
        break