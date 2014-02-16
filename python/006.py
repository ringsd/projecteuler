
def squart_sum( n ):
    sum1 = 0
    sum2 = 0
    for i in range( 1, n + 1 ):
        sum1 = sum1 + i * i
    for i in range( 1, n + 1 ):
        sum2 = sum2 + i
    sum2 = sum2 * sum2
    print sum2 - sum1

squart_sum(10)
squart_sum(100)
