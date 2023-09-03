def binary_search(arr, q):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == q:
            return mid
        elif arr[mid] < q:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Читаем вводные данные
n = int(input())
arr = list(map(int, input().split()))
q = int(input())

# Вызываем функцию и выводим результат
print(binary_search(arr, q))