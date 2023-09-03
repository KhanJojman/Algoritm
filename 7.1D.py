def min_covering_length(n, k, points):
    points.sort()  # Сортируем точки по возрастанию

    # Инициализируем переменные
    left = 0
    right = points[-1] - points[0]  # Максимальная возможная длина отрезка
    result = right

    while left <= right:
        mid = (left + right) // 2  # Берем среднюю длину отрезка

        count = 1  # Количество отрезков, которые будут использованы
        last_point = points[0]  # Последняя точка, покрытая текущим отрезком

        for i in range(1, n):
            if points[i] - last_point > mid:  # Если текущая точка не покрыта текущим отрезком
                count += 1
                last_point = points[i]

        if count <= k:  # Если количество отрезков не превышает k
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

# Чтение входных данных
n, k = map(int, input().split())
points = list(map(int, input().split()))

# Вызов функции и вывод результата
print(min_covering_length(n, k, points))