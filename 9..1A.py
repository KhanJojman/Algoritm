# Ввод количества запросов
q = int(input())

# Инициализация списка
lst = []

# Обработка запросов
for _ in range(q):
    query = input().split()
    q_type = int(query[0])

    if q_type == 1:
        x = int(query[1])
        y = int(query[2])

        if x == 0:
            lst.insert(0, y)
        else:
            lst.insert(x, y)
    elif q_type == 2:
        x = int(query[1])
        print(lst[x - 1])
    elif q_type == 3:
        x = int(query[1])
        lst.pop(x - 1)