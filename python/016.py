import math

sum = 0
k = int(math.pow( 2, 1000 ))
while True:
    sum = sum + k % 10
    k = k / 10
    if k == 0:
        break

print sum        