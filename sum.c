#include<stdio.h>
int add(int x, int y) 
{
    if(x==0){
        return y;
    }
    y+=x;
    x-=1;
    return add(x,y);
}

int main() 
{
 int a;
 int b=0;
 scanf("%d",&a);
 int s=add(a,b);
 printf("%d",s);
  return 0;
}
