# https://pl.spoj.com/problems/PTROL/
try:
    for _ in range(int(input())):
        l = input().split()[1:]
        print(' '.join(l[1:]), l[0])    
except Exception as e:
    print(e)
    pass