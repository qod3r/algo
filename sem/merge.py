def merge_sort(a):
    l = len(a)
    if l <= 1:
        return a
    
    left, right = [], []
    for i in range(l):
        if i < l / 2:
            left.append(a[i])
        else:
            right.append(a[i])
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)


def merge(left, right):
    res = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left[0])
            left.pop(0)
        else:
            res.append(right[0])
            right.pop(0)
    
    while len(left) > 0:
        res.append(left[0])
        left.pop(0)
    while len(right) > 0:
        res.append(right[0])
        right.pop(0)
    
    return res