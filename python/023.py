import math
import time

start = time.time()


#num_range = 28124
num_range = 28150
perfect_num_flag = [False]*num_range
abundant_num_list = [0]*num_range

def abundant_num( n ):
    result = False
    sum = 1
    m = n
    sqrt_n = int(math.sqrt( n ))
    i = 2
#    print "%d :"%(n),
    while n != 1:
        if i > sqrt_n:
            break
        if n % i == 0:
            if i == n / i:
#                print "%d "%(i),
                sum = sum + i
            else:
#                print "%d %d "%(i, n/i),
                sum = sum + i + n / i
        i = i + 1;
    if sum > m:
        result = True
#    print result 
    return result

count = 0
for i in range( 1, num_range ):
    perfect_num_flag[i] = abundant_num( i )
    if perfect_num_flag[i] == True:
        abundant_num_list[count] = i
        count = count + 1
print count

print "It took %f seconds."% (time.time() - start)
start = time.time()

sum = 0
for i in range( 1, num_range ):
    flag = True
    for j in range( 0, count ):
        if i - abundant_num_list[j] <= 0:
            break
        if perfect_num_flag[i-abundant_num_list[j]]:
            flag = False
            break
    if flag:
        sum = sum + i
#        print i

print sum       

print "It took %f seconds."% (time.time() - start)
