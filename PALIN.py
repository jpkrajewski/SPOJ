# A positive integer is called a palindrome if its representation in the decimal system is 
# the same when read from left to right and from right to left. 
# For a given positive integer K of not more than 1000000 digits, 
# write the value of the smallest palindrome larger than K to output. 
# Numbers are always displayed without leading zeros.

# Input
# The first line contains integer t, the number of test cases. 
# Integers K are given in the next t lines.

# Output
# For each K, output the smallest palindrome larger than K.

# Example
# Input:
# 2
# 808
# 2133

# Output:
# 818
# 2222

# 21 33
# 21 12
# 22 22

# 33 21
# 33 33

# 9912
# 99 99 


times = int(input())
for _ in range(times):
    number = input()
    length = len(number)
    middle = length // 2
    if length % 2 == 0:
        left = number[:middle]
        palindrome = left + left[::-1]
    else:
        left = number[:middle + 1]
        palindrome = left + left[::-1][1:]
    if int(palindrome) > int(number):
        print(palindrome)
    else:
        if length % 2 == 0:
            left_incremented = str(int(left) + 1)
            new_palindrome = left_incremented + left_incremented[::-1]
        else:
            left_incremented = str(int(left) + 1)
            new_palindrome = left_incremented + left_incremented[::-1][1:]
        print(palindrome)