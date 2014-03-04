
def base10_to_base2( n ):
    base2n = 0
    if n == 0:
        return 0
    return base10_to_base2( n/2 ) * 10 + n % 2

def palindromes( s ):
    flag = True
    str_len = len(s)
    half_len = str_len / 2
    for i in range( 0, half_len+1 ):
        if s[i] != s[str_len-i-1]:
            flag = False
            break
    return flag

def solve_36():
    sum = 0
    for i in range( 1, 1000001 ):
        if palindromes( str(i) ):
            #print i
            base2n = base10_to_base2( i )
            if palindromes( str(base2n) ):
                sum = sum + i
                print i
    print sum
    
solve_36()

