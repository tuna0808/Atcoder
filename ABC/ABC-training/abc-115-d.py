"""
# TLE
def barger(lv):
    if lv == 0: return "P"
    tmp_b = barger(lv-1)
    return "B"+tmp_b+"P"+tmp_b+"B"

n, x = map(int, input().split())
barger_str = barger(n)
cnt = 1
ans = 0

# ここでTLEする.
for s in barger_str[::-1]:
    if s == "P": ans += 1
    if cnt == x: break
    cnt += 1

print(ans)
"""
