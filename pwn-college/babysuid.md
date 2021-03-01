## Instance 1

Since /bin/cat is a SUID program and its user is root. We can exploit it to get the flag. 

[1]

## Instance 2

Our target is a SUID program and its user should be root. So use find command to find it:

```
$ find . -type f -uid 0 -perm /u+s 2>/dev/null
```

[2]

We get /usr/bin/find. Besides, we can use its argument `-exec` to execute some malicious commands. In our case, we should run `cat flag` to leak the contents of the binary flag. 

[3]