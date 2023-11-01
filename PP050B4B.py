n = int(input())
for _ in range(n):
    a, b = input().split()
    la = len(a)
    lb = len(b)
    if la < lb:
        shorter = la
    else:
        shorter = lb
    answer = []
    for i in range(shorter):
        answer.append(a[i])
        answer.append(b[i])
    print("".join(answer))