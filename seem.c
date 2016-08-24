#include<stdio.h>
#include <pthread.h>
#include <semaphore.h>

#include <unistd.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

sem_t a,b;
void *fun1(void *arg)
{
	char buf[128];
	int fd;
	ssize_t n;
	fd = open("1.txt",O_RDWR|O_CREAT|O_TRUNC,0664);
	if(fd < 0)
	{
		perror("open1");
		return 0;
	}
	while(1)
	{
		sem_wait(&a);
		n = read(0,buf,sizeof(buf));
		write(fd,buf,n);
		sem_post(&b);
	}
}

void *fun2(void *arg)
{
	char buf[128];
	int fd;
	ssize_t n;
	fd = open("1.txt",O_RDWR|O_CREAT|O_TRUNC,0664);
	if(fd < 0)
	{
		perror("open1");
		return 0;
	}
	while(1)
	{
		sem_wait(&b);
		n = read(fd,buf,sizeof(buf));
		write(0,buf,n);
		sem_post(&a);
	}
}
sem_t a,b;
int main(int argc, const char *argv[])
{
	int ret;
	pthread_t tid[2];
	sem_init(&a,0,1);
	sem_init(&b,0,0);
	ret = pthread_create(&tid[0],NULL,fun1,(void *)argv[1]);
	if(ret < 0)
	{
		perror("fail to thread fun1");
		return 0;
	}
	ret = pthread_create(&tid[0],NULL,fun2,(void *)argv[1]);
	if(ret < 0)
	{
		perror("fail thread fun2 ");
		return 0;
	}
	while(1);
	return 0;
}
