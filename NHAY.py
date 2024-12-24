# Sample input:
# 2
# na
# banananobano
# 6
# foobar
# foo
# 9
# foobarfoo
# barfoobarfoobarfoobarfoobarfoo

# Sample output:
# 2
# 4

# 3
# 9
# 15
# 21


while True:
    try:
        needle_length = int(input())
        needle = input()
        text = input()

        counter = 0
        for index in range(len(text) - needle_length + 1):
            if text[index:index+needle_length] == needle:
                print(index)
    except Exception:
        break