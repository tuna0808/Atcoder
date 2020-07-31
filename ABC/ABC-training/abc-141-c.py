n, k, q = map(int, input().split())
users = {i + 1: 0 for i in range(n)}
for i in range(q):
    a = int(input())
    users[a] += 1

output = []
for user in users.values():
    if k - q + user > 0: output.append("Yes")
    else: output.append("No")
print(*output, sep="\n")

