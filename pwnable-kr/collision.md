This is the second challenge in pwnable.kr. After connecting to the challenge with ssh, let's check the contents first:

![img](https://raw.githubusercontent.com/chuang76/image/master/col-1.PNG)

And check the protection mechanism of the executable file `col`:

![img](https://raw.githubusercontent.com/chuang76/image/master/col-2.PNG)

Since the source code `col.c` is available, we can download the code through the following command and go over it:

```
scp -P 2222 col@pwnable.kr:col.c ./col.c
```

```c
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}

int main(int argc, char* argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
        if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }
        
        if(hashcode == check_password( argv[1] )){                       
                system("/bin/cat flag");                                 
                return 0;                         
        }                        
        else
        	printf("wrong passcode.\n");                                             
        return 0;   
}
```

If the return value of `check_password` function (which passed `argv[1]` as an argument) equals to `hashcode`, i.e. 0x21DD09EC, then we can capture the flag. Since the function `check_password` plays an essential part in this challenge, we should understand what it does first. I'll show its task by passing different parameters. 

After downloading the source code `col.c` to the host, we can modify some codes to observe changes of `ip`. I add some codes as follows to check the contents of `ip`, and remove the limitation in main function temporarily (that is, the length of argument is not limited). 

```c
for (i = 0; i < 5; i++)
	printf("ip[%d] = 0x%x\n", i, ip[i]); 
```

The modified code can be compiled through:

```
gcc -m32 col.c -o col 
```

We first enter a string `0000`  as an argument, as you can see, `ip[0]` equals to  `0x30303030`. And this value is just the ASCII code of string `0000`.  

![img](https://raw.githubusercontent.com/chuang76/image/master/col-8.PNG)

Subsequently, let's enter another string `1000` and see what happens. The ASCII value stored in `ip[0]` becomes `0x30303031`. Why not `0x31303030`? The reason is: in x86 architecture, the system adapts Little Endian format to store a word. That is, store LSB at the lowest address. 

```
string '1000' stored in ip[0]:
				|  0x30	|	-> low address (LSB)
				|  0x30	|
				|  0x30	|	
				|  0x31 |	-> high address (MSB)
```

![img](https://raw.githubusercontent.com/chuang76/image/master/col-5.PNG)

What happens if we enter a longer string (to conform to the limitation of challenge)? Since we know that each size of `char` type is 1, and each size of `int` type is 4; thus, if we enter an argument with a length of 20, this argument can be represented in `5` integers through `check_password` function. The following example can prove our idea:

![img](https://raw.githubusercontent.com/chuang76/image/master/col-9.png)

Let's continue. In `check_password` function, the return value `res` tries to sum up each element in `ip`. Accordingly, if we attempt to make this summation equal to `hashcode` (0x21DD09EC), we can try a combination like:

```
Since 0x21DD09EC / 5 = 0x6C5CEC8 ...
ip[0], ip[1], ip[2], ip[3] can be 0x6C5CEC8, while ip[4] = 0x6C5CECC. 
```

It should be noted that the ordering of bytes (Endianness) is in Little Endian format, so here's our shellcode:

```
\xC8\xCE\xC5\x06\xC8\xCE\xC5\x06\xC8\xCE\xC5\x06\xC8\xCE\xC5\x06\xCC\xCE\xC5\x06
```

Or with operations in Python: 

```
col@pwnable:~$ ./col $(python -c "print '\xC8\xCE\xC5\x06' * 4 + '\xCC\xCE\xC5\x06'")
```

We can therefore obtain the flag. 

![img](https://raw.githubusercontent.com/chuang76/image/master/col-10.png)

<br>

## Other issue

- MD5 algorithm
- Type casting 

