#include<iostream>

using namespace std;

int main()
{
    int t_case, i;
    long long n1, n2, n3, sum;
    cin >> t_case;
    for(i=0;i<t_case;i++)
    {
        cin >> n1 >>n2>>n3;
        sum = n1+n2+n3;
        cout << sum/2<<'\n';
    }
    return 0;
}
