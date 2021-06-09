from collections import deque

S = list(input())
T = deque()
direction = 1

for s in S:
    if s != "R":
        if direction==1:
            if (len(T)>0) and (s == T[-1]):
                T.pop()
            else:
                T.append(s)
        elif direction == -1:
            if (len(T)>0) and (s == T[0]):
                T.popleft()
            else:
                T.appendleft(s)

    elif s == "R":
        direction *= -1



if direction==1:
    print("".join(list(T)))
else:
    print("".join(list(T)[::-1]))