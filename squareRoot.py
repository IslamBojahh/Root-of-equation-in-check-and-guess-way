# -*- coding: utf-8 -*-
"""
find the root of equation polynomial in a simple case (x^2-y)
"""

epsillon=0.01
y=24
guess=y/2.0

while abs((guess**2)-y)>epsillon:
    guess=guess-((guess**2)-y)/(2*guess)
    
print(guess)