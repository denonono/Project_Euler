n = 1
sum = 0
while n < 1000:
    sum += pow(n,n)
    n += 1

sum = str(sum)
print(sum[-10:-1])