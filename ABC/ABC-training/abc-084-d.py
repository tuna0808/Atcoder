import math


def get_sieve_of_eratosthenes(n):# エラトステネスのふるい(O(NloglogN)). ~nまでの素数をリストで返す.
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


Q = int(input())
ls = [0]
prime = set(get_sieve_of_eratosthenes(10**5 + 10))

output = []
for i in range(10**5+10):
    if (i in prime) & (int((i+1)/2) in prime):
        ls.append(ls[-1]+1)
    else: 
        ls.append(ls[-1])

for q in range(Q):
    l, r = map(int, input().split())
    output.append(ls[r+1]-ls[l])
print(*output, sep="\n")

