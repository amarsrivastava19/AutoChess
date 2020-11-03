#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### In our games, if a piece moves, we need to delete the piece on the space where it is currently placed. 
### These functions identifies the location of the original piece, and allows us to know which square to set to 0. 


def RowChecker(start,target): 
    
    rows = [[i for i in range(j,j+8)] for j in range(0,64,8)]
            
    for row in rows: 
        if start in row and target in row: 
            return True
    
    return False




def FileChecker(start,target): 
    
    if target > start: 
        while target > start: 
            target = target - 8
            if target == start: 
                return True
        return False
    else: 
        while start > target: 
            start = start - 8
            if target == start: 
                return True
        return False
            




def R_PathFinder(start,target): 
    ## suppose start is 2 and target is 34 
    ## we expect the output to be [10,18,26]
    ## 
    ## suppose start is 2 and target is 6
    ## we expect the output to be [3,4,5]
    ##
    ## if no path available, return n/a
    
    diff = target - start
    diff_abs = abs(target - start) 
    
    
    
    if RowChecker(start,target) == True:
        if diff > 0: 
            path = [i for i in range(start+1,target) if i > ((start//8)*8) and i <((start//8)*8+8) ]
        else: 
            path = [i for i in range(target+1,start) if i > ((start//8)*8) and i <((start//8)*8+8)]
        
    elif FileChecker(start,target) == True:
        if diff > 0: 
            path = [i for i in range(start+8,target,8) if i > 1 and i < 64]
        else: 
            path = [i for i in range(target,start,8) if i > 1 and i < 64]
        
    else: 
        path = False
        
    return path



def KnightFinder(inty): 
    
    possible = inty + 16 - 1
    possible2 = inty + 16 + 1
    possible3 = inty + 2 + 8
    possible4 = inty + 2 - 8
    possible5 = inty - 2 + 8 
    possible6 = inty - 2 - 8
    possible7 = inty - 16 - 1
    possible8 = inty - 16 + 1
        
    if inty in [0,8,16,24,32,40,48,56]: 
        possible = -1
        possible7 = -1
        possible5 = -1
        possible6 = -1 
    
    if inty in [1,9,17,25,33,41,49,57]: 
        possible5 = -1
        possible6 = -1
        
    if inty in [7,15,23,31,39,47,55,63]: 
        possible2 = -1
        possible3 = -1 
        possible4 = -1
        possible8 = -1

    if inty in [6,14,22,30,38,46,54,62]: 
        possible3 = -1
        possible4 = -1
        
        
    listy2 = [possible,possible2,possible3,possible4,possible5,possible6,possible7,possible8]
    listy = [i for i in listy2 if (i >= 0 and i <= 63)]
    
    return listy





def BishopFinder(inty): 
    left_edge = [0,8,16,24,32,40,48,56]
    right_edge = [7,15,23,31,39,47,55,63]
    
    listy = []
    
    x = inty
    while (x >= 0 and x <= 63):
        if x in right_edge:
            break
        x = x + 8 + 1
        if (x >= 0 and x <= 63): 
            listy.append(x)
        if (x in left_edge or x in right_edge): 
            break
            
    x = inty
    while (x >= 0 and x <= 63):
        if x in right_edge: 
            break
        x = x - 8 + 1
        if (x >= 0 and x <= 63): 
            listy.append(x)
        if (x in left_edge or x in right_edge): 
            break
    
    x = inty
    while (x >= 0 and x <= 63):
        if x in left_edge:
            break
        x = x + 8 - 1
        if (x >= 0 and x <= 63): 
            listy.append(x)
        if (x in left_edge or x in right_edge): 
            break
            
    x = inty
    while (x >= 0 and x <= 63):
        if x in left_edge:
            break
        x = x - 8 - 1
        if (x >= 0 and x <= 63): 
            listy.append(x)
        if (x in left_edge or x in right_edge): 
            break
            
    return listy




def RookFinder(inty): 
    
    left_edge = [0,8,16,24,32,40,48,56]
    right_edge = [7,15,23,31,39,47,55,63]
    
    listy = []
    
    x = inty
    while (x >= 0 and x <= 63):
        if x in right_edge:
            break
        x = x +1
        if (x >= 0 and x <= 63): 
            listy.append(x)
        if (x in left_edge or x in right_edge): 
            break
            
            
    x = inty        
    while (x >= 0 and x <= 63):
        if x in left_edge:
            break
        x = x - 1
        if (x >= 0 and x <= 63): 
            listy.append(x)
        if (x in left_edge or x in right_edge): 
            break
            
    x = inty
    while (x >= 0 and x <= 63):
        x = x + 8
        if (x >= 0 and x <= 63): 
            listy.append(x)

    x = inty
    while (x >= 0 and x <= 63):
        x = x - 8
        if (x >= 0 and x <= 63): 
            listy.append(x)

    return listy

