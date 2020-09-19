#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### This function initializes game boards for white and black 
### Each board contains one unique unit out of the following : Pawns, Rooks, Knights, Bishops, Queen, King
### There are 6 gameboards for white and 6 for black

def board_creator(): 
    
    ### Initialize the white and black boards 

    
    p_board_W = [0]*8 + [1]*8 + [0]*48
    
    K_board_W = [0]*64
    K_board_W[4] = 1
    
    N_board_W = [0]*64
    N_board_W[1] = 1
    N_board_W[6] = 1
    
    R_board_W = [0]*64
    R_board_W[0] = 1
    R_board_W[7] = 1
    
    Q_board_W = [0]*64
    Q_board_W[3] = 1
    
    B_board_W = [0]*64
    B_board_W[2] = 1
    B_board_W[5] = 1
    
    p_board_B = [0]*48 + [1]*8 + [0]*8
    
    K_board_B = [0]*64
    K_board_B[60] = 1
    
    N_board_B = [0]*64
    N_board_B[62] = 1
    N_board_B[57] = 1
    
    R_board_B = [0]*64
    R_board_B[56] = 1
    R_board_B[63] = 1
    
    Q_board_B = [0]*64
    Q_board_B[59] = 1 
    
    B_board_B = [0]*64
    B_board_B[58] = 1
    B_board_B[61] = 1

    
    
    
    total_board_W = [p_board_W,#0
                     K_board_W,#1
                     N_board_W,#2
                     Q_board_W,#3
                     R_board_W,#4
                     B_board_W]#5
    
    total_board_B = [p_board_B,#0
                     K_board_B,#1
                     N_board_B,#2
                     Q_board_B,#3
                     R_board_B,#4
                     B_board_B]#5
    
    return total_board_W, total_board_B
    

