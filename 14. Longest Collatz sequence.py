n = 2
max_counter = 0
max_number = 0
while n != 1000000:
    counter = 0
    m = n
    while True:
        if m % 2 == 0:
            m = m // 2
            counter += 1
        else:
            m = 3 * m + 1
            counter += 1
        if m == 1:
            break
    if counter > max_counter:
        max_counter = counter
        max_number = n
    n += 1
print(max_number)