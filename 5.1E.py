def last_digit_sum(m, n):
    # Инициализируем последовательность последних цифр чисел Фибоначчи с начальными значениями 0 и 1
    fib_last_digits = [0, 1]

    # Находим периодичность последних цифр чисел Фибоначчи
    for i in range(2, 60):
        fib_last_digits.append((fib_last_digits[i - 1] + fib_last_digits[i - 2]) % 10)

    # Вычисляем последнюю цифру суммы чисел Фибоначчи с номерами от m до n
    sum_last_digit = (fib_last_digits[(n + 2) % 60] - fib_last_digits[(m + 1) % 60]) % 10

    # Если значение отрицательное, добавляем 10
    if sum_last_digit < 0:
        sum_last_digit += 10

    return sum_last_digit


# Считываем значения из ввода
m, n = map(int, input().split())

# Вычисляем последнюю цифру суммы чисел Фибоначчи с номерами от m до n
result = last_digit_sum(m, n)

# Выводим результат
print(result)