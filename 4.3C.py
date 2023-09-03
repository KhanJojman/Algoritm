def max_triplet_product(numbers):
    n = len(numbers)

    # Инициализируем минимальные значения для хранения трех наименьших чисел и максимальные значения для хранения трех наибольших чисел
    min1 = min2 = float('inf')
    max1 = max2 = max3 = float('-inf')

    # Проходим по всем числам в последовательности
    for i in range(n):
        # Если число меньше наименьшего, обновляем значения наименьших чисел
        if numbers[i] < min1:
            min2 = min1
            min1 = numbers[i]
        # Если число меньше второго наименьшего, обновляем значение второго наименьшего числа
        elif numbers[i] < min2:
            min2 = numbers[i]

        # Если число больше наибольшего, обновляем значения наибольших чисел
        if numbers[i] > max1:
            max3 = max2
            max2 = max1
            max1 = numbers[i]
        # Если число больше второго наибольшего, обновляем значение второго наибольшего числа
        elif numbers[i] > max2:
            max3 = max2
            max2 = numbers[i]
        # Если число больше третьего наибольшего, обновляем значение третьего наибольшего числа
        elif numbers[i] > max3:
            max3 = numbers[i]

    # Вычисляем максимальное произведение
    max_product = max(min1 * min2 * max1, max1 * max2 * max3)

    return max_product


# Считываем значения из ввода
n = int(input())
numbers = list(map(int, input().split()))

# Вычисляем максимальное произведение трех элементов
result = max_triplet_product(numbers)

# Выводим результат
print(result)