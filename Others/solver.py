#!/usr/bin/python3 

from z3 import *

key = [BitVec(f'arr[{i}]',8) for i in range(51)]

s = Solver()

s.add(key[50] == ord('C'))
s.add(key[4] == ord('T'))
s.add(key[8] == ord('F'))
s.add(key[11] == ord('{'))
s.add(key[38] == ord('}'))


s.add(key[50] == (((key[0] ^ key[1]) - key[2]) + key[3]))
s.add(key[4] == key[5] ^ key[6] ^ key[1] ^ key[7])
s.add(key[8] == ((((key[9] + key[10]) - key[5]) - key[11]) - key[12]))
s.add(key[11] == ((key[13] + key[14] * -2 ^ key[15]) + key[5]))
s.add(key[16] == (key[17] - key[18]))
s.add(key[19] == (key[20] ^ key[2]))
s.add(key[3] == ((key[21] + key[14]) - key[20] ^ key[22]))
s.add(key[23] == ((key[4] ^ key[24]) + key[25]))
s.add(key[26] == (key[23] ^ key[27]))
s.add(key[14] == (((key[15] ^ key[28]) - key[16]) + key[25]))
s.add(key[29] == (((key[1] ^ key[7]) - key[15]) - key[2]))
s.add(key[30] == (key[2] + key[22]))
s.add(key[31] == key[6] + key[32])
s.add(key[22] == ((key[21] - key[33] ^ key[6]) + key[26]))
s.add(key[24] == (key[34] - key[35]))
s.add(key[36] == key[37] ^ key[27])
s.add(key[15] == (key[38] ^ key[22] ^ key[39] + key[8] + key[31]))
s.add(key[34] == ((key[12] + key[9] + key[50]) - key[11]))
s.add(key[5] == (((key[0] ^ key[13]) - key[21]) - key[40]))
s.add(key[6] == (key[12] ^ key[21]))
s.add(key[18] == ((key[18] ^ key[20] ^ key[41] + key[40]) + key[21]))
s.add(key[41] == (((key[12] - key[16]) - key[30] ^ key[35]) - key[0]))
s.add(key[42] == (key[25] - key[22] ^ key[20]))
s.add(key[27] == (key[18] ^ key[34] ^ key[50] ^ key[18]))
s.add(key[21] == (((key[15] ^ key[30]) + key[16] + key[34]) - key[29]))
s.add(key[43] == (key[6] + key[28] + (key[37] ^ key[25])))
s.add(key[44] == ((key[20] + key[21] + key[9]) - key[33]))
s.add(key[40] == (key[24] ^ key[22]))
s.add(key[45] == ((key[10] + key[4]) - key[7]))
s.add(key[0] == (((key[2] - key[35]) - key[0]) - key[27]))
s.add(key[35] == ((key[34] + key[24]) - key[45] ^ key[7]))
s.add(key[25] == ((key[24] + key[19] + key[22]) - key[12]))
s.add(key[17] == ((key[32] - key[24] ^ key[6]) - key[25]))
s.add(key[46] == (((key[17] ^ key[11]) - key[6]) - key[14]))
s.add(key[10] == ((key[4] - key[12]) + (key[3] - key[47] ^ key[12])))
s.add(key[9] == ((key[21] + key[35]) - key[40] ^ key[28]))
s.add(key[48] == (((key[35] ^ key[46]) - key[46]) + key[29]))
s.add(key[1] == (((key[9] ^ key[44]) - key[19]) + key[7]))
s.add(key[20] == (key[2] ^ key[48]))
s.add(key[49] == ((key[40] + key[23] ^ key[12]) - key[14]))
s.add(key[13] == (key[43] ^ key[15] ^ key[23] ^ key[6]))
s.add(key[7] == ((key[4] + key[38]) - key[40]))
s.add(key[47] == ((key[17] + key[37]) - key[24]))
s.add(key[12] == (key[18] ^ key[32] ^ key[36] + key[7] + key[27]))
s.add(key[32] == (key[41] - key[49]))
s.add(key[37] == (((key[30] - key[37]) - key[23]) - key[10]))
s.add(key[39] == ((key[43] + key[24] ^ key[20]) - key[30]))
s.add(key[33] == (key[24] - key[2] ^ key[29]))
s.add(key[28] == (key[48] ^ key[44]))
s.add(key[38] == (key[24] ^ key[27] ^ key[15] + key[2] + key[31]))


#while s.check() == z3.sat:
#	model = s.model()	
#	print(model)
	
	
if s.check():
	print(s.model())
