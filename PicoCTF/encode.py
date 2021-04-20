#!/usr/bin/python3
# It is used to decode text in UTF-16BE format

### Original Algorithm: ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
### This qns is actually about byte shifting
### Eg. ord('p') = 01110000
###     ord('p') << 8 = 01110000 00000000 => 28672
###     +
###     ord('i') = 01101001
###     (ord('p') << 8 ) + ord('i') = 01110000 01101001 = 28777
### In order to decode text into the original 2 letters, 
###         first letter => shift 8 bits to the right (eg. 01110000 01101001 >> 8 == 00000000 01110000 == p)
###         second letter => shift 8 bits to the right then shift it back to left ( eg. 01110000 01101001 >> 8 == 00000000 01110000 << 8 == 01110000 00000000) then
###         minus the text ( eg. 01110000 01101001 - 01110000 0000000 == 01101001 == i)


text="灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽"

for i in range(len(text)):
    print(chr(ord(text[i])>>8))
    print(chr((ord(text[i])) - ((ord(text[i])>>8)<<8)) )
