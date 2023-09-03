n, m = map(int, input().split())

A = []
for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for _ in range(n):
    row = list(map(int, input().split()))
    B.append(row)

C = []
for i in range(n):
    row = []
    for j in range(m):
        sum_ij = A[i][j] + B[i][j]
        row.append(sum_ij)
    C.append(row)

for row in C:
    for num in row:
        print(num, end=" ")
    print()