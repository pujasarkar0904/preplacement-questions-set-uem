#include<stdio.h>
int main(){
    int  choice;
    float temp,result;
    printf("1. celcius to farenheit");
    printf("2.farenheit to celcius\n");
    scanf("%d",&choice);
    printf("enter temp:");
    scanf("%f",&temp);
    if (choice==1){
        result= (temp*9/5)+32;
        printf("%.1f F",result);
    }
    else if(choice==2){
        result=(temp-32)*5/9;
        printf("%.1f c ",result);
    }
    else{
        printf("invalid choice");
    }
    return 0;
    }
    


