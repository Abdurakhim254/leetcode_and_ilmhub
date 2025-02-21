#include<stdio.h>
int get_day(int a,int b){
	switch(b){
      case 1: return 31;
      case 2: return 29;
      case 3: return 31;
      case 4: return 30;
      case 5: return 31;
      case 6: return 30;
      case 7:
      case 8:
       		 return 31;
      case 9: return 30;
      case 10: return 31;
      case 11: return 30;
      case 12: return 31;
    }

}
int main(){
	int a,b;
  	scanf("%d %d",&a,&b);
  	if(a>0 && (b>0 && b<=12)){
    
     int s=get_day(a,b);
     printf("%d ",s); 
    }
	
	return 0;
}