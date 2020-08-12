fibonacci_numbers = [1,1]
position = 0

while len(str(fibonacci_numbers[-1])) < 1000:
    current_fibo = fibonacci_numbers[position] + fibonacci_numbers[position+1]
    fibonacci_numbers.append(current_fibo)
    position += 1

print(len(fibonacci_numbers))