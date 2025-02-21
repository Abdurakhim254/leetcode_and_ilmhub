#include<stdio.h>
int check(int a){
    switch(a){
        case 13:
        a=1;
        break;
        case 14:
        a=4;
        break;
        case 15:
        a=3;
        break;
        case 16:
        a=4;
        break;
        case 17:
        a=5;
        break;
        case 18:
        a=6;
        break;
        case 19:
        a=7;
        break;
        case 20:
        a=8;
        break;
        case 21:
        a=9;
        break;
        case 22:
        a=10;
        break;
        case 23:
        a=11;
        break;
        case 24:
        a=12;

    }
    return a;
}
int main(){
	int a,b;
  	scanf("%d:%d",&a,&b);
  	if(a<=12 && b<=60){
      printf("%2d:%02d AM",a,b); 
    } 
    else {
        int s=check(a);
        printf("%2d:%02d PM",s,b); 
    }

	return 0;
}