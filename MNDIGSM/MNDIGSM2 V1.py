import math 

q = int(input())

def fector(n) :
    lst1 = []
    lst2 = []

    for i in range(1, int(math.sqrt(n) + 1)):
        if (n % i == 0) :
            temp = n//i
            if (temp == i) :
                    lst1.append(i)
            else :
                    lst1.append(i)
                    lst2.append(temp)
    lst1 += reversed(lst2)
    return lst1

def unsafe(lst,n,r):
    traveller = len(lst)-1
    riski = -1
    l = 2

    for i in range(len(lst)):
        if riski == -1 and lst[traveller]<l and traveller != len(lst)-1 and lst[traveller+1] != l :
            riski = 0
            traveller -= 1
            continue

        if lst[traveller] < l or lst[traveller] > r:
            del lst[traveller]
        traveller -= 1
        
    return riski, lst

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
    n,r = map(int,input().split())
    
    minimum = 1e20
    min2 = 1e20

    # in n is present in range of l and r, min sum = 1 and min base = n
    if 2<=n and n<=r:
        print(n)
        continue

    lst = fector(n)
    riski, lst = unsafe(lst,n,r)

    if len(lst) == 0:
        for base in range(2,min(n+1,r+1)):
            sum = sumofdigits(n,base,minimum)           
            if sum<minimum:
                minimum = sum
                minbase = base
            if minimum == 1:
                break

        if r+1 > n:
            if n < minimum:
                minimum = n
                tempminbase = n+1

    
    else:
        for base in lst[1:]: #  for base in lst
            sum = sumofdigits(n,base,minimum)         
            if sum<minimum:
                minimum = sum
                minbase = base
            if minimum == 1:
                break
        
        sum = sumofdigits(n,lst[0],minimum)
        if sum<minimum:
            if riski != 0:
                minimum = sum
                minbase = lst[0]

            else:
                tempmin = 1e20
                tempminbase = -1
                
                for base in range( 2,min(n+1,lst[1]) ):
                    tempsum = sumofdigits(n,base,tempmin)           
                    if tempsum<tempmin:
                        tempmin = tempsum
                        tempminbase = base
                    if tempmin == 1:
                        break

                if lst[1] > n:
                    if n < tempmin:
                        tempmin = n
                        tempminbase = n+1
                
                if tempmin < minimum:
                    minimum = tempmin
                    minbase = tempminbase
                               
    print(minbase)




