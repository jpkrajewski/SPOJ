n = int(input())
for _ in range(n):
    _, *n = map(int, input().split())
    avg = sum(n) / len(n)
    diff = [abs(avg - x) for x in n]
    smallest = 1_000_000
    smallest_idx = -1
    for i, z in enumerate(diff):
        if z < smallest:
            smallest = z
            smallest_idx = i
    print(n[smallest_idx])