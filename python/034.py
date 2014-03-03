
def factorial( n ):
    assert n >= 0
    product = 1
    for i in range( 1, n + 1 ):
        product = product * i
    return product
    
def solve_34():
    all_sum = 0
    factorial_array = [0]*10
    #calc the 1 - 9 factorial
    factorial_array[0] = 1
    for i in range( 1, 10 ):
        factorial_array[i] = factorial_array[i-1]*i
        print "%d! = %d"%( i, factorial_array[i] )

    max_num = factorial_array[9]*9 + 1
    for i in range( 10, max_num ):
        n = i
        sum = 0
        while True:
            t = n % 10
            sum = sum + factorial_array[t]
            n = n / 10
            if n == 0:
                break

        if sum == i:
            print sum
            all_sum = all_sum + i
    print all_sum

solve_34()