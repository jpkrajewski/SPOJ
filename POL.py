while True:
    try:
        n = int(input())
        for _ in range(n):
            string = input()
            l = round(len(string) / 2)
            print(string[:l])
    except Exception:
        break