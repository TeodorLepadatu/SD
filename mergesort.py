def merge(v, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = v[l + i] 
    for j in range(0, n2):
        R[j] = v[m + 1 + j]
    #print(L)
    #print(R)
    i = 0     
    j = 0     
    k = l     
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            v[k] = L[i]
            i += 1
        else:
            v[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        v[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        v[k] = R[j]
        j += 1
        k += 1

def mergesort(v, l, r):
    if l < r:
        m = (r+l)//2
        mergesort(v, l, m)
        mergesort(v, m+1, r)
        merge(v, l, m, r)

v=[int(x) for x in input().split()]
#merge(v,0,int((len(v)-1)/2),len(v)-1)
mergesort(v,0,len(v)-1)
print(v)