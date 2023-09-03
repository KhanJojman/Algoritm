def calculate_lcs_count(A, B, C):
    n = len(A)
    m = len(B)
    k = len(C)

    table = [
        [[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)
    ]  # создание трехмерной таблицы размером (n+1)x(m+1)x(k+1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for l in range(1, k + 1):
                table[i][j][l] = table[i - 1][j][l]  # значение из верхней ячейки
                table[i][j][l] = max(
                    table[i][j][l], table[i][j - 1][l]
                )  # значение из левой ячейки
                table[i][j][l] = max(
                    table[i][j][l], table[i][j][l - 1]
                )  # значение из глубины

                if A[i - 1] == B[j - 1] == C[l - 1]:  # сравниваем символы из A, B и C
                    table[i][j][l] = max(
                        table[i][j][l], table[i - 1][j - 1][l - 1] + 1
                    )  # значение из диагональной ячейки + 1

    return table[n][m][k]  # возвращаем количество наибольших подпоследовательностей


# Ввод данных
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
k = int(input())
C = list(map(int, input().split()))

# Вычисление и вывод результата
lcs_count = calculate_lcs_count(A, B, C)
print(lcs_count)
