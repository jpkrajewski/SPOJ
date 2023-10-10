# https://pl.spoj.com/problems/CALC/
try:
    while True:
        op, n1, n2 = input().split()
        print(eval(f'int({n1} {op} {n2})')) # Super unsafe, but efective :)
except Exception as e:
    pass