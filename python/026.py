import time

#This problem maybe from solve the the big number 

def reciprocal_cycles( m, n ):
    if m > n:
        return 0
    
    quotient_count  = 0
    quotient_list   = [0]*1001
    remainder_list  = [0]*1001
    
    while True:
        while m < n:
            m = m * 10
        quotient = m / n
        remainder = m % n
        m = remainder
        if remainder != 0:
            #print ("%d")%(quotient),
            for i in range( 0, quotient_count + 1 ):
                if quotient == quotient_list[i] and remainder == remainder_list[i]:
                    count = quotient_count + 1 - i
                    return count
            quotient_count = quotient_count + 1
            quotient_list[quotient_count]   = quotient
            remainder_list[quotient_count]  = remainder
        else:
            return 0
    
    return 0

def solve_26():
    max_count = -1
    max_index = -1

    index = 1
    while True:
        count = reciprocal_cycles( 1, index )
        if max_count < count:
            max_count = count
            max_index = index
        index = index + 1
        if index > 1001:
            break

    print ("%d:%d")%(max_index, max_count)    
    
    
#bas
def solve_26_1():
    max_count = -1
    max_index = -1

    index = 1000
    while True:
        count = reciprocal_cycles( 1, index )
        if max_count < count:
            max_count = count
            max_index = index
        index = index - 1
        if index < 1 or index < max_count:
            break

    print ("%d:%d")%(max_index, max_count)
    
start = time.time()

#solve_26()
solve_26_1()

print "It took %f seconds."% (time.time() - start)
