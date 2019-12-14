#include <stdio.h>
#include <windows.h>
#include "crc.h"

static void guard_func()
{
	char pass[100];
	printf("Input String : ");
	scanf("%100s", pass);
	if(!strcmp(pass, "test"))	
		printf("Good\n");
	else
		printf("Bad Password\n");
}

static void dummy() {}

DWORD WINAPI anti_debug(LPVOID lpParam)
{
	unsigned long szFunc = (unsigned long)&dummy - (unsigned long)&guard_func;
	unsigned char *buf = (unsigned char *)malloc(szFunc);

	printf("%X\n", szFunc);

	while(1)
	{
		memset(buf, 0, szFunc+1);
		memcpy(buf, guard_func, szFunc);
		initCRC(szFunc, buf);

		unsigned __int64 crc = make_crc();
		if(crc != 0x26af9b5e0bcafe9e)
			ExitProcess(-1);
		Sleep(1000);
	}
	free(buf);
	return 0;
}

int main(int argc, char **argv)
{
	CreateThread(0,0,anti_debug,0,0,0);
	guard_func();
	return 0;
}
