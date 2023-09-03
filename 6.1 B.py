import sys


def find_min_coin_set(money):
    # Список возможных номиналов монет
    coins = [1, 5, 10, 20, 50]

    # Массив для хранения количества монет для каждой суммы
    min_coins = [sys.maxsize] * (money + 1)
    min_coins[0] = 0

    # Массив для хранения выбранных монет
    selected_coins = [-1] * (money + 1)

    # Динамическое программирование
    for i in range(1, money + 1):
        for coin in coins:
            if i >= coin and 1 + min_coins[i - coin] < min_coins[i]:
                min_coins[i] = 1 + min_coins[i - coin]
                selected_coins[i] = coin

    # Восстановление набора монет
    coin_set = []
    current_money = money
    while current_money > 0:
        coin_set.append(selected_coins[current_money])
        current_money -= selected_coins[current_money]

    return coin_set


# Ввод суммы денег
money = int(input())

# Находим набор монет
coin_set = find_min_coin_set(money)

# Вывод количества монет в наборе
print(len(coin_set))

# Вывод номиналов монет
print(*coin_set)