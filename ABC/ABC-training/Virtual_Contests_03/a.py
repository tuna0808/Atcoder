s = int(input())
i = 2
al = set()
al.add(s)

while(True):
    if s%2 == 0:
        s /= 2
    else:
        s = s*3 + 1
    
    if s in al: 
        break
    else:
        i += 1
        al.add(s)


print(i)
