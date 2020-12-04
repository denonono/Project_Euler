from timeit import default_timer as timer

divisor = 2
num = 208

start = timer()

while divisor <= 20:
    if num % divisor == 0:
        divisor += 1
    else:
        num += 1
        divisor = 2

print(num)
end = timer()
print(end-start)
