#include<iostream>
using namespace std;

int main()
{
	int a, b, n, w; //양 사료, 염소 사료, 마리수, 사료량
	cin >> a >> b >> n >> w;
	int x, y, lx,ly;
	if (a != b)
	{
		x = (w - (b * n)) / (a - b);
		y = (w - (a * n)) / (b - a);
		lx = (w - (b * n)) % (a - b);
		ly = (w - (a * n)) % (b - a);

		if (x <= 0 || y <= 0 || lx * ly != 0)
		{
			cout << -1;
			return 0;
		}
		cout << x << '\n' << y;
	}
	else
	{
		if (n * a != w)
		{
			cout << -1;
			return 0;
		}
		else
		{
			if (n == 2)
			{
				cout << 1 << ' ' << 1;
				return 0;
			}
			cout << -1;
			return 0;
		}
	}
}