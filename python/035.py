import time
import math

#prime_range = 1000000
prime_range = 1000000
prime = [0]*prime_range
primeflag = [True]*prime_range

def find_prime(n):
    k = 0
    primeflag[0] = False
    primeflag[1] = False
    for i in range( 2, n ):
        j = i
        if primeflag[i] == True:
            prime.append( i )
            prime[k] = i;
            k = k + 1
            while True:
                j = j + i
                if j >= n:
                    break
                primeflag[j] = False
    return k


def order_list( start_pos, end_pos, number_list=[] ):
    if start_pos == end_pos:
        print number_list
        return
    
    i = start_pos
    while i <= end_pos:
        num = number_list[start_pos]
        number_list[start_pos] = number_list[i]
        number_list[i] = num
        order_list( start_pos + 1, end_pos, number_list )
        num = number_list[start_pos]
        number_list[start_pos] = number_list[i]
        number_list[i] = num
        i = i + 1

def solve_35():
    sum = 0
    prime_count = find_prime(prime_range)
    for i in range( 0, prime_count ):
        n = prime[i]
        if primeflag[n]:
            #get the n digit
            digit = 0
            base_10 = 1
            
            temp_n = n
            while temp_n:
                digit = digit + 1
                temp_n = temp_n / 10
                if temp_n == 0:
                    break
                base_10 = base_10 * 10
            
            #number rotation
            flag = True
            temp_n = n
            for i in range( 0, digit ):
                temp_n = temp_n % 10 * base_10 + temp_n / 10
                if primeflag[temp_n] == False:
                    flag = False

            if flag:
                for i in range( 0, digit ):
                    temp_n = temp_n % 10 * base_10 + temp_n / 10
                    primeflag[temp_n] = False
                print n
                
    for i in range( 0, prime_count ):
        if primeflag[ prime[i] ] == False:
            sum = sum + 1
        
    print sum
start = time.time()

#number_list = [0,1,2]
#order_list( 0, 2, number_list )
solve_35()

print "It took %f seconds."% (time.time() - start)

