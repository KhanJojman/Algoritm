def check_equal_sum_partition(n, values):
    total_sum = sum(values)

    # Если сумма значений не делится на 3 без остатка, то невозможно разделить на три равные суммы
    if total_sum % 3 != 0:
        return 0

    target_sum = total_sum // 3

    # Создаем таблицу размером (n+1) x (target_sum+1)
    # table[i][j] равно 1, если первые i предметов могут быть разделены на подмножества, сумма каждого равна j; иначе равно 0
    table = [[0] * (target_sum + 1) for _ in range(n + 1)]

    # Заполняем первый столбец нулями, так как сумма равна 0 при выборе любого количества предметов
    for i in range(n + 1):
        table[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            table[i][j] = table[i - 1][
                j
            ]  # Если не включаем текущий предмет, при условии, что предыдущие предметы могут быть разделены

            if j >= values[i - 1]:
                table[i][j] = (
                    table[i][j] or table[i - 1][j - values[i - 1]]
                )  # Если включаем текущий предмет и предыдущие предметы могут быть разделены

    return table[n][target_sum]


# Ввод данных
n = int(input())
values = list(map(int, input().split()))

# Вычисление и вывод результата
result = check_equal_sum_partition(n, values)
print(result)

# Не работает
