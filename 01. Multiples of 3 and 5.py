sum1, sum2, sum3 = 0, 0, 0
for i in range(1, 334):
    sum1 += 3*i
for j in range(1, 200):
    sum2 += 5*j
for k in range(1, 67):
    sum3 += 3*5*k

print((sum1+sum2)-sum3)
