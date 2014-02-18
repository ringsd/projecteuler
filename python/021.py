import math

def divisors_sum( n ):
    sqrt_n = int(math.sqrt(n))
    sum = 1
    for i in range( 2, sqrt_n ):
        if n % i == 0 and n / i != i:
            sum = sum + i + n / i
    return sum

test_num = 10000 + 1
divisors_sum_list = [0]*test_num
divisors_flag_list = [False]*test_num
for i in range( 1, test_num ):
    divisors_sum_list[i] = divisors_sum( i )

sum = 0    
for i in range( 1, test_num ):
    a = i
    b = da = divisors_sum_list[a]
    if a != b and \
       b < test_num and \
       divisors_flag_list[a] == False and \
       divisors_flag_list[b] == False and \
       divisors_sum_list[b] == a:
        sum = sum + a + b
        print "%d, %d"%(a, b)
        divisors_flag_list[a] = True
        divisors_flag_list[b] = True

print sum        