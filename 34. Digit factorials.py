import math as m
n = 3
final_sum = 0

while n < 200000:
    temp_sum = 0
    for i in str(n):
        temp_sum += m.factorial(int(i))
    if temp_sum == n:
        final_sum += n
    n += 1
    
print(final_sum)