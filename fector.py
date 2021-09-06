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
    riski = -1

    for i in range(len(lst)):
        if riski == -1 and lst[traveller]<l and traveller != len(lst)-1 and lst[traveller+1] != l :
            riski = 0
            traveller -= 1
            continue

        if lst[traveller] < l or lst[traveller] > r:
            del lst[traveller]
        traveller -= 1
        
    return riski, lst

    

n = 246821571333
l = 2100565645
r = 235448989889

a1 = fector(n)
print(a1)

riski, lst = unsafe(a1,n,l,r)
print(riski)
print(lst)

 