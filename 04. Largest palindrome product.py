def is_palindrome(a):
    return a == a[::-1]

max = 0
for i in range(100,1000):
    for j in range(100, 1000):
        product = i*j
        if is_palindrome(str(product)):
            if product > max:
                max = product
print(max)
