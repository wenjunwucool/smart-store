#include<stdio.h>
#include<stdlib.h>
#include"/usr/include/sys/queue.h"
struct QUEUE_ITEM{
    int value;//数据域
    TAILQ_ENTRY(QUEUE_ITEM)entries;//队列指针
};
    TAILQ_HEAD(,QUEUE_ITEM) queue_head;//定义头队列
int main(int argc, const char *argv[])
{
    struct QUEUE_ITEM *item;  
    struct QUEUE_ITEM *tmp_item;  
    TAILQ_INIT(&queue_head);//初始化头队列  
    int i=0;  
    for(i=5;i<10;i+=2){  
    item=malloc(sizeof(item));  
    item->value=i;  
    TAILQ_INSERT_TAIL(&queue_head, item, entries);  
    }  
                          
    struct QUEUE_ITEM *ins_item,*test;  
    ins_item=malloc(sizeof(ins_item));  
    test=malloc(sizeof(ins_item));  
                              
    ins_item->value=100;  
    TAILQ_INSERT_BEFORE(item,ins_item,entries);  
    tmp_item=TAILQ_FIRST(&queue_head);  
    printf("first element is %d\n",tmp_item->value);  
                                              
    tmp_item=TAILQ_NEXT(tmp_item,entries);  
    printf("next element is %d\n",tmp_item->value);  
                                                      
    tmp_item=TAILQ_NEXT(tmp_item,entries);  
    printf("next element is %d\n",tmp_item->value);  
                                                              
    tmp_item=TAILQ_NEXT(tmp_item,entries);  
    printf("next element is %d\n",tmp_item->value);
    TAILQ_FOREACH(ins_item,&queue_head,entries){
        printf("%s\n",ins_item->value);
    }
    return 0;

}
