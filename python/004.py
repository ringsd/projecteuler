import math

def is_palindromic_num(num):
    flag = True
    bit = 1
    #get the number bit count
    tempnum = num
    while True:
        tempnum = tempnum / 10
        if tempnum == 0:
            break
        bit = bit + 1
#    print bit
#    print num
    half_bit = bit / 2
    for i in range( 1, half_bit + 1 ):
        low_bit =  num / int(math.pow( 10, i - 1 )) % 10
        high_bit = num / int(math.pow( 10, bit - i)) % 10
#        print "low_bit:%d, high_bit:%d" %(low_bit, high_bit)
        if low_bit != high_bit:
            flag = False
            break
    return flag

def get_palindromic_max(minnum, maxnum):
    answer = 0
    i = maxnum
    while True:
        j = maxnum
        while True:
            ans = False
            bit = 0
            k = i * j
            if answer > k:
                break
            if is_palindromic_num( k ) == True:
                ans = True
                answer = k
            if ans and answer < k:
                answer = k
            j = j - 1
            if j < minnum:
                break
        i = i - 1
        if i < minnum:
            break
    print answer

#is_palindromic_num( 695606 )
get_palindromic_max( 100, 999 )