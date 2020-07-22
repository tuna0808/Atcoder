N = int(input())
ls = {i+1: 0 for i in range(N+1)}
flag = 0
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            tmp = (x ** 2) + (y ** 2) + (z ** 2) + (x * y) + (y * z) + (z * x)
            if tmp > N:
                flag = 1
                break
            else:
                ls[tmp] += 1
        #if flag: break
    #if flag: break
            

for i in range(N):
    print(ls[i+1])