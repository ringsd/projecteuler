import time

def solve_28( n ):
    n = n * n
    i = 1
    step = 2
    sum = 0
    j = 0
    while True:
        sum = sum + i
        if i >= n:
            break
        i = i + step
        j = j + 1
        if j == 4:
            step = step + 2
            j = 0
    print sum
start = time.time()

solve_28( 1001 )

print "It took %f seconds."% (time.time() - start)