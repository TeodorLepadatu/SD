def counting_sort(v):
    n = len(v)
    mx = max(v) + 1  
    f = [0] * mx
    out = []
    
    for i in range(n):
        f[v[i]] += 1
    
    for i in range(mx):
        while f[i] != 0:
            out.append(i)
            f[i] -= 1
    
    return out

v = [int(x) for x in input().split()]
print(counting_sort(v))
