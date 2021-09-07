import math

n = 4137357113711
l = 2
r = 4137357113
sqrt = math.floor( math.sqrt(n) )

miniimum = 1e20
minbase = 0

for base in range(2,sqrt):
    num = n
    sum = 0
    
    while num>0:
        sum += num%base
        num = num//base
    
    if sum<miniimum:
        miniimum = sum
        minbase = base
        #print(sum,minbase)

for base in range(sqrt,r):
    num = n
    sum = 0

    if (n % (base) ) >= (n % (base-1) ):
        sum = (base -1 ) + n % (base-1)
    else:
        sum = n % (base-1)

    if sum<miniimum:
        miniimum = sum
        minbase = base
        #print(sum,minbase)

print(miniimum,minbase)
    