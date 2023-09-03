n = int(input())
dictionary = {}

for _ in range(n):
    query = input().split()

    if query[0] == '1':
        key = int(query[1])
        value = int(query[2])
        dictionary[key] = value
    elif query[0] == '2':
        key = int(query[1])
        value = dictionary.get(key, -1)
        print(value)