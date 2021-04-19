#!/usr/bin/python3
# This script takes the message and translate using rot13

rot13trans = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
  
def rot13(text):
    return text.translate(rot13trans)

def main():
    msg = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}"
    print(rot13(msg))

main()
