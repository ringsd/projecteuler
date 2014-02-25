import math

def power_of_digit( n, power ):
    m = n
    sum = 0
    while True:
        mmod = m % 10
        sum = sum + math.pow( mmod, power )
        m = m / 10
        if m == 0:
            break
    if sum == n:
        return True
    else:
        return False
            
def solve_30():
    sum = 0
    i = 0
    power = 4
    maxnum = math.pow( 9, power ) * 10
    while True:
        if power_of_digit( i, power ):
            sum = sum + i
            print i
        i = i + 1
        if i > maxnum:
            break
    print sum

solve_30()