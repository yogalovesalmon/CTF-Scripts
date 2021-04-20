#!/usr/bin/python3
# It is used to encode text in UTF-16BE format

text="灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽"

for i in range(len(text)):
    print(chr(ord(text[i])>>8))
    print(chr((ord(text[i])) - ((ord(text[i])>>8)<<8)) )
