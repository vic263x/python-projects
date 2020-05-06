# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:06:02 2020

@author: Wiktoria
"""

#a class definition
class Word: 
    
    count = 0
    
    def whatami(self):
        self.x = "I'm a noun"

    def setDefinition(self, x):
        self.definition = x
        Word.count += 1
        
    def getDefinitionUppercased(self):
        return self.definition.upper()
# an instance
w = Word()
w2 = Word()

w.setDefinition("An animal with four legs")
print(w.definition)

w2.setDefinition("A vehicle that flies")
print(w2.definition)

print(w.getDefinitionUppercased())





