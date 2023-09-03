import random


def modifiedQuickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    return modifiedQuickSort(less) + equal + modifiedQuickSort(greater)


# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))

# Сортировка и вывод результата
sorted_arr = modifiedQuickSort(arr)
print(*sorted_arr)