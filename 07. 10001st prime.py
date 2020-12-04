import math as m


def isPrime(x):
    divisor_limit = int(m.sqrt(x))
    count = 0
    for i in range(2, divisor_limit+1):
        if x % i == 0:
            count += 1

    if count == 0:
        print(x)
        return True
    else:
        return False


def main():
    primes = 2
    n = 1
    while(primes != 10001):
        if isPrime(6 * n + 1) == True:
            primes += 1
        if isPrime(6 * n - 1) == True:
            primes += 1
        n += 1


if __name__ == "__main__":
    main()


