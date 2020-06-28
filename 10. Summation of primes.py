import math as m

def main():
    sum = 5
    k = 1
    prime_suspect1, prime_suspect2 = 0, 0
    while k != 333333:
        prime_suspect1 = 6*k + 1
        prime_suspect2 = 6*k - 1
        if isPrime(prime_suspect1) == True:
            sum += prime_suspect1
        if isPrime(prime_suspect2) == True:
            sum += prime_suspect2
        k += 1
    print(sum)


def isPrime(x):
    counter = 0
    roof = int(m.sqrt(x))
    for i in range(2, roof+1):
        if x % i == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    main()    