N = int(input()) 
syou = N//100
amari = N % 100
if amari == 0:
    print(syou)
else:
    print(syou+1)