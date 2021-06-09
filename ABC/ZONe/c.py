N = int(input())
specs = []

for n in range(N):
    spec = list(map(int, input().split()))
    specs.append(spec)

# ②2分探索の中で, チームの総合力をX以上にできるかを判定する関数を定義
def ok(x):
    exist = [False]*(1<<5) # 5bit分の２進数を保持しておくようのリスト. ２進数を10進数に変換した時に32個なので32個のリストとして管理. これによって, 存在する
    for spec in specs: # N=3000回最大で回る
        binary = 0 # ある人の各スペックがXを超えているかを保持する. 2進数に変換して, 論理和を取ることで実現
        for i in range(5):
            if spec[i] >= x:
                y = 1 << i # 1を２進数に変換してiビット分ずらす = 2進数にした時iビット目が立ってるような数yを実現
                binary = binary | y # binaryとiビット目が立ってるyとの論理和を取ることで, 
        exist[binary] = True

    for i in range(1 << 5): # 高々2**5通りの5bitの01の組み合わせしかないので, その32通りの中から3つ選ぶということをする. その際に, そのbit列(例えば10101とか)がN人の中に存在したかどうかを確認するためにさっきexist[binary(=10101)]を作った.
        #なので, exist[i],exist[j],exist[k]というスキルが存在して, かつ, そのi,j,kの論理和が11111に等しければX以上を実現可能ということ.
        for j in range(1 << 5): # 同じ人は選ばないからrange(j+1, 1<<5)でもいい
            for k in range(1 << 5):
                if exist[i] and exist[j] and exist[k] and (i | j | k)==(1<<5)-1: #今32C3とってきた3つの組み合わせ全ての5bitの2進数が, N人の選手のスペックを5bitに変換したもののなかにまずあるかどうかを判定→exist[i] and exist[j] and exist[k]. その後, i,j,kの論理和が11111になっているかを判定.
                    return True # なっているならそれは実現できるのでTrueをreturn
    return False # N人の選手の持つ5bitの組み合わせ(高々32通り)のどれでも11111を実現できなければそれは無理ってことでFalseをreturn
                



bottom, top = 1, 10**10

# ①大枠の二分探索, チームの総合力がX以上にできるかを調べる(この設定だとO(log10**10)かな?)
while top-bottom > 1:
    mid = (top+bottom) // 2
    if ok(mid): bottom = mid
    else: top = mid

# 最終的に実現可能なチームの最大値は2分探索した時の下界であるbottom
print(bottom)
