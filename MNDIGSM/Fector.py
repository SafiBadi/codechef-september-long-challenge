import math 

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

    

n = 500
l = 55
r = 84745645656565

a1 = fector(n)
print(a1)

riski, lst = unsafe(a1,n,l,r)
#print(riski)
#print(lst)

 