#!/usr/bin/env python

#SICA 2016 _ RE-150
#Team : Th3Jackers
#Mimo-0xC001
#www.fb.com/0xC00l

def getFlag():
 Key="F!14bcFbjgHonDigEzDfiNoshDFR14Gff5zDBEssZerg=="
 Flag=""
 for i in range(26):
  if(not (i & 3)):
   xor_key=(2*i) + 3
   Flag+= chr(xor_key ^ ord(Key[i]))
  if(not (i % 5)):
   xor_key=2*(i+2)
   Flag+=chr(xor_key ^ ord(Key[i]))
 return Flag

def main():
 print "[+] - Flag : ", getFlag() 
 
if __name__ == '__main__':
    main()