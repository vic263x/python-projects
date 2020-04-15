# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:35:03 2020

@author: Wiktoria
"""

from googletrans import Translator


def main():
    translator = Translator()
    result = translator.translate('How are you?', dest= 'es')
    print(result.text)
    
main()
















