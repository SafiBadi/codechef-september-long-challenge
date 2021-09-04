q = int(input())

def utility(n):

    if (n >= 0 and n <= 9):
        return chr(n + ord('0'));
    else:
        return chr(n - 10 + ord('A'));

def converter(result, base, num):
    while (num > 0):
        result+= utility(num % base);
        num = int(num / base);
    result = "".join(reversed(result))
    return result;

for i in range(q):
    n,r = map(int,input().split())
    #print(n,l,r)
    
    min = None
    minbase = None 
    for j in range(2,r+1):
        result = "";
        num = converter(result, j, n)

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




