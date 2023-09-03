from collections import deque

stack = deque()
res = []

q = int(input().strip())

for _ in range(q):
    query = list(map(int, input().strip().split()))

    if query[0] == 1:
        stack.append(query[1])
    elif query[0] == 2:
        if stack:
            stack.pop()

    res.append(str(stack[-1]) if stack else '-1')

print('\n'.join(res))