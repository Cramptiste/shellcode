#!/usr/bin/env python
import os
# votre programme en asm doit etre dans le meme dir que le shellcode.py
file = input("entrez le nom de votre programme en assembleur")
file1 = file.split('.')
command = "nasm "+file+" -o "+file1[0]+".o"
os.system(command)
command2 = "ndisasm -u "+file[0]+".io"
os.system(command2)
fd = open("shelltemp", "r")
ligne = "".join(fd.readline())
os.system("touch shellcode1")
fl = open("shellcode1", "w")
while ligne:
    tp = ligne.split(" ")
    fl.write(tp[2])
    ligne = "".join(fd.readline())
fl.close()
fl = open("shellcode1", "r")
code = fl.read(2)
os.system("touch shellcode")
fc = open("shellcode", "w")
fc.write(r'shellcode[]="')
while code:
    hex=r"\x"+code
    fc.write(hex)
    code = fl.read(2)
fc.write('";')
fl.close()
fc.close()
os.system("rm shellcode1")
fd.close()
os.system("rm shelltemp")
