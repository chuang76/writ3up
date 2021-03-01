#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int bof(char* str)
{
	char buffer[12]; 
	unsigned int* framep; 

	asm("movl %%ebp, %0" : "=r" (framep)); 

	printf("ebp value = 0x%.8x\n", (unsigned)framep); 
	printf("buffer address = 0x%.8x\n", (unsigned)buffer); 

	strcpy(buffer, str); 		// buffer overflow
	return 1; 
}

int main(int argc, char** argv)
{
	char input[100]; 
	FILE* badfile; 

	badfile = fopen("badfile", "r"); 
	int len = fread(input, sizeof(char), 100, badfile); 
	printf("input size = %d", len); 

	bof(input); 
	printf("return properly\n"); 

	return 1; 
}
