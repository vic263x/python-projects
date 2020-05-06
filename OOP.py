# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:06:02 2020

@author: Wiktoria
"""

#a class definition
class Word: 
    
    count = 0
    
    def __init__(self, definition, entry):
        self.definition = definition
        self.entry = entry
        Word.count +=1
        print("Instantiating Word object")
    
    
    def whatami(self):
        self.x = "I'm a noun"

    
    def getDefinitionUppercased(self):
        return self.definition.upper()
# an instance
w = Word("An animal with four legs", "Dog")
w2 = Word("A vehicle can fly", "Airplane")

print(w.getDefinitionUppercased())

print(w2.entry)
print(Word.count)




