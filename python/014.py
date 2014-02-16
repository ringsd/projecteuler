import time

start = time.time()

item_range = 1000001
value_array =  [0]*item_range
max_item = 0
max_value = 0

def calc_collatz( n ):
    k = 0
    org_n = n
    while True:
        if n == 1:
            value_array[org_n] = k
            return k
        k = k + 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        if org_n > n:
            k = k + value_array[n]
            value_array[org_n] = k
            return k
    return k

for i in range (1, item_range):
    value = calc_collatz( i )
    if value > max_value:
        max_value = value
        max_item = i

print "It took %f seconds."% (time.time() - start)
print "max_item:%d, max_value:%d\n"%(max_item, max_value)