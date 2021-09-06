
number  = 21
sum = 0

for base in range(2,number+100):
    num = number
    sum = 0
    

    while num>0:
        sum += num%base
        num = num//base

    if number%base == 0:
        print(number,"\t",base,"\t\t",number%base,"\t",sum)
    