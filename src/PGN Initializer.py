#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import chess
import chess.pgn

### PGN_initializer opens a .pgn file and reads it into memory

### PGN_Counter grabs the number of games in a .pgn file. This is used to loop through the .pgn files within the pipeline. 


def PGN_initializer(file):

    pgn = open(file)
    return pgn


def PGN_Counter(filepath):
    
    pgn = PGN_initializer(filepath)

    counter = 0

    for i in range(0,60000): 
        first_game = chess.pgn.read_game(pgn)
        if first_game is None: 
            break 
        else: 
            counter = counter + 1

    pgn = PGN_initializer(filepath)
    
    return counter, pgn

