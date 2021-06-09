sx, sy, gx, gy = map(int, input().split())

x = ((sy*gx+sx*gy) / (gy+sy))

print(x)