
name_array = []
infile = open( '022.txt', 'r' )
indata = infile.read()
for line in indata.split('\n'):
    name_line = []
    for names in line.split(','):
        for name in names.split('\"'):
            if cmp( name, "" ) == 1:
                name_array.append( name )
infile.close()

name_array.sort()
sum = 0
i = 0
for name in name_array:
    i = i + 1
    score = 0
    for c in name:
#        print c
        score = score + ord(c) - ord('A') + 1
    sum = sum + score * i
    if cmp( name, "COLIN" ) == 0:
        print name
        print i
        print score

print sum