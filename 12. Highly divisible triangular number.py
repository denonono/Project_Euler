import math as m

def main():
    counter = 1
    tri_number = 0
    while True:
        tri_number = tri_number + counter
        counter += 1
        if divisors(tri_number) >= 500:
            print(tri_number)
            break


def divisors(x):
    divisors = 0
    for i in range(1, int(m.sqrt(x))):
        if x % i == 0:
            divisors +=2
        else:
            continue
    return divisors




if __name__ == "__main__":
    main()