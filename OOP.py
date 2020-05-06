# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:06:02 2020

@author: Wiktoria
"""


class Segment:
    def __init__(self, grapheme):
        self.grapheme = grapheme
        
class Plosive(Segment):
    
    def voicing(self):
        return "voiceless"
        
class Fricative(Segment):

    def poa(self):
        return "dental"
    
plo = Plosive("k")

fri = Fricative("th")

print(plo.grapheme)
print(plo.voicing())
print(fri.grapheme)
print(fri.poa())




