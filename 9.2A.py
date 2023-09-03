q = int(input())  # Количество запросов
myset = set()  # Изначально пустое множество
output = []  # Список для хранения ответов на запросы второго типа

for _ in range(q):
    query = input().split()  # Считываем запрос и разделяем его на части

    if query[0] == '1':
        x = int(query[1])  # Число x
        myset.add(x)  # Добавляем x во множество

    elif query[0] == '2':
        x = int(query[1])  # Число x
        if x in myset:
            output.append('1')  # Добавляем 1 в список, если число x содержится во множестве
        else:
            output.append('0')  # Добавляем 0 в список, если число x не содержится во множестве

# Выводим ответы на запросы второго типа
for ans in output:
    print(ans)