T = input()
T_l = [t for t in T]

for i in range(len(T_l)):
  if T[i] =="?": T_l[i] = "D"

print("".join(T_l))