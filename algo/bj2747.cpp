#include<stdio.h>

int fibo(int);

int main()
{
	int num,result;
	scanf("%d", &num);
	result = fibo(num);
	printf("%d\n",result);
	return 0;
}

int fibo(int num)
{
	if(num <2)
	{
		return num;
	}
	return fibo(num-1)+fibo(num-2);
}
