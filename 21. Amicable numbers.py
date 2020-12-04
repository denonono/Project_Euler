amicable_nums = []
n = 220

def divisors(x):
    sum = 0
    for i in range(1, x//2+1):
        if x % i == 0:
            sum += i
    return sum



while n < 10000:
    divisors_sum = divisors(n)
    divisors_divisors_sum = divisors(divisors_sum)

    if divisors_divisors_sum == n and n != divisors_sum and n not in amicable_nums:
        amicable_nums.append(n)
        amicable_nums.append(divisors_sum)
    n += 1
    
print(sum(amicable_nums))
