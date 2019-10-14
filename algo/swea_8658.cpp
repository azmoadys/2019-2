//https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AW1lwyh6WPwDFARC
#include<iostream>
 
using namespace std;
 
int main(int argc, char** argv)
{
    int test_case;
    int T;
    cin >> T;
    for (test_case = 1; test_case <= T; ++test_case)
    {
        int num[10];
        for (int i = 0; i < 10; i++)
            cin >> num[i];
        int max, min;
        for (int i = 0; i < 10; i++)
        {
            int sum = 0;
            while (num[i]!=0)
            {
                sum += num[i] % 10;
                num[i] = num[i]/10;
            }
            if (i == 0)
            {
                max = sum;
                min = sum;
            }
            else
            {
                if (sum > max)
                    max = sum;
                else if (sum < min)
                    min = sum;
            }
        }
        cout << "#" << test_case << " " << max << " " << min << "\n";
    }
    return 0;
}
