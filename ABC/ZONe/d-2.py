S = list(input())
direction = 1
ls_1 = []
ls_2 = []


for s in S:
    if s != "R":
        if direction==1:
            ls_1.append(s)
        elif direction == -1:
            ls_2.append(s)
    elif s == "R":
        direction *= -1

if direction==-1:
    ls_1 = ls_1[::-1]
    ls = ls_1 + ls_2
    T = "".join(ls)
else:
    ls_2 = ls_2[::-1]
    ls = ls_2 + ls_1
    T = "".join(ls)

stack = []

for t in T:
    if len(stack) !=0:
        if stack[-1] == t:
            stack.pop()
        else:
            stack.append(t)
    else:
        stack.append(t)
    

print("".join(stack))
    