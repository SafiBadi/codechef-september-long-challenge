q = int(input()) 

for i in range(q):
    n,l,r = map(int,input().split())
    
    minimum = 1e20
    minbase = -1

    # in n is between l and r, n can be represented as 10 in base n, Therefor min sum = 1 for min base = n
    if n>=l and n<=r:
        print(n)
        continue

    # if l and r both greater than n, min sum = n and min base = any of l,l+1,l+2....r
    if l>n:
        print(l)
        continue

    while (l<r and ((n//r) <r)):
        digit1 = n//r
        digit2 = n%r

        sum = digit1 + digit2
        if sum < minimum:
            minimum = sum
            minbase = r
            if minimum == 1:
                break

        r = n//(digit1+1)

    if minimum > 1:
        for base in range(l,int(r+1)):
            num = n
            sum = 0

            while True:
                if num<l:
                    sum += num
                    if sum < minimum:
                        minimum = sum
                        minbase = base
                    break

                sum += num % base
                num = num // base
                if sum>minimum:
                    break

            if minimum == 1:
                break

    print(minbase)




'''
1   
987654321 55 46876

'''