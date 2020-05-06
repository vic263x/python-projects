# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:06:02 2020

@author: Wiktoria
"""


class Phrase: 
    
    
    
    def sentence(self):
        self.a = "A new sentence"
        
    def setDefinition(self, a):
        self.definition = a
        
        
    def getDefinitionUppercased(self):
        return self.definition.upper()
    
p1 = Phrase()
p2 = Phrase()

p1.setDefinition("A different sentence")
print(p1.definition)

print(p1.getDefinitionUppercased())

p2.setDefinition("Sentence number two")
print(p2.definition)

print(p2.getDefinitionUppercased())
    





