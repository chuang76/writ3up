This is the first problem in pwnable.kr. After connecting to the problem with ssh, let's check the contents first: 

![img](https://raw.githubusercontent.com/chuang76/image/master/fd-2.PNG)

And check the protection mechanism of executable file:

![img](https://raw.githubusercontent.com/chuang76/image/master/fd-3.PNG)

Since the source code is available, let's go over it: 

![img](https://raw.githubusercontent.com/chuang76/image/master/fd.PNG)

With the source code above, we can see if `buf` is the same as `LETMEWIN`, then we can capture the flag. Subsequently, contents of `buf` are stored through `read` function, which reads a file with file descriptor `fd`. The `fd` value is obtained from our parameter then subtract `0x1234`. 

So, let's review the standard file descriptors: 0, 1, 2 represent `stdin`, `stdout`, `stderr` respectively. And here is our trick. Since we know 0 denoted as standard input, let's force `fd` equals to zero, then the `stdin` makes us type anything, eg. type `LETMEWIN`.  Suffice it to say, to make file descriptor = 0, we should pass (0 + 0x1234) = 4660 as an argument. 

We can therefore obtain the flag:

![img](https://raw.githubusercontent.com/chuang76/image/master/fd-4.PNG)


