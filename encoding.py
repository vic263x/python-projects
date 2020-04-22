# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:33:05 2020

@author: Wiktoria
"""


from bs4 import UnicodeDammit

f = open('cb5.txt','rb')
c = f.read()
decoding = UnicodeDammit(c)
encoding = decoding.original_encoding

c = c.decode(encoding) 
f.close()
print('Some Chinese:', c)

























