
number2string = {
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    100:'hundred',
    1000:'thousand'  
}

#for (k,v) in number2string.items(): 
#    print "dict[%d]=%s" %(k,v)

def number_to_string( n ):
    numstr  = ""
    numstr2 = ""
    flag = 0
    if n / 1000 != 0:
        numstr = numstr + number2string[n/1000] + ' ' + number2string[1000]
        numstr2 = numstr2 + number2string[n/1000] + number2string[1000]
        flag = 1
        n = n % 1000

    if n / 100 != 0:
        flag = 1
        numstr = numstr + number2string[n/100] + ' ' + number2string[100]
        numstr2 = numstr2 + number2string[n/100] + number2string[100]
        n = n % 100
    
    if n / 10 >= 2:
        if flag:
            numstr = numstr + ' and' + ' '
            numstr2 = numstr2 + 'and'
        flag = 2
        numstr = numstr + number2string[n/10*10]
        numstr2 = numstr2 + number2string[n/10*10]
        n = n % 10

    if n < 20 and n >= 10:
        if flag:
            numstr = numstr + ' and' + ' '
            numstr2 = numstr2 + 'and'
        flag = 2
        numstr = numstr + number2string[n]
        numstr2 = numstr2 + number2string[n]
        n = 0
        
    if n != 0:
        if flag == 1:
            numstr = numstr + ' and' + ' '
            numstr2 = numstr2 + 'and'
        if flag == 2:
            numstr = numstr + ' '
            numstr2 = numstr2
        numstr = numstr + number2string[n]
        numstr2 = numstr2 + number2string[n]
#    print numstr
    return len(numstr2)

sum = 0
for i in range (1, 1001):
    sum = sum + number_to_string( i )
print sum