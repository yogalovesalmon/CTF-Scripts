#!/bin/python3
#### picoCTF2019 Reverse Cipher ####

cipher = 'w1{1wq83k055j5f'
flag = ""

i = 0
for count in range(8,23):
        if ((count & 1) == 0):
                flag += chr(ord(cipher[i])-5)
        else:
                flag += chr(ord(cipher[i])+2)
        i+=1

print("picoCTF{" + flag + "}")

