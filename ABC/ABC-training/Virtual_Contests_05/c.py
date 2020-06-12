
A, B = map(int, input().split())
count = 0
count_a = A//4 - A//100 + A//400
count_b = B//4 - B//100 + B//400


if ((A%4==0) & (B%100!=0)) | (A%400==0):
    print(count_b-count_a+1)
else:
    print(count_b-count_a)

# 最初から下のように区間で考えようとするとかなりめんどくさくなる
"""
A, B = map(int, input().split())
count = 0
if A==B:
    if ((A%4==0) & (A%100!=0)) | (A%400==0):
        count += 1
    else: count += 0

    print(count)
    exit()


# ここでB-A >= 4かどうかの判定が必要
if B-A >= 4:
    if (A%4==0) | (B%4==0):
        count = (B-A) // 4 +1
    else:
        count = (B-A) // 4

else:
    for i in range(A, B+1):
        if i%4 == 0:
            count += 1
 


start_100 = A + (100 - A%100)
if start_100 <= B: 
    count_100 = (B-start_100) // 100 + 1
else: count_100 = 0

#print(count_100)

start_400 = A + (400 - A%400)
if start_400 <= B: 
    count_400 = (B-start_400) // 400 + 1
else: count_400 = 0

#print(count_400)

print(count - count_100 + count_400)
"""



