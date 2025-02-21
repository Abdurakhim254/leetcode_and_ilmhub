#include<stdio.h>
int countOnes(int x)
{
    int count=0;
  while(x){
    if(x%2!=0){
        count+=1;
    }
    x=x/2;
  }
  return count;
}
int main() 
{
  int n;
  scanf("%d",&n);
  int s=countOnes(n);
  printf("%d",s);
  return 0;
}
