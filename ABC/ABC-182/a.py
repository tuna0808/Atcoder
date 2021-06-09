
A, B = map(int, input().split())
tmp = 2*A+100
print(tmp-B)

"""
・print(input.split())はリストになる
・map(int, input().split())でmapを被せたままだとmapobjectになる(以下でroopさせると出力は可能)ので, list()でリストに変換するべき.
for i in map(int, input().split()):
    print(i)
"""