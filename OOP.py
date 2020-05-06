# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:06:02 2020

@author: Wiktoria
"""


class Segment:
    def __init__(self, grapheme):
        self.grapheme = grapheme
        
class Consonant(Segment):
    
    def moa(self):
        return "palatal"
        
class Vowel(Segment):

    def height(self):
        return "low"
    
con = Consonant("t")

vow = Vowel("o")

print(con.grapheme)
print(con.moa())
print(vow.grapheme)
print(vow.height())




