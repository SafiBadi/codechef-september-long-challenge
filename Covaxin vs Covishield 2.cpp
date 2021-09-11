//WA

#include <bits/stdc++.h>
using namespace std;

void sulution()
{
    int i,j=0;
    long long int x,a,b,c,d,p,q,r,s,t,m,money=0,count=0,temp=0,faster=0,slower=0,fr=0,sr=0,jump=0;
    
    scanf("%d",&i);
    scanf("%lld %lld %lld %lld %lld",&x,&a,&b,&c,&d);
    scanf("%lld %lld %lld %lld %lld %lld",&p,&q,&r,&s,&t,&m);
 
    for(j = 0; j<i; j++)
    {   
        if (b>d)
        {
            faster = a;
            slower = c;
            fr = b;
            sr = d;
        }
        else
        {
            faster = c;
            slower = a;
            fr = d;
            sr = b;
        }
        
        money = x;
        count = 0;
        while(faster < slower && money>0)
        {
            if (money - faster >= 0)
            {
                count++;
                money -= faster;
                faster += fr;
            }
            else
            {
                break;
            }
        }
       
        if (money >= faster || money>= slower)
        {
            while (1)
            {
                jump = ( (faster*sr) +  ( ( (sr-1)*(sr-1+1) ) / 2 ) * fr) +
                       ( (slower*fr) +  ( ( (fr-1)*(fr-1+1) ) / 2 ) * sr);
                   
                if ( (money - jump) >=0 )
                {
                    count += (fr + sr);
                    money -= jump;
                    faster += (fr * sr);
                    slower += (sr * fr);
                }
                else
                {
                    break;
                }
            }
            
        }
        
        if (money >= faster || money>= slower)
        {
            while (1)
            {   
                if (slower < faster)
                {
                    if ( (money - slower) >= 0  )
                    {
                        count++;
                        money -= slower;
                        slower += sr;
                    }
                    else
                    {
                        break;
                    }
                }
                else
                {
                    if ( (money - faster) >=0 )
                    {
                        count++;
                        money -= faster;
                        faster += fr;
                    }
                    else
                    {
                        break;
                    }
                }
            }
        }
        
        printf("%lld \n",count);
        
        temp = count*t;
        
        a = ( (a + temp) % m ) + p;
        b = ( (b + temp) % m ) + q;
        c = ( (c + temp) % m ) + r;
        d = ( (d + temp) % m ) + s;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    sulution();
    return 0;
}

