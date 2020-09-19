#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### This function converts a pawn move to an integer value. 
### For example, "E4" in the pgn would correspond to value "28" in our gameboard 
### Ignore pawn promotions 

def pos2int(pos):
    dicty = {"a":0, "b":1,"c":2,"d":3, "e":4, "f":5,"g":6,"h":7}
    if "=" in pos: 
        return False
    digit = int(pos[-1])
    inty = dicty[pos[0]]+(digit-1)*8
    return inty

