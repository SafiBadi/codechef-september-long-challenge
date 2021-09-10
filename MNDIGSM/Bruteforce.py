n = 987654321
l = 153
r = 1000

minimum = 1e20
minbase  =-1
for base in range(l,r):
    num = n
    sum = 0
    
    while num>0:
        sum += num%base
        num = num//base


    print(n,base,"\t",n%base,"\t",sum)


    