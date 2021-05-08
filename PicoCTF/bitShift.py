#!/bin/python3
#### picoCTF2019 VaultDoor7 (bit shift) ####

nums = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734293602, 1701067056, 892756537]

flag = ""

for num in nums:
	first = num >> 24
	second = (num >> 16) - (first << 8)
	third = (num >> 8) - ((num >> 16) << 8)
	four = num - ((num >> 8)<<8)
	flag += chr(first)+ chr(second)+ chr(third) + chr(four)

print(flag)
