import time

currency = [200, 100, 50, 20, 10, 5, 2]
#currency = [5, 2]
currencylen = len( currency )
count = 0

def solve_31( choose, n ):
    count = 0
    if choose >= currencylen:
        return 1
    if n == 0:
        return 1
    max_num = n / currency[choose]
    for i in range( 0, max_num + 1 ):
        count = count + solve_31( choose + 1, n - i * currency[choose] )
    return count

    
def solve_31_1( n ):
    coin = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0]*(n+1)
    coinlen = len( coin )
    ways[0] = 1
    for i in range( 0, coinlen ):
        for j in range( coin[i], n + 1 ):
            ways[j] = ways[j] + ways[j - coin[i]] 
    print ways[n]
    
start = time.time()

#print solve_31( 0, 200 )
solve_31_1( 200 )

print "It took %f seconds."% (time.time() - start)

