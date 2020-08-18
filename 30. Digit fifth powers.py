n = 2
final = 0
while n < 400000:
    sum = 0
    for i in str(n):
        sum += int(i)**5
    if sum == n:
        final += n
    n += 1
print(final)