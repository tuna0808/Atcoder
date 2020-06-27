X, Y = map(int, input().split())
ans = "No"
for turu in range(X+1):
    tmp = 2*turu + 4*(X-turu)
    if tmp == Y:
        ans = "Yes"
        break
print(ans)


