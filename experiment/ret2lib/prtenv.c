#include <stdio.h>
#include <stdlib.h>

void main()
{
	char* shell = getenv("my_shell"); 
	if (shell)
		printf("shell = %s, address = 0x%x\n", shell, (unsigned int)shell);
}
