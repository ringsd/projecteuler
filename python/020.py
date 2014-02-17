
def get_factorial_sum( n ):
    factorial = 1
    sum = 0
    for i in range (1, n+1):
        factorial = factorial * i
    while factorial != 0:
        sum = sum + factorial % 10
        factorial = factorial / 10
    print sum
    return sum
    
get_factorial_sum( 10 )
get_factorial_sum( 100 )