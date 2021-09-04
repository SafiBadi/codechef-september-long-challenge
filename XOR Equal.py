t = int(input())

for i in range(t):
    n,x = map(int,input().split())
    a = list(map(int, input().split()))
    #print(a)

    dct =  dict()
    for i in a:
        dct[i] = dct.get(i,0) + 1

    mx = 0
    op = 0

    tempmx = 0
    tempop = 0

    for i in dct.keys():

        if i == 0:
            tempmx = dct[i]

            if tempmx >= mx:  
                mx = tempmx
                op = 0

        else:
            tempmx = dct[i] + dct.get(i^x,0)
       
            if tempmx == mx:   
                # Max remains same         
                if dct.get(i^x) is None:
                    tempop = 0
                else:
                    tempop = min( dct.get(i^x), dct[i] )
                op = min(op,tempop)

            elif tempmx > mx:
                mx = tempmx
                if dct.get(i^x) is None:
                    op = 0
                else:
                    op = min( dct.get(i^x), dct[i] )

    print(mx,op)