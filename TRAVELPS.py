t = int(input())

for i in range(t):
    n,a,b = map(int,input().split())
    str = input()

    dict = 0
    st = 0

    for i in str:
        if i == "0":
            dict += 1
        else:
            st += 1
    print((dict*a) + (st*b))