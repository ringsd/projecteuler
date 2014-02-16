
#a^2 + b^2 = c^2
#a + b + c = 1000
#how about the a*b*c
#

for a in range( 1, 1000 ):
    for b in range( a, 1000 ):
        c = 1000 - a - b
        if a*a + b*b == c*c:
            print a*b*c
