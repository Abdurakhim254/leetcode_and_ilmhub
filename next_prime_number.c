#include<stdio.h>
#include<stdbool.h>
int main(){
    int a;
    scanf("%d",&a);
    int count1=0,count2=1;
    bool check=true;

    while (check)
    {
        count1=0;
        for(int i=1;i<=a;i++){
            if(a%i==0){
                count1++;
            }
        }
        if(count1==2){
            printf("%d",a);
            check=false;
        }else{
            a++;
        }   
    }
    return 0;
}