### DaVinci CTF 2021 - Rocca Pia (50 points) 

The file is a 64-bit x84-64 ELF executable. Use Ghidra to analyze the content. I renamed some variable names to make the program more readable. The program aims to transform the argument. If the return value is 0, we can get the flag. 

![](https://github.com/chuang76/writ3up/blob/main/figure/dvc-1.PNG?raw=true)

So let's dive into `transform()` function. As you can see, the function aims to take the even bit to do an XOR operation with 0x13, and take the odd bit to do an XOR operation with 0x37. 

![](https://github.com/chuang76/writ3up/blob/main/figure/dvc-2.PNG?raw=true)

XOR operation has an important propery: the inverse of XOR is still XOR. Note that the third argument of strncmp() function is 0x16, which means it only compares the first 22 bytes. So we can write a simple program called `exp.c` to derive the correct argument: 

```c
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
```

Here is the flag. 

```
$ gcc exp.c -o exp 
$ ./exp 
dvCTF{I_l1k3_sw1mm1ng}
```



