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
    risk = False
    l = 2

    chamatkar = 1e20
    if len(lst)>0:
        chamatkar = lst[len(lst)//2]

    for i in range(len(lst)):
        if risk == False and lst[traveller]<l and traveller != len(lst)-1 and lst[traveller+1] != l : # last comparison is l not 1
            risk = True

        if lst[traveller] < l or lst[traveller] > r:
            del lst[traveller]
        traveller -= 1

    try:
        chamatkarindex = lst.index(chamatkar)
    except:
        chamatkarindex = len(lst)-1

    if len(lst) == 0:
        lst.append(r)
        risk = True

    return risk, chamatkarindex,chamatkar, lst

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

def sumafterchamatkar(n,base):
    sum = 0
    if n % (base-1) == 0:
        sum = base -1
    elif n % (base) > n % (base-1):
        sum = (base -1 ) + n % (base-1)
    else:
        sum = n % (base-1)
    return sum

def minofstartingelements(n,list0,chamatkar,minimum,minbase):
    for base in range( 2, min(n+1, list0+1) ):
        if base > chamatkar:
            sum = sumafterchamatkar(n,base)
        else:
            sum = sumofdigits(n,base,minimum) 
                      
        if sum<minimum:
            minimum = sum
            minbase = base
        if minimum == 1:
            return minimum, minbase
    
    if list0>n:
        if n < minimum:
            minimum = n
            minbase = r
    
    return minimum, minbase
        

for i in range(q):
    n,r = map(int,input().split())
    
    minimum = 1e20
    minbase = -1

    # in n is present in range of l and r, min sum = 1 and min base = n 
    if 2<=n and n<=r:
        print(n)
        continue

    lst = fector(n)
    risk, chamatkarindex,chamatkar, lst = unsafe(lst,n,r)

    for base in lst[:chamatkarindex]:
        sum = sumofdigits(n,base,minimum)         
        if sum<minimum:
            minimum = sum
            minbase = base
        if minimum == 1:
            break
    
    if minimum != 1:
        for base in lst[chamatkarindex:]:
            sum = sumafterchamatkar(n,base)
            if sum<minimum:
                minimum = sum
                minbase = base
            if minimum == 1:
                break

    tempbase = 0
    if risk is True:
        sum,tempbase = minofstartingelements(n,lst[0],chamatkar,minimum,minbase)
        
        if sum < minimum:
            minimum = sum 
            minbase = tempbase
                               
    print(minbase)




