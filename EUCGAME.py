while True:    
    try:
        n = int(input())
        for _ in range(n):
            a, b = map(int, input().split())
            if a < b:
                a, b = b, a
            while (not a == b) and (a > 0) and (b > 0):
                a = a - b
                if a == b:
                    break
                b = b - a
            print(a + b)
    except Exception:
        break