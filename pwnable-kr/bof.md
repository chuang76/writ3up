This is the third challenge in pwnable.kr [1], and it is about buffer overflow. <br>Let's start. First of all, according to the pwnable.kr website, we can obtain the source code `bof.c` and executable file `bof` as follows: 

```
$ wget http://pwnable.kr/bin/bof.c
$ wget http://pwnable.kr/bin/bof
```

After downloading the files with wget, the properties of protection can be observed through checksec command `checkesec bof`:

![img](https://raw.githubusercontent.com/chuang76/image/master/bof-1.png)

Since the source code is available, we then go over it and try to understand what it does. 

![img](https://raw.githubusercontent.com/chuang76/image/master/bof-3.png)

Based on the information of source code, if `key` equals to 0xcafebabe, then we can take control of `/bin/sh`.  However, in the main function, the value of key has been stored with 0xdeadbeef. So, how can we overwrite the `key` value? 

Let's move on to the `func` function. In `func` function, as we can see, it calls a `gets` function, which is a dangerous function since it lacks of boundary checking mechanism. With this vulnerability, we can make the overflow happen, and get an entry to overwrite the original `key` value (i.e. force `key` equals to 0xcafebabe). 

The figure below is about `func` contents in assembly, and the red box contains the most essential part: `gets` and compare the `key` value with 0xcafebebe. In GDB, you can check the contents in assembly with `layout asm` command. 

![img](https://raw.githubusercontent.com/chuang76/image/master/bof-4.png)

Next, since we attempt to overwrite `key` value, the memory address of `key` is needed. To explore where `key` value is stored, we first set a breakpoint at `func`, and type `ni` instruction until we meet `gets` function. The `gets` function reads a string from standard input, and stored the data into `overflow` array. When we stop at `gets`, we can type anything we want (eg. I enter aaaaaaaa in this experiment), then observe the current state of stack. 

![img](https://raw.githubusercontent.com/chuang76/image/master/bof-5.PNG)

The figure above demonstrates 0xffffd26c is the address where `overflow` starts, and the address of original `key` value starts at 0xffffd2a0. The roughly memory layout is like:

```
high		|	0xdeadbeef	 |     -> 0xffffd2a0 ('0xcafebabe')
		--------------------------
		|          ...      	 |     -> ...        ('a')
		|       overflow[1]      |     -> 0xffffd26d ('a')
low		|       overflow[0]      |     -> 0xffffd26c ('a')
```

So how many bytes should we overwrite? The answer is 0xffffd2a0 - 0xffffd26c = 0x34 = 52 bytes. And remember the original `key` value should be replaced with 0xcafebabe. We can write an exploit code `exp.py` by pwntools as follows:

```
from pwn import *
r = remote('pwnable.kr', 9000)
addr = p32(0xcafebabe)
r.sendline(b'a' * 52 + addr)
r.interactive()
```

Therefore, the flag can be captured. 

![img](https://raw.githubusercontent.com/chuang76/image/master/bof-6.PNG)







