def permute(a, l, r):
    if l == r:
        print(a)
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]
string = list('ABC')
permute(string, 0, len(string))

