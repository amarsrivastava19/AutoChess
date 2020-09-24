#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### Main workflow that combines all other functions together into a formal pipeline from raw data to processed vectors
### ready to be fed into the DL algorithm

### If you have one .pgn file, call Pipeline() to get 10 gameboards for every game in the .pgn 
### If you have multiple .pgn files, call File2Pipeline() with the folder path, and this will loop through each .pgn,
### and then through each game. 




def Pipeline(filepath): 
    
    total_list = []
    
    num_games, pgn = PGN_Counter(filepath)
    
    for i in range(0,num_games): 
        
        first_game = chess.pgn.read_game(pgn)
        result = first_game.headers["Result"]
        
        if result == "1/2-1/2": 
            continue
            
        if result == "1-0":
            resultW = 1
            resultB = 0 
            
        if result == "0-1":
            resultW = 0
            resultB = 1
            
        if result != "1/2-1/2" and result != "1-0" and result != "0-1": 
            print("ERROR ERRROR ERRROR ERROR R")
            
        

        x = str(first_game.mainline_moves())
        first_split = x.split(".")
        second_split = [i.split(" ")[1:3] for i in first_split if len(i.split(" ")) == 4]

        white_moves = [i[0] for i in second_split]
        black_moves = [i[1] for i in second_split]
        
        try: 
            ten_boards = MasterChessComplete(white_moves,black_moves,resultW,resultB)
            
            for board in ten_boards: 
                total_list.append(board)
            
        except: 
            continue 
            
    return total_list





def File2Pipeline(path):
    listy = []
    files = os.listdir(path)
    
    for i,file in enumerate(files):
        try:
            print("Reading file# " + str(i) + "/" + str(len(files)))
            pathy = path + "\\" + file
            x = Pipeline(pathy)
            listy = listy + x
        except:
            print("This is a bad file, skipping and moving onto the next...")
        
    return listy 
    

