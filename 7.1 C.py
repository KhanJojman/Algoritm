def count_occurrences(arr, q):
    left = 0
    right = len(arr) - 1

    # Используем двоичный поиск для нахождения первого и последнего вхождения элемента
    first_occurrence = -1
    last_occurrence = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == q:
            first_occurrence = mid
            right = mid - 1
        elif arr[mid] < q:
            left = mid + 1
        else:
            right = mid - 1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == q:
            last_occurrence = mid
            left = mid + 1
        elif arr[mid] < q:
            left = mid + 1
        else:
            right = mid - 1

    # Если элемент не найден, возвращаем 0
    if first_occurrence == -1:
        return 0

    return last_occurrence - first_occurrence + 1


# Читаем вводные данные
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
q_values = list(map(int, input().split()))

# Вызываем функцию для каждого значения q и выводим результаты
for q in q_values:
    occurrences = count_occurrences(arr, q)
    print(occurrences, end=' ')