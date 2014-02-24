def Fibonacci( n ):
    if n == 1 or n == 0:
        return 1
    return Fibonacci( n-1 ) + Fibonacci( n-2 )
    
def Digits( n ):
    i = 1
    while True:
        n = n / 10
        if n == 0:
            break
        i = i + 1
    return i

fibonacci_num = []

fibonacci_num.append(1)
fibonacci_num.append(1)
i = 2
while True:
    fibonacci_num.append( fibonacci_num[i-1] + fibonacci_num[i-2] )
    if Digits(fibonacci_num[i]) >= 1000:
        print i + 1
        break
    i = i + 1
