#!/usr/bin/python3

import gdb

CHAR_SUCCESS = 0x5655599b
FAILURE = 0x565559a7

gdb.execute("set pagination off")
gdb.execute('b*0x5655599b')
gdb.execute('b*0x565559a7')

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-+*{}'"

flag= list('a'*30)

for i in range(0, len(flag)):
	for c in charset:
		print("entering char: " + c)
		flag[i] = c
		success_hits = i
		
		gdb.execute("run <<< $(python -c \"print '"+''.join(flag)+"'\")")
		
		while(success_hits > 0):
			gdb.execute('c')
			success_hits -=1
		
		eip = int(gdb.parse_and_eval("$eip"))	
		
		if eip == int(CHAR_SUCCESS):
			break
		if eip == int(FAILURE):
			continue

print("".join(flag))
gdb.execute("set pagination on")
