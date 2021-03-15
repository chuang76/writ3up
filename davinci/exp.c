#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
    char *str = "wAPcULZh\x7f\x06x\x04LDd\x06~Z\"YtJNice flag";
    for (int i = 0; i < 22; i++) {
        if ((i % 2) == 0)
        	printf("%c", str[i] ^ 0x13);
        else
        	printf("%c", str[i] ^ 0x37);
    }
    printf("\n");
    return 0;
}
