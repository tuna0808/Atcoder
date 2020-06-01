H_1, M_1, H_2, M_2, K = map(int, input().split())

st = H_1*60 + M_1
end = H_2*60 + M_2

tmp = end - K

print(tmp - st)