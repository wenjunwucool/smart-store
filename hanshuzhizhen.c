#include<stdio.h>
typedef struct spdk_nvmf_listen_addr{
    int addr;
    char traddr;
} nvmf_addr;

int print_listern_add(void)
{
    printf("*****\n");

};

struct test
{
    
	int (*listen_addr_add)(struct spdk_nvmf_listen_addr *listen_addr);
};
int main(int argc, const char *argv[])
{
	struct spdk_nvmf_listen_addr *listen_addr;
    struct test *test1;
	//listen_addr ->addr=192;
    printf("***%x\n",test1->listen_addr_add(listen_addr));
   /* if(test1->listen_addr_add(listen_addr)<0)
{
    printf("&&&\n");
}*/
    return 0;
}
