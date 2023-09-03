def last_digit_fib(n):
    fib_numbers = [0, 1]
    for i in range(2, 61):
        fib_numbers.append((fib_numbers[i-1] + fib_numbers[i-2]) % 10)
    return fib_numbers[n % 60]

n = int(input())
print(last_digit_fib(n))