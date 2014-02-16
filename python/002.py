old_term1 = 0
old_term2 = 1
new_term = 1
sum = 0
while True:
    new_term = old_term1 + old_term2
    if new_term > 4000000:
        break
    if new_term%2 == 0:
        sum = sum + new_term
    old_term1 = old_term2
    old_term2 = new_term
    print new_term
print sum
