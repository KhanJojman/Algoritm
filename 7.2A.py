def has_dominant_element(arr):
    count = 0
    candidate = None

    # Используем алгоритм "Мажоритарное голосование"
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Проверяем, является ли кандидат доминирующим элементом
    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    if count > len(arr) // 2:
        return 1
    else:
        return 0


# Читаем вводные данные
n = int(input())
arr = list(map(int, input().split()))

# Проверяем, содержит ли последовательность доминирующий элемент
result = has_dominant_element(arr)
print(result)