
def gcd( n, m ):
    """This function return a number is gcd of n and m"""
    assert(n > 0 and m > 0)
    while True:
        if n > m:
            temp = n
            n = m
            m = temp
        
        temp = m % n
        if temp == 0:
            return n
        else:
            n = temp

#lambda function using sample
lcm=lambda n, m: n*m/gcd( n, m )

def is_curious_fraction( n, m ):
    if n % 10 == 0 or m % 10 == 0:
        return False
    
    n0 = n % 10
    n1 = n / 10
    m0 = m % 10
    m1 = m / 10
    
    if n0 == m0 and n1 * m == m1 * n:
        return True
    
    if n0 == m1 and n1 * m == m0 * n:
        return True

    if n1 == m0 and n0 * m == m1 * n:
        return True
    
    if n1 == m1 and n0 * m == m0 * n:
        return True
    
    return False

def solve_33():
    product_i = 1
    product_j = 1
    for i in range( 10, 100 ):
        for j in range( i+1, 100 ):
            if is_curious_fraction( i, j ) == True:
                product_i = product_i * i
                product_j = product_j * j
                print "%d, %d"%(i, j)

    return product_j / gcd( product_i, product_j )
    
print solve_33()    