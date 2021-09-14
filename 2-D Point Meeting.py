class point:

    def __init__(self,x,y):
            self.x = float(x)
            self.y = float(y)

    def vertical(self):
        a = 1
        b = 0
        c = -self.x
        return a,b,c

    def horizontal(self):
        a = 0
        b = 1
        c = -self.y
        return a,b,c
    
    def dig1(self):
        a = 1
        b = 1
        c = -( self.x + self.y )
        return a,b,c

    def dig2(self):
        a = 1
        b = -1
        c = -self.x + self.y
        return a,b,c

def intersect(p1,p2):
    a1 = p1[0]
    b1 = p1[1]

    a2 = p2[0]
    b2 = p2[1]

    # if both lines are vertical they don't intersect
    if b1 == 0 and  b2 == 0:
        return False
    # if only any of the one line is vertical then they intersect
    if b1 == 0 or b2 == 0:
        return True

    # if both lines are perallen they don not intersect, 
    # else intersact
    if (a1/b1) == (a2/b2):
        return False
    else:
        return True

def intersectionpoint(l1,l2):
    a1 = l1[0]
    b1 = l1[1]
    c1 = l1[2]

    a2 = l2[0]
    b2 = l2[1]
    c2 = l2[2]

    a1b2_minus_a2b1 = ((a1*b2) - (a2*b1))
    x = ((b1*c2) - (b2*c1)) / a1b2_minus_a2b1
    y = ((c1*a2) - (c2*a1)) / a1b2_minus_a2b1

    if x == 0:
        x = 0
    if y == 0:
        y = 0

    return (x,y)

def update(dct,ip,p1,p2):
    if dct.get(ip,0) == 0:
        dct[ip] = {(p1.x,p1.y),(p2.x,p2.y)}
    else:
        dct[ip].add((p1.x,p1.y))
        dct[ip].add((p2.x,p2.y))

t = int(input())

for q in range(t):
    n = int(input())

    x = list(map(int,input().split()))
    y = list(map(int,input().split()))

    dct = dict()

    for i in range(len(x)):
        x1 = x[i]
        y1 = y[i]

        p1 = point(x1,y1)
        if dct.get((p1.x,p1.y),0) == 0:
            dct[(p1.x,p1.y)] = {(p1.x,p1.y)}
        #print (dct,"\n")

        for j in range(len(x)):
            if i ==j:
                continue

            x2 = x[j]
            y2 = y[j]

            p2 = point(x2,y2)

            # Horizontal ######################################################################
            if intersect(p1.horizontal(),p2.vertical()):
                ip = intersectionpoint(p1.horizontal(),p2.vertical())
                update(dct,ip,p1,p2)    

            if intersect(p1.horizontal(),p2.dig1()):
                ip = intersectionpoint(p1.horizontal(),p2.dig1())
                update(dct,ip,p1,p2)

            if intersect(p1.horizontal(),p2.dig2()):
                ip = intersectionpoint(p1.horizontal(),p2.dig2())
                update(dct,ip,p1,p2)

            # Vertical ######################################################################
            if intersect(p1.vertical(),p2.horizontal()):
                ip = intersectionpoint(p1.vertical(),p2.horizontal())
                update(dct,ip,p1,p2)

            if intersect(p1.vertical(),p2.dig1()):
                ip = intersectionpoint(p1.vertical(),p2.dig1())
                update(dct,ip,p1,p2)

            if intersect(p1.vertical(),p2.dig2()):
                ip = intersectionpoint(p1.vertical(),p2.dig2())
                update(dct,ip,p1,p2)

            # dig1 ######################################################################
            if intersect(p1.dig1(),p2.horizontal()):
                ip = intersectionpoint(p1.dig1(),p2.horizontal())
                update(dct,ip,p1,p2)

            if intersect(p1.dig1(),p2.vertical()):
                ip = intersectionpoint(p1.dig1(),p2.vertical())
                update(dct,ip,p1,p2)

            if intersect(p1.dig1(),p2.dig2()):
                ip = intersectionpoint(p1.dig1(),p2.dig2())
                update(dct,ip,p1,p2)

            # dig2 ######################################################################
            if intersect(p1.dig2(),p2.horizontal()):
                ip = intersectionpoint(p1.dig2(),p2.horizontal())
                update(dct,ip,p1,p2)

            if intersect(p1.dig2(),p2.vertical()):
                ip = intersectionpoint(p1.dig2(),p2.vertical())
                update(dct,ip,p1,p2)

            if intersect(p1.dig2(),p2.dig1()):
                ip = intersectionpoint(p1.dig2(),p2.dig1())
                update(dct,ip,p1,p2)

    maximum = -1
    maxkey = - 1

    #print(dct)
    for k,v in dct.items():
        if len(v) == maximum:
            if k in v:
                maxkey = k
        elif len(v) > maximum:
            maximum = len(v)
            maxkey = k

    if maxkey in dct[maxkey]:
        ans = (len(dct[maxkey]) - 1) + ( ( len(x) - len(dct[maxkey]) )*2 )
    else:
        ans = (len(dct[maxkey])) + ( ( len(x) - len(dct[maxkey]) )*2 )

    print(ans)
            



