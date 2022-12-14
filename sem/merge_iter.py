def merge_sort(a):
    width = 1
    n = len(a)
    step = 1
    while width < n:
        l = 0
        while (l < n):
            r = min(l + (width * 2 - 1), n - 1)
            m = min(l + width - 1, n - 1)
            print(f"step: {step}")
            merge(a, l, m, r)
            step += 1
            l += width * 2
        
        width *= 2
    
    return a


def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1 
    R = [0] * n2 
    for i in range(0, n1): 
        L[i] = a[l + i] 
    for i in range(0, n2): 
        R[i] = a[m + i + 1] 
    print(L, R)
    i, j, k = 0, 0, l 
    while i < n1 and j < n2: 
        if L[i] <= R[j]: 
            a[k] = L[i] 
            i += 1
        else: 
            a[k] = R[j] 
            j += 1
        k += 1
  
    while i < n1: 
        a[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        a[k] = R[j] 
        j += 1
        k += 1
