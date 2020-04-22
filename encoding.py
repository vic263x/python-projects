# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:33:05 2020

@author: Wiktoria
"""


# %20 space in percent encoding

import urllib.parse 

text = 'Cześć, mam na imię Michał!'
encoded = urllib.parse.quote(text)
print(encoded)

























