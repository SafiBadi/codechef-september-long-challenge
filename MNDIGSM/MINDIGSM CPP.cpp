#include <bits/stdc++.h>
using namespace std;

void sulution()
{
    int q, n, l, r, num = 0, sum=0, minimum = INT_MAX, minbase = -1;
    
    cin >> q;
    for (int i = 0; i < q; i++) 
    {
        cin >> n >> l >> r;
        
        if (n >= l && n <= r) 
        {
            cout << n << "\n";
            continue;
        }
        
        if (n < l) 
        {
            cout << l << "\n";
            continue;
        }
    
        minimum = INT_MAX;
        minbase = 0;
        sum = 0;
       
        while (l < r && n / r < r) 
        {
            int digit1 = n / r;
            int digit2 = n % r;
            
            sum = digit1 + digit2;
            if (sum < minimum) 
            {
                minimum = sum;
                minbase = r;
            }
            
            r = n / (digit1 + 1);
        }
        
        while (l <= r) 
        {
            num = n;
            sum = 0;
            
            for (;;) 
            {
                if (num < l) 
                {
                    sum += num;
                    if (sum < minimum) 
                    {
                        minimum = sum;
                        minbase = l;
                    }
                    break;
                }
                sum += num % l;
                num /= l;
                if (sum >= minimum)
                {   
                    break;
                }
            }
            l++;
        }
        cout <<  minbase <<  "\n";
    }
};

int main() {
    
    sulution();
    
    return 0;
}