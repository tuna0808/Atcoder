def binary_search_low(ls, v):
    """
    ・基準(v)より小さい値が配列の中に何個あるか, 二分探索によって見つける.
    [input]
        ls: 二分探索するリスト(配列)
        v: 探索の基準となる値
    [output]
        return: 基準を満たす配列の要素数
    """
    ok = -1
    ng = n

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if ls[mid] < v: ok = mid
        else: ng = mid
        
    return ok+1
    
def binary_search_high(ls, v):
    """
    ・基準(v)より大きい値が配列の中に何個あるか, 二分探索によって見つける.
    [input]
        ls: 二分探索するリスト(配列)
        v: 探索の基準となる値
    [output]
        return: 基準を満たす配列の要素数
    """
    ng = -1
    ok = n

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if ls[mid] > v: ok = mid
        else: ng = mid
        
    return len(ls) - ok


n = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))
ans = 0

for b in B:
    a_count = binary_search_low(A,b)
    b_count = binary_search_high(C, b)
    ans += a_count*b_count

print(ans)


