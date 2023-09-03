n, L = map(int, input().split())
points = list(map(int, input().split()))

points.sort()

count = 1
last_point = points[0] + L

for point in points:
    if point > last_point:
        count += 1
        last_point = point + L

print(count)


print(len(points))
print(*points)
