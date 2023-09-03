def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))

# Вызов функции сортировки выбором
sorted_arr = selection_sort(arr)

# Вывод отсортированного массива
for num in sorted_arr:
    print(num, end=" ")