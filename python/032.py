import time

def pandigital_products( n, m ):
    flag = True
    n0 = n
    m0 = m
    digit = [0]*10
    while n:
        digit[n % 10] = digit[n % 10] + 1
        n = n / 10
        
    while m:
        digit[m % 10] = digit[m % 10] + 1
        m = m / 10

    product = n0 * m0
    
    while product:
        digit[product % 10] = digit[product % 10] + 1
        product = product / 10

    if digit[0] >= 1:
        return False
    for i in range( 1, 10 ):
        if digit[i] != 1:
            flag = False
            break
        #print digit[i]
        
    return flag
    
def solve_32():
    #digit 1 * digit 4 >= digit 4
    product_list = []
    sum = 0
    for n in range( 1, 10 ):
        for m in range( 1000, 9999 ):
            if pandigital_products( n, m ):
                product = n * m
                flag = True
                #for i in range( 0, len(product_list) ):
                #    if product_list[i] == product:
                #        flag = False
                #        break
                if flag == True:
                    sum = sum + product
                #    product_list.append( product )
                #print "%d*%d=%d"%(n, m, n*m)
                
    #digit 2 * digit 3 >= digit 4
    for n in range( 10, 100 ):
        for m in range( 100, 999 ):
            if pandigital_products( n, m ):
                product = n * m
                flag = True
                #for i in range( 0, len(product_list) ):
                #    if product_list[i] == product:
                #        flag = False
                #        break
                if flag == True:
                    sum = sum + product
                #    product_list.append( product )
                #print "%d*%d=%d"%(n, m, n*m)
    print sum

start = time.time()

#pandigital_products( 39, 186 )
solve_32()

print "It took %f seconds."% (time.time() - start)
