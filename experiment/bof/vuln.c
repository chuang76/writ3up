#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifndef BUF_SZ 
#define BUF_SZ 100
#endif 

int bof(char *str)
{
    char buffer[BUF_SZ]; 
    strcpy(buffer, str);                         // buffer overflow attack 
    return 1; 
}

int main(int argc, char** argv)
{
    char str[517]; 
    FILE* badfile; 

    badfile = fopen("badfile", "r"); 
    fread(str, sizeof(char), 517, badfile);     // read contents from badfile
    bof(str);                                   // copy to the buffer
    printf("Return properly\n"); 

    return 1; 
}
