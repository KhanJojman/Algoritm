def max_gold_weight(W, weights):
    n = len(weights)

    # Создаем таблицу размером (n+1) x (W+1)
    # table[i][j] будет содержать максимальный вес слитков, который можно уместить в рюкзак вместимостью j, если использовать только i первых слитков
    table = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            # Если слиток i больше вместимости рюкзака j, то не берем его и максимальный вес остается таким же как для i-1 слитков
            if weights[i - 1] > j:
                table[i][j] = table[i - 1][j]
            else:
                # Берем максимум из (максимальный вес для i-1 слитков без текущего слитка, максимальный вес для i-1 слитков с текущим слитком)
                table[i][j] = max(
                    table[i - 1][j], table[i - 1][j - weights[i - 1]] + weights[i - 1]
                )

    return table[n][W]


# Ввод данных
W, n = map(int, input().split())
weights = list(map(int, input().split()))

# Вычисление и вывод результата
max_weight = max_gold_weight(W, weights)
print(max_weight)
