
num_array = []
infile = open( '011.txt', 'r' )
indata = infile.read()
for line in indata.split('\n'):
    num_line = []
    for num in line.split(' '):
        num_line.append( int(num) )
    num_array.append(num_line)
infile.close()

answer = 0
for i in range( 0, 17):
    for j in range (0, 17):
        product = num_array[i][j]*num_array[i][j+1]*num_array[i][j+2]*num_array[i][j+3]
        if product > answer:
            answer = product
        product = num_array[i][j]*num_array[i+1][j]*num_array[i+2][j]*num_array[i+3][j]
        if product > answer:
            answer = product
        product = num_array[i][j]*num_array[i+1][j+1]*num_array[i+2][j+2]*num_array[i+3][j+3]
        if product > answer:
            answer = product
        if j-1>=0 and j-2>=0 and j-3>=0:
            product = num_array[i][j]*num_array[i+1][j-1]*num_array[i+2][j-2]*num_array[i+3][j-3]
            if product > answer:
                answer = product
        
print answer