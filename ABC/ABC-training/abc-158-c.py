A, B = map(int, input().split())
ans = -1
for i in range(1,1101):
    if (int((i*8)/100)==A)  & (int((i*10)/100)==B):
        #print((i*8)/100)
        #print((i*10)/100)
        ans = i
        break

print(ans)