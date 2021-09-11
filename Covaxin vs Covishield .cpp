//TLE

#include <bits/stdc++.h>
using namespace std;

void sulution()
{
    int i,j=0;
    long long int x,a,b,c,d,p,q,r,s,t,m,money=0,count=0,temp=0,covaxine=0,covishield=0;
    
    scanf("%d",&i);
    scanf("%lld %lld %lld %lld %lld",&x,&a,&b,&c,&d);
    scanf("%lld %lld %lld %lld %lld %lld",&p,&q,&r,&s,&t,&m);
 
    for(j = 0; j<i; j++)
    {   
        covaxine = a;
        covishield = c;
        money = x;
        count = 0;
        while(money>0)
        {
            if (covaxine<covishield)
            {
                if (money - covaxine >= 0)
                {
                    money -= covaxine;
                    count++;
                    covaxine += b;
                }
                else
                {
                    break;
                }
            }
            else
            {
                if (money - covishield >= 0)
                {
                    money -= covishield;
                    count++;
                    covishield += d;
                }
                else
                {
                    break;
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

