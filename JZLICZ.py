import string

letters = string.ascii_letters

try:
    for _ in range(int(input())):
        d = {}
        for c in input():
            if c not in letters:
                continue
            if c in d:
                d[c] += 1
            else:
                d[c] = 0
        for k in sorted(list(d), key=lambda x: x.islower()):
            print(f"{k} {d[k]}")
except:
    pass