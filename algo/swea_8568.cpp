//https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AW1B8rJq3NUDFARC
#include<iostream>
#include<vector>
using namespace std;
 
int main(int argc, char** argv)
{
    int test_case;
    int T;
    cin >> T;
    for (test_case = 1; test_case <= T; ++test_case)
    {
        int N;
        cin >> N;
        vector<int> p;
        vector<int> wrong;
        wrong.assign(3, 0);
        p.assign(N, 0);
        for (int i = 0; i < N; i++)
        {
            cin >> p[i];
        }
        bool finish = false;
        bool change = false;
        int result = 0;
        for (int i = 0; i < N-1; i++)
        {
            change = false;
            if (p[i] % 3 == (i+1) % 3)
                continue;
            for (int j = i+1; j < N; j++)
            {
                if (p[j] % 3 == (j+1) % 3)
                    continue;
                if (p[i] % 3 == (j+1) % 3 && p[j] % 3 == (i+1) % 3)
                {
                    int temp1 = p[j];
                    p[j] = p[i];
                    p[i] = temp1;
                    change = true;
                    result++;
                    break;
                }
            }
            if (change == false)
            {
                for (int j = i+1; j < N; j++)
                {
                    if (p[j] % 3 == (j+1) % 3)
                        continue;
                    if (p[j] % 3 == (i + 1) % 3)
                    {
                        int temp1 = p[j];
                        p[j] = p[i];
                        p[i] = temp1;
                        change == true;
                        result++;
                        break;
                    }
                }
            }
        }
        cout << "#"<<test_case<<" " << result << "\n";
    }
    return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
