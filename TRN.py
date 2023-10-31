while True:
    try:
        m, n = map(int, input().split())
        matrix = []
        for _ in range(m):
            row = input().split()
            matrix.append(row)
        for row in range(n):
            data = []
            for col in range(m):
                data.append(matrix[col][row])
            print(" ".join(data))
    except Exception as e:
        break