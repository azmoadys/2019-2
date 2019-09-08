#include<stdio.h>
void sort(int *a, int *b, int *c);
void swap(int *a, int *b);
int main(void)
{
    int a,b,c;
    scanf("%d %d %d", &a, &b, &c);
    sort(&a, &b, &c);
    printf("%d %d %d\n", a,b,c);    
    return 0;
}

void sort(int *a, int *b, int*c)
{
    if(*a > *b)
    {swap(a, b);}
    if(*b>*c){
    swap(b, c);}
    if(*a> *c){
    swap(a, c);}
    if(*a > *b)
    {swap(a, b);}
    if(*b>*c){
    swap(b, c);}
    if(*a> *c){
    swap(a, c);}

}

void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

