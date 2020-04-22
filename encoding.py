# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:33:05 2020

@author: Wiktoria
"""

f = open('r1251.txt','rb')
r = f.read()
r = r.decode('1251') # windows - 1251 encoding
f.close()
print('Some Russian:', r)


f = open('cb5.txt','rb')
c = f.read()
c = c.decode('big5') # big5 encoding
f.close()
print('Some Chinese:', c)

























