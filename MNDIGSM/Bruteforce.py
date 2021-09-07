n = 787989554645

l = 2
r = 7879895

previoumin = 1e20

sum = 0
previoussum = 1e20

lastbreakout = 0
miniimum = 1e20
minbase = 0

for base in range(l,r):
    num = n
    sum = 0
    
    while num>0:
        sum += num%base
        num = num//base

    if sum>previoussum and  n%(base-1) != 0:
        lastbreakout = base-1

    if sum<miniimum:
        miniimum = sum
        minbase = base

    print(n,"\t",base,"\t",n%base,"\t",sum,"\t",miniimum,minbase)

    #if n % (base-1) == 0 and base<chamatkar+1:
        #checker = (base -1)*2   

    #elif  n % (base-1) == 0 and base>=chamatkar:
        #checker = base -1    

    #elif n % (base) > n % (base-1):
        #checker = (base -1 ) + n % (base-1)

    #elif n % (base) < n % (base-1) and base<chamatkar:
        #checker = (base -1 ) + n % (base-1)

    #else:
        #checker = n % (base-1)

    if (n % (base) ) >= (n % (base-1) ):
        checker = (base -1 ) + n % (base-1)
    else:
        checker = n % (base-1)

    #if checker != sum:
        #print("Observation is wrong :",checker)
        #break

    #if sum<8:
        #break


    previoussum = sum
    