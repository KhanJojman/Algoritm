def calculate_lcs_length(A, B):
    n = len(A)
    m = len(B)

    table = [
        [0] * (m + 1) for _ in range(n + 1)
    ]  # создание таблицы размером (n+1)x(m+1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            table[i][j] = table[i - 1][j]  # значение из верхней ячейки
            table[i][j] = max(table[i][j], table[i][j - 1])  # значение из левой ячейки
            if A[i - 1] == B[j - 1]:  # сравниваем символы из A и B
                table[i][j] = max(
                    table[i][j], table[i - 1][j - 1] + 1
                )  # значение из диагональной ячейки + 1

    return table[n][m]  # возвращаем длину LCS


# Ввод данных
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# Вычисление и вывод результата
lcs_length = calculate_lcs_length(A, B)
print(lcs_length)
