from pwn import *

r = remote("mercury.picoctf.net", 41934) # connect to site 
r.recvuntil("This is the encrypted flag!\n")
flag = r.recvlineS(keepends = False)
print(flag)