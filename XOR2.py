t = int(input())

for i in range(t):
    n,x = map(int,input().split())
    a = list(map(int, input().split()))

    dct1 =  dict()
    for i in a:
        dct1[i] = dct1.get(i,0) + 1

    dct2 = dict()
    for i in dct1:
        if x==0:
            dct2[i] = 0
        else:
            dct2[i] = dct1.get(i^x,0)

    mx = 0
    op = 1e10
    for k,v in dct1.items():
        if v + dct2[k] == mx and dct2[k]<op:
            mx = v + dct2[k]
            op = dct2[k]
        elif v + dct2[k] > mx:
            mx = v + dct2[k]
            op = dct2[k]

    print(int(mx),int(op))