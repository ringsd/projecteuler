
num_range = 1000000 - 1

number = [0,1,2,3,4,5,6,7,8,9]

def factor( n ):
    factor_num = 1
    for i in range (1, n+1):
        factor_num = factor_num * i
    return factor_num

while num_range != 0:
    number_len = len(number)    
    factor_num = factor( number_len - 1 )
    k = 0
    while num_range - factor_num >= 0:
        num_range = num_range - factor_num
        k = k + 1
    print "%d!*%d - %d"%(number_len - 1, k, number[k])
    del number[k]

print "0!*1 - %d"%(number[0])
