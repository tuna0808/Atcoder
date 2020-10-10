a, b, c, d = map(int, input().split())

ls = [a * c, a * d, b * c, b * d]
print(max(ls))