n = int(input())
segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

segments.sort(key=lambda x: x[1])

points = []
current_point = segments[0][1]
points.append(current_point)

for segment in segments[1:]:
    if current_point < segment[0]:
        current_point = segment[1]
        points.append(current_point