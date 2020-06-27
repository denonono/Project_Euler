u, v, sum = 2, 1, 0

while True:
    x = pow(u, 2) - pow(v, 2)
    y = 2 * u * v
    z = pow(u, 2) + pow(v, 2)
    sum = x + y + z

    if 1000 % sum == 0:
        temp = 1000 // sum
        x = x * temp
        y = y * temp
        z = z * temp
        print(x*y*z)
        break
    else:
        u += 1

    if sum > 500:
        v += 1
        u = v + 1
    