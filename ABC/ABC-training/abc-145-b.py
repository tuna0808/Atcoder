n = int(input())
s = input()

if n == 1:
    print("No")
    exit()

if s[:int(n / 2)] == s[int(n / 2):]: print("Yes")
else: print("No")
