S = input()

OK = []
NG = []
hatena = []
for i, s in enumerate(S):
    if s=="o": OK.append(i)
    elif s=="x": NG.append(i)
    elif s=="?": hatena.append(i)
ans = 0

#print(OK)
#print(NG)

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                flag = 1
                ls = [i,j,k,l]
                for ok in OK:
                    if ok in ls: 
                        continue
                    else: flag = 0
                for ng in NG:
                    if ng not in ls: 
                        continue
                    else: flag = 0
                if flag: ans += 1
                


print(ans)


"""
import math
S = input()

ok = []
ng = []
hatena = []
for i, s in enumerate(S):
    if s=="o": ok.append(i)
    elif s=="x": ng.append(i)
    elif s=="?": hatena.append(i)

if len(ok) > 4:
    print(0)
    exit()

ans = 0

# 確実な数を使った総数
if len(ok)==4:
    ans += (4*3*2*1)

elif len(ok)==3:
    ans += 3*(4*3)

elif len(ok)==2:
    ans += 6

elif len(ok)==1:
    ans += 1

# ?を含める場合の総数
if len(ok)==4:
    ans += 0

elif len(ok)==3:
    ans += len(hatena)*(4*3*2*1)

elif len(ok)==2:
    if len(hatena) == 1:
        ans += (4*3)
    elif len(hatena) > 1:
        ans += len(hatena)*(4*3) # ?のうち2個同じ数値を使うパターン
        ans += (math.factorial(len(hatena))/ math.factorial(2))*(4*3*2*1) # ?のうち2個違う数値を使うパターン

elif len(ok)==1:
    ans += len(hatena)*(4+6+4)# 4!/3!+4!/2!2!+4!/3!
    

print(ans)

"""