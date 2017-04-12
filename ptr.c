#include<stdio.h>
int main(int argc, const char *argv[])
{
    char *p;
    char *s = "string";
    p = s;
    s = "char"; //remember it 
    printf("%s\n",p);
    printf("%s\n",s);
    return 0;
}
