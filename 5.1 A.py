def fibonacci(n):
    # Инициализируем словарь для хранения промежуточных результатов
    fib_dict = {}

    # Вспомогательная функция для вычисления числа Фибоначчи
    def fibonacci_helper(n):
        # Базовый случай: F(0) = 0, F(1) = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1

        # Если результат для данного значения уже был вычислен, возвращаем его
        if n in fib_dict:
            return fib_dict[n]

        # Рекурсивный случай: F(n) = F(n-1) + F(n-2)
        # Вычисляем результат и сохраняем его в словаре
        fib_dict[n] = fibonacci_helper(n - 1) + fibonacci_helper(n - 2)

        return fib_dict[n]

    # Вызываем вспомогательную функцию
    result = fibonacci_helper(n)

    return result


# Считываем значение из ввода
n = int(input())

# Вычисляем n-е число Фибоначчи
result = fibonacci(n)

# Выводим результат
print(result)