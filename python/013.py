infile = open( '013.txt', 'r' )
indata = infile.read()

sum = 0

for line in indata.split('\n'):
    sum = sum + int(line)
infile.close()

print sum
