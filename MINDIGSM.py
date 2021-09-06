q = int(input())

def sumofdigits(num,base,minimum):
    sum = 0
    if base>num:
        return num
    else:
        while num>0:
            sum += num%base
            num = num//base
            if sum>minimum:
                break
    return sum

for i in range(q):
    n,l,r = map(int,input().split())
    
    minimum = 1e20
    minbase = -1 

    # in n is present in range of l and r, min sum = 1 and min base = n
    if l<=n and n<=r:
        print(n)
        continue

    # if l and r both greater than n, min sum = n and min base = l,l+1....r
    if l>n and r>n:
        print(l)
        continue

    for base in range(l,min(n,r)+1):
        sum = sumofdigits(n,base,minimum)
        if sum<minimum:
            minimum = sum
            minbase = base

    if l>n:
        if l < minimum:
            minbase = l 
    
    print(minbase)




