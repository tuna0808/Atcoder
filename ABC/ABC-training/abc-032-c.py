n, k = map(int, input().split())
s = []
for _ in range(n):
    s.append(int(input()))

if 0 in s:
    print(n)
    exit()

r, l = 0, 0
mul = 1
ans = 0

while (r < n):
    if mul * s[r] <= k:
        mul *= s[r]
        r += 1
        ans = max(ans, r - l)
    elif r == l:
        r += 1
        l += 1
    else:
        mul //= s[l]
        l += 1
print(ans)


"""
ans = 0
mul = 1
right = -1
for left in range(len(s)):
    while (mul <= k):
        right += 1
        if right == len(s):
            right -= 1
            break
        #print(f"left{left}, right{right}")
        if right != 0: mul = mul * s[right - 1]
        
        

    ans = max(ans, (right - 1) - left)
    mul = int(mul / s[left])
    #print(f"ans{ans}, mul{mul}")
    #print()
    if right == left:
        right += 1
    
        
print(ans)
"""

    

    
