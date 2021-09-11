t = int(input())

def distance(p1,p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

for i in range(t):
    n, m = map(int,input().split())

    points = set()
    for i in range(m):
        for j in range(n):
            points.add((i,j))

    temp = 0
    record = dict()
    for i in points:
        for j in points:
            if j>i:
                temp = distance(i,j)
                record[temp] = record.get(temp,0) + 1

        print (record)

    ans = 0
    for i,ai in record.items():
        ans += (ai) * (31**(i-1))
        print(ans)

    print(ans%998244353)
