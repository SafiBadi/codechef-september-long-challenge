import math

def sumofdigits(num,base,minimum):
    sum = 0
    while num>0:
        sum += num%base
        num = num//base
        if sum>minimum:
            break
    return sum

def primemin(n,l,r):

    sqrt = math.ceil( math.sqrt(n) )

    minimum = 1e20
    minbase = 0

    currentdigit = (math.floor(math.log(n) / math.log(l)) + 1)
    base = l
    if l<sqrt:
        while (math.floor(math.log(n) / math.log(base)) + 1) == currentdigit and base<sqrt:
            print("1",base,end=" ")

            sum = sumofdigits(n,base,minimum)           
            if sum<minimum:
                minimum = sum
                minbase = base
            print(minbase)
            base +=1

            if base == r:
                return minbase

    
        for base in reversed(range(base,min(sqrt,r+1))):
            print("2")
            sum = 0
            
            dig = (math.floor(math.log(n) / math.log(base)) + 1)
            
            if dig > currentdigit:
                currentdigit = dig
            
                sum = sumofdigits(n,base,minimum)          
                if sum<minimum:
                    minimum = sum
                    minbase = base

    for base in range(min(base,r+1),r+1):
        print("3")
        num = n
        sum = 0

        if (n % (base) ) >= (n % (base-1) ):
            sum = (base -1 ) + n % (base-1)
        else:
            sum = n % (base-1)

        if sum<minimum:
            minimum = sum
            minbase = base

    return minbase

n = 100148544
l = 10047576
r = 20056464

aa = primemin(n,l,r)
print(aa)