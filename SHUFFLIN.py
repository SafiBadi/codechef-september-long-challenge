t = int(input())

for i in range(t):
    n = input()
    #a = map(int,input().split())
    a = list(input().split())
    #print(a)

    on = 0
    en = 0
    for num in a:
        if int(num)%2 == 1:
            on += 1
        else:
            en += 1
    
    ep = len(a)//2
    op = len(a)-ep
    #print(on,ep,en,op)
    print(min(on,ep)+min(en,op))