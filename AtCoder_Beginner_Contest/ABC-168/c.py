import math

a, b, h, m = map(int, input().split())

h_d = 30*h + 30 * (m/60)
m_d = 360 * (m/60)

diff = abs(h_d-m_d)
c_2 = (a**2) + (b**2) - 2*a*b*math.cos(math.radians(diff))

print(math.sqrt(c_2))