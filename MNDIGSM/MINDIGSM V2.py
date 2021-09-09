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

def unsafe(lst,n,l,r):
    traveller = len(lst)-1
    risk = False

    for i in range(len(lst)):
        if risk == False and lst[traveller]<l and traveller != len(lst)-1 and lst[traveller+1] != l : # last comparison is l not 1
            risk = lst[traveller]

        if lst[traveller] < l or lst[traveller] > r:
            del lst[traveller]
        traveller -= 1

    if len(lst) == 0:
        risk = True

    return risk, lst

def sumofdigits(num,base,minimum):
    sum = 0
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
    if n>=l and n<=r:
        print(n)
        continue

    # if l and r both greater than n, min sum = n and min base = anu of l,l+1....r
    if l>n:
        print(l)
        continue

    lst = fector(n)
    risk, lst = unsafe(lst,n,l,r)

    for base in lst:
        sum = sumofdigits(n,base,minimum)         
        if sum<minimum:
            minimum = sum
            minbase = base
        if minimum == 1:
            break

    if risk is not False:
        if len(lst) != 0:
            if sumofdigits(n,risk,minimum) < minimum:
                for base in range( l, lst[0] ):
                    sum = sumofdigits(n,base,minimum)         
                    if sum<minimum:
                        minimum = sum
                        minbase = base
                    if minimum == 1:
                        break
        
        else:
            for base in range( l, min(r,n) + 1 ):
                sum = sumofdigits(n,base,minimum)         
                if sum<minimum:
                    minimum = sum
                    minbase = base
                if minimum == 1:
                    break

    if r>n and n<minimum:
        minimum = n
        minbase = r
                 
    print(minbase)




