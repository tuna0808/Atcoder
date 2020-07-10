def count_x(x):
    """
    O(logx)
    """
    if x == 1: return 1
    return 2*count_x(x//2)+1
    

print(count_x(int(input())))
