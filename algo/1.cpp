#include<iostream>
using namespace std;

int main()
{
	long long n;
	cin >> n;
	int cnt = 0; //1ÀÇ °¹¼ö
	long long sum = 1, temp; //ÇÕ
	while (true)
	{
		if (n <= sum)
			break;
		cnt++;
		temp = cnt+1;
		sum = temp + 1 * cnt;
		for(int i=0;i<cnt;i++)
		{
			sum += 2 * temp;
			temp = 2 * temp;
		}
	}
	cout << cnt;
	return 0;
}
