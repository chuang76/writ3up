## Instance 1

Since /bin/cat is a SUID program and its user is root. We can exploit it to get the flag. 

![](https://github.com/chuang76/writ3up/blob/main/figure/cse466-1.PNG?raw=true)



## Instance 2

Our target is a SUID program and its user should be root. So use find command to find it:

```
$ find . -type f -uid 0 -perm /u+s 2>/dev/null
```

![](https://github.com/chuang76/writ3up/blob/main/figure/cse466-2.PNG?raw=true)

We get /usr/bin/find. Besides, we can use its argument `-exec` to execute some malicious commands. In our case, we should run `cat flag` to leak the contents of the binary flag. 

![](https://github.com/chuang76/writ3up/blob/main/figure/cse466-3.PNG?raw=true)