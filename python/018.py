
linecount = 0
num_array = []
infile = open( '018-2.txt', 'r' )
indata = infile.read()
for line in indata.split('\n'):
    num_line = []
    for num in line.split(' '):
        num_line.append( int(num) )
    num_array.append(num_line)
    linecount = linecount + 1
infile.close()

for i in range(0, linecount):
    for j in range(0, i+1):
        print '%d '%num_array[i][j],
    print ''
    
for i in range(0, linecount):
    for j in range(0, i+1):
        if i > 0:
            num0 = 0
            num1 = 0
            if j > 0:
                num0 = num_array[i-1][j-1] + num_array[i][j]
            if j < i:
                num1 = num_array[i-1][j] + num_array[i][j]
            if num0 > num1:
                num_array[i][j] = num0
            else:
                num_array[i][j] = num1

max_value = 0
for i in range(0, linecount):
    if max_value < num_array[linecount-1][i]:
        max_value = num_array[linecount-1][i]

print max_value