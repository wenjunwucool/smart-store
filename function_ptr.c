#include<stdio.h>

typedef int (*p)(int x ,int y);
int get_max(int x,int y)
{
    return (x>y? x:y); 
}

int get_min(int x ,int y)
{
    return(x<y? x:y);
}

int get_value(int x,int y,p a)
{
    printf("%d\n",a(x,y));    
}

int main(int argc, const char *argv[])
{
    get_value(10,20,get_max);    
    get_value(10,20,get_min);    
    return 0;
}
