a, b, x = map(int, input().split())
l = 0
r = 10**9 + 1

while((r-l) > 1):
    mid = (r+l) // 2
    #print(mid)
    if mid*a + len(str(mid))*b > x:
        r = mid
    else:
        l = mid
print(l)