import sys
sys.path.append('../../')
from librarys import prime_factorization as pf

N = int(input())
fac_dic = pf.factorization(N) 
count = 0


for k,v in fac_dic.items():
  tmp = 1
  while(v >= tmp):
    v = v - tmp
    tmp += 1
    count += 1
  


print(count)
