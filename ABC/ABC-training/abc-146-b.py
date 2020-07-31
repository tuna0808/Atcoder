n = int(input())
S = input()
ans = ""
for s in S:
    tmp = ord(s) + n
    if tmp > 90:
        tmp -= 26
    ans += chr(tmp)
print(ans)