fibo = [1, 2]
current_position = 0
current_value = 0
sum = 0

while(True):
    current_value = fibo[current_position] + fibo[current_position+1]
    if current_value <= 4000000:
        fibo.append(current_value)
        current_position += 1
    else:
        break
print(fibo)


for i in fibo:
    if i % 2 == 0:
        sum += i
print(sum)
