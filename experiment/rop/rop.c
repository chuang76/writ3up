#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int bof(char* str)
{
	char buffer[100]; 
	unsigned int* framep; 

	asm("movl %%ebp, %0" : "=r" (framep));             // copy ebp 
	printf("ebp value = 0x%x\n", (unsigned)framep); 
	printf("buffer address = 0x%x\n", (unsigned)buffer); 

	strcpy(buffer, str);                               // buffer overflow 

	return 1; 
}

void foo() {
	static int i = 0; 
	printf("function foo() is called %d times\n", ++i);
}

void helper(int x) {
	printf("helper()'s argument = 0x%x\n", x);
}

int main(int argc, char** argv)
{
	char input[1000]; 
	FILE* badfile; 

	char* shell = getenv("my_shell"); 
	if (shell)
		printf("shell = %s, address = 0x%x\n", shell, (unsigned int)shell); 

	badfile = fopen("badfile", "r"); 
	fread(input, sizeof(char), 1000, badfile); 

	bof(input); 

	printf("return properly\n");
	return 1; 
}
