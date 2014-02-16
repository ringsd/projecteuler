import time

start = time.time()


def calc_lattice_path( n ):
    map = [[0 for i in range(n+2) ] for j in range(n+2)]
    map[1][1] = 1
    for i in range( 1, n+2 ):
        for j in range( 1, n+2 ):
            if i == 1 and j == 1:
                continue
            map[i][j] = map[i-1][j] + map[i][j-1]
    for i in range( 1, n+2 ):
        for j in range( 1, n+2 ):
            print "%d "%map[i][j],
        print ""
    print map[n+1][n+1]
    
calc_lattice_path( 2 )
calc_lattice_path( 20 )
print "It took %f seconds."% (time.time() - start)
