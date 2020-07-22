a, b, k = map(int, input().split())
after_a = max(0, a - k)
after_b = b
if after_a == 0:
    k -= a
    after_b = max(0, b - k)

print(after_a, after_b)