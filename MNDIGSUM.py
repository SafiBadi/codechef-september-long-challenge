def reVal(num):
 
    if (num >= 0 and num <= 9):
        return chr(num + ord('0'));
    else:
        return chr(num - 10 + ord('A'));
 
def fromDeci(res, base, inputNum):
    while (inputNum > 0):
        res+= reVal(inputNum % base);
        inputNum = int(inputNum / base);
    res = res[::-1]; 
    return res;

q = input()
q = int(q)
for i in range(q):
    n,l,r = map(int,input().split())
    #print(n,l,r)
    
    min = None
    minbase = None 
    for j in range(l,r+1):
        res = "";
        num = fromDeci(res, j, n)

        sum = 0
        for i in num:
            sum += int(i)
        #print(num)
        #print(sum)

        if min is None:
            min = sum
            minbase = j
        else:
            if sum<min:
                min = sum
                minbase = j
    print(minbase)
    
    
