S = input()
S = S[::-1]

ans = ""

for s in S:
    if s=="6":ans += "9"
    elif s=="9": ans += "6"
    else: ans += s
print(ans)