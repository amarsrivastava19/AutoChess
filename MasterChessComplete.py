#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Function that calls MasterChess 10 times for a given game in a .pgn file

def MasterChessComplete(white_moves,black_moves,resultW,resultB): 
    
    ### get a list of viable moves under the following conditions
        # We cannot have a capture move, so "x" can't be in either white or black
        # We cannot be in the opening. So 5 moves have to have passed. 
     
    viable_moves = [i for i,x in enumerate(white_moves) if ("x" not in white_moves[i]) and ("x" not in black_moves[i]) and (i > 5)]

    ### pick 10 random moves
    try: 
        move_picker = random.sample(viable_moves, k=10)

        to_move = [random.randint(0,1) for i in range(0,10)]
    
    except: 
        move_picker = viable_moves
        to_move = [random.randint(0,1) for i in viable_moves]

        
    listy = []
    
    for i,j in zip(move_picker,to_move):

        ### call Master Chess Here over random moves
        ### we want to return a list of lists that we can later append
        new_board = MasterChess(white_moves[0:i+1], black_moves[0:i+1], j,resultW,resultB)
        listy.append(new_board)

    return listy 


