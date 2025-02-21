#include<stdio.h>
int main(){
    FILE *f=fopen("C:\\Users\\Asus Vivobook\\Desktop\\ oddiy.txt","a+");
    if (f==NULL){
        puts("False");
        return -1;
    }
    char s[]="Salom Dunyo naqadar go'zalsan";
    fprintf(f,"%s\n",s);
    fclose(f);
    // f=fopen("C:\\Users\\Asus Vivobook\\Desktop\\ oddiy.txt","r");
    system("start C:\\Users\\Asus Vivobook\\Desktop\\ oddiy.txt");    
    return 0;
}