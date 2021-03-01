This is one of Toddler's Bottle challenge in pwnable.kr. According to the information provided by the website, we can download the directory with wget command:

```
$ wget -r --no-parent http://pwnable.kr/bin/flag
```

There is only one executable file in the directory. Let's give some preliminary tests. 

![img](https://raw.githubusercontent.com/chuang76/image/master/flag-2.PNG)

Without the contents of source code (i.e. unavailable), we then try to disassemble the executable file. 

![img](https://raw.githubusercontent.com/chuang76/image/master/flag-10.png)

Since there's nothing showed on the screen after `objdump -d` command, we then check the properties of protection mechanism with checksec, and print some printable characters in the file instead. 

![img](https://raw.githubusercontent.com/chuang76/image/master/flag-8.png)

```
$ strings -n 30 flag
@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_
`abcdefghijklmnopqrstuvwxyz{|}~
"9999$%&/999956799999:<DG9999HI_`
''''!#$`''''abcd''''efgh''''ijkl''''mnop''''qrst''''uvwx''''yz{|''''}~
Q2R''''STUV''''WXYZ''''[\]^''''_
MNONNNNPRTUNNNNVWYZNNNN[\_`NNNNabcdNNNNefhi
rrrr!"#$rrrr%&'(rrrr)*+,rrrr-./0rrrr1234rrrr5678rrrr9;<=rrrr>@ABrrrrCDFJrrrrKLMNrrrrOPRSrrrrTUVWrrrrXYZ[rrrr\]^_rrrr`abcrrrrdefgrrrrhijkrrrrlmnorrrrpqrsrrrrtuvwrrrrxyz{rrrr|}~
!"9999#$%&9999'()*9999+,-.9999/012999934569999789:9999;<=>9999?@AB9999CDEF9999GHIJ9999KLMN9999OPQR9999STUV9999WXYZ9999[\]^9999_`ab9999cdef9999ghij9999klmn9999opqr9999stuv9999wxyz9999{|}~9999
b'cdr%WrefgWr%Whij%Wr%klr%WrmnoWr%Wpqr%Wr%str%WruvwWr%Wxyz%Wr%ABr%WrCDEWr%WFGH%Wr%IJr%WrKLMWr%WNOP%Wr%QRr%WrSTUWr%WVWX%Wr%YZ
$9999(/6>9999HQXa9999eimq9999uy}
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
$Id: UPX 3.08 Copyright (C) 1996-2011 the UPX Team. All Rights Reserved. $
GCC: (Ubuntu/Linaro 4.6.3-1u)#
```

Based on the information above, we can understand the file has been packed with `UPX`, which is an executable packer with a data compression algorithm namely UCL. To unpack the file, we just type the command as follows:

```
$ upx -d flag 
```

After unpacking the file, let's continue. First, we set a breakpoint at the main function, and try to explore the program. You can display the program in assembly with `layout asm`. 

![img](https://raw.githubusercontent.com/chuang76/image/master/flag-5.PNG)

As you can see, the comment demonstrates the flag is just at address 0x6c2070. We then print the memory contents at the given address 0x6c2070. And here is our flag. 

![img](https://raw.githubusercontent.com/chuang76/image/master/flag-11.png)

<br>

## Other issue

- UPX packer 
- Executable compression: (1) reduce the storage requirements (2) deter reverse engineering 

