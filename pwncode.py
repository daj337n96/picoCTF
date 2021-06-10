from pwn import *

KEY_LEN = 50000
MAX_CHUNK = 2000 # can be any number

r = remote("mercury.picoctf.net", 41934) # connect to site

# receive the given encrypted flag and unhex it
r.recvuntil("This is the encrypted flag!\n")  
flag = r.recvlineS(keepends = False)
log.info(f"Flag: {flag}") # hex format 
unhex_flag = unhex(flag)

counter = KEY_LEN - len(unhex_flag) # counter to track remaining bytes of the 5000

# loop to send 'a'*(remaining bytes of the 5000)
with log.progress('Causing wrap-around') as p:
    while counter > 0:
        p.status(f"{counter} bytes left")
        chunk_size = min(MAX_CHUNK, counter)
        r.sendlineafter("What data would you like to encrypt? ", "a" * chunk_size)
        
        counter -= chunk_size

# wrap-around occured so send unhex_flag
r.sendlineafter("What data would you like to encrypt? ", unhex_flag)
r.recvlineS()
log.success("The flag: {}".format(unhex(r.recvlineS()))) # hex format 