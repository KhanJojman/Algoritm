def edit_distance(s1, s2):
    m = len(s1)
    n = len(s2)

    # Создаем матрицу размером (m+1) x (n+1) для хранения редакционных расстояний
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Инициализируем первую строку и первый столбец матрицы
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Вычисляем редакционное расстояние
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]


# Пример использования
s1 = input()
s2 = input()
distance = edit_distance(s1, s2)
print(distance)
