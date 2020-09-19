#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Main workflow that takes in a list of white moves, a list of black moves, who should be the last to move,
### who was the winner, and who was the loser. 

### White [list of strings] : List of white moves; ex. [e4, Nf3,...]
### Black [list of strings] : List of black moves; ex. [d7, e6,...]
### tomove [int32] : 0 if white should be last to move, 1 if black should be last to move
### resultW [int32] : 1 if white won game
### resultB [int32] : 1 if black won game

### returns list of magnitude 773 for feeding into training algorithm. 



def MasterChess(white,black,tomove,resultW,resultB):
    
    
    
    dictyRN1 = {"a":[i for i in range(0,64,8)],
           "b":[i for i in range(1,64,8)],
           "c":[i for i in range(2,64,8)], 
           "d":[i for i in range(3,64,8)], 
           "e":[i for i in range(4,64,8)], 
           "f":[i for i in range(5,64,8)], 
           "g":[i for i in range(6,64,8)], 
           "h":[i for i in range(7,64,8)]}

    dictyRN2 = {"1":[i for i in range (0,8)], 
            "2":[i for i in range (8,16)], 
            "3":[i for i in range (16,24)], 
            "4":[i for i in range (24,32)], 
            "5":[i for i in range (32,40)], 
            "6":[i for i in range (40,48)], 
            "7":[i for i in range (48,56)], 
            "8":[i for i in range (56,64)]}
    

    enpass_W = [i for i in range(32,40)]

    enpass_B = [i for i in range(24,32)]
    
    
    king_castle_W = [1]
    queen_castle_W = [1]
    king_castle_B = [1]
    queen_castle_B = [1]

    
    double_pieces = ["N","R","B"]
    
    total_board_W, total_board_B = board_creator()
    
    lastmove_W = []
    lastmove_B = []
    counter = 0 

    for i,j in zip(white,black):

        if i == white[-1] and tomove == 0:

            masterlist = total_board_W + total_board_B
            masterlist = sum(masterlist, [])
            for i in [king_castle_W,king_castle_B,queen_castle_W,queen_castle_B, [tomove],[resultW],[resultB]]: 
                masterlist.append(i[0])
            return masterlist 

        i = i.replace("+","")
        j = j.replace("+","")

        if len(i) == 2: 
            lastmove_W.append(i[-2::1])

        if len(j) == 2: 
            lastmove_B.append(j[-2::1])

        if i == "O-O": 
            king_castle_W[0] = 0
            queen_castle_W[0] = 0
            total_board_W[1][4] = 0 
            total_board_W[4][7] = 0
            total_board_W[1][6] = 1
            total_board_W[4][5] = 1

        if i == "O-O-O": 
            king_castle_W[0] = 0
            queen_castle_W[0] = 0
            total_board_W[1][4] = 0
            total_board_W[4][0] = 0
            total_board_W[1][2] = 1 
            total_board_W[4][3] = 1

        if i != "O-O" and i!= "O-O-O": 

            piece_W = i[0]
            pos_W = i[-2::1]

            if pos2int(pos_W) == False: 

                pos_W = i.replace("=Q","").replace("=N","").replace("=B","").replace("=R", "")[-2::1]

            pos_W_int = pos2int(pos_W)

            ### If there is a take in the white move, remove the respective piece in the black camp

            if "x" in i: 
                for board in total_board_B:
                    if board[pos_W_int] == 1:
                        board[pos_W_int] = 0

            ### adjust Queens position

            if piece_W == "Q": 
                total_board_W[3] = [0]*64
                total_board_W[3][pos_W_int] = 1

            ### adjust Kings position

            if piece_W == "K": 
                total_board_W[1] = [0]*64
                total_board_W[1][pos_W_int] = 1

            ### adjust Bishop's position 

            if piece_W == "B": 
                prev_B = BishopFinder(pos_W_int)
                for pos in prev_B: 
                    if total_board_W[5][pos] == 1: 
                        total_board_W[5][pos] = 0


                total_board_W[5][pos_W_int] = 1

            ### adjust Knight's position 

            if piece_W == "N": 

                N_temp = i.replace("x","")
                if len(N_temp) >= 4: 
                    if i[1] in dictyRN1: 
                        for pos in dictyRN1[i[1]]: 
                            if total_board_W[2][pos] == 1: 
                                total_board_W[2][pos] = 0 

                    if i[1] in dictyRN2: 
                        for pos in dictyRN2[i[1]]: 
                            if total_board_W[2][pos] == 1: 
                                total_board_W[2][pos] = 0

                else: 
                    prev_N = KnightFinder(pos_W_int)
                    for pos in prev_N: 
                        if total_board_W[2][pos] == 1: 
                            total_board_W[2][pos] = 0

                total_board_W[2][pos_W_int] = 1

            ### adjust Rook's position 

            if piece_W == "R": 

                R_temp = i.replace("x","")

                if len(R_temp) >= 4: 
                    if i[1] in dictyRN1: 
                        for pos in dictyRN1[i[1]]: 
                            if total_board_W[4][pos] == 1: 
                                total_board_W[4][pos] = 0


                    if i[1] in dictyRN2: 
                        for pos in dictyRN2[i[1]]: 
                            if total_board_W[4][pos] == 1: 
                                total_board_W[4][pos] = 0

                else: 

                    prev_R_list = [i for i, x in enumerate(total_board_W[4]) if x == 1 ]

                    if len(prev_R_list) == 1: 

                        prev_R = RookFinder(pos_W_int)

                        for pos in prev_R: 
                            if total_board_W[4][pos] == 1: 
                                total_board_W[4][pos] = 0

                    else:
                        bad_rook = []

                        for rook in prev_R_list: 
                            listy = R_PathFinder(rook,pos_W_int)
                            if listy == False: 
                                bad_rook.append(rook)
                            else:
                                for r in listy: 
                                    for board in total_board_W+total_board_B: 
                                        if board[r] == 1:
                                            bad_rook.append(rook)
                                            break

                        del_rook_list = [i for i in prev_R_list if i not in bad_rook]

                        good_rook = del_rook_list[0]
                        total_board_W[4][good_rook] = 0
                            
                            
                total_board_W[4][pos_W_int] = 1

            ### adjust board positions for pawns

            if piece_W in ["a","b","c","d","e","f","g","h"]:
                if "=" in i:
                    if "x" in i: 
                        if i[0] < i[2]: 
                            total_board_W[0][pos_W_int - 9] = 0
                        else: 
                            total_board_W[0][pos_W_int - 7] = 0

                    if i[-1] == "Q": 
                        total_board_W[3][pos_W_int] = 1
                    elif i[-1] == "R": 
                        total_board_W[4][pos_W_int] = 1
                    elif i[-1] == "B": 
                        total_board_W[5][pos_W_int] = 1
                    elif i[-1] == "N": 
                        total_board_W[1][pos_W_int] = 1




                if ("x" in i) and not ("=" in i): 

                    if pos2int(lastmove_B[-1]) in enpass_W and abs(pos_W_int - pos2int(lastmove_B[-1])) == 8 :
                        if i[0] < i[-2]: 
                            total_board_W[0][pos_W_int-9] = 0
                            total_board_B[0][pos_W_int - 8] = 0
                        else: 
                            total_board_W[0][pos_W_int-7] = 0                            
                            total_board_B[0][pos_W_int - 8] = 0

                    elif i[0] < i[-2]:
                        total_board_W[0][pos_W_int-9] = 0
                    else:
                        total_board_W[0][pos_W_int-7] = 0

                else:

                    if pos_W_int in enpass_B: 
                        if total_board_W[0][pos_W_int-16] == 1:
                            total_board_W[0][pos_W_int-16] = 0
                        else: 
                            total_board_W[0][pos_W_int-8] = 0 
                    else: 
                        total_board_W[0][pos_W_int-8] = 0 

                total_board_W[0][pos_W_int] = 1



        if j == black[-1] and tomove == 1:

            masterlist = total_board_W + total_board_B
            masterlist = sum(masterlist, [])
            for i in [king_castle_W,king_castle_B,queen_castle_W,queen_castle_B, [tomove],[resultW],[resultB]]: 
                masterlist.append(i[0])
            return masterlist 


        if j == "O-O": 
            king_castle_B[0] = 0
            queen_castle_B[0] = 0 
            total_board_B[1][60] = 0
            total_board_B[4][63] = 0
            total_board_B[1][62] = 1
            total_board_B[4][61] = 1 

        if j == "O-O-O": 
            king_castle_B[0] = 0
            queen_castle_B[0] = 0
            total_board_B[1][60] = 0
            total_board_B[4][56] = 0
            total_board_B[1][58] = 1 
            total_board_B[4][59] = 1

        if j != "O-O" and j!= "O-O-O": 

            piece_B = j[0]
            pos_B = j[-2::1]
            pos_B_int = pos2int(pos_B) 

            ### If there is a take in the black move, remove the respective piece in the black camp

            if "x" in j:
                for board in total_board_W: 
                    if board[pos_B_int] == 1: 
                        board[pos_B_int] = 0
            ### adjust Queens position for Black 

            if piece_B == "Q": 
                total_board_B[3] = [0]*64
                total_board_B[3][pos_B_int] = 1

            ### adjust Kings position for Black 

            if piece_B == "K": 
                total_board_B[1] = [0]*64
                total_board_B[1][pos_B_int] = 1

            ### adjust Bishop's position for Black 

            if piece_B == "B": 
                prev_B = BishopFinder(pos_B_int)
                for pos in prev_B: 
                        if total_board_B[5][pos] == 1: 
                            total_board_B[5][pos] = 0


                total_board_B[5][pos_B_int] = 1 


            ### adjust Knight's position for Black 

            if piece_B == "N": 

                N_temp = j.replace("x","")

                if len(N_temp) >= 4: 

                    if j[1] in dictyRN1: 
                        for pos in dictyRN1[j[1]]: 
                            if total_board_B[2][pos] == 1: 
                                total_board_B[2][pos] = 0 

                    if j[1] in dictyRN2: 
                        for pos in dictyRN2[j[1]]: 
                            if total_board_B[2][pos] == 1: 
                                total_board_B[2][pos] = 0

                else: 
                    prev_N = KnightFinder(pos_B_int)
                    for pos in prev_N: 
                        if total_board_B[2][pos] == 1: 
                            total_board_B[2][pos] = 0

                total_board_B[2][pos_B_int] = 1

            ### adjust Rook's position for Black 

            if piece_B == "R": 

                R_temp = j.replace("x","")

                if len(R_temp) >= 4:

                    if j[1] in dictyRN1: 
                        for pos in dictyRN1[j[1]]: 
                            if total_board_B[4][pos] == 1: 
                                total_board_B[4][pos] = 0


                    if j[1] in dictyRN2: 
                        for pos in dictyRN2[j[1]]: 
                            if total_board_B[4][pos] == 1: 
                                total_board_B[4][pos] = 0

                else: 

                    prev_R_list = [i for i, x in enumerate(total_board_B[4]) if x == 1 ]

                    if len(prev_R_list) == 1: 
                        prev_R = RookFinder(pos_B_int)

                        for pos in prev_R: 
                            if total_board_B[4][pos] == 1: 
                                total_board_B[4][pos] = 0

                    else:
                        bad_rook = []
                        for rook in prev_R_list: 
                            listy = R_PathFinder(rook,pos_B_int)
                            if listy == False: 
                                bad_rook.append(rook)
                            else:
                                for r in listy:
                                    for board in total_board_W+total_board_B: 
                                        if board[r] == 1:
                                            bad_rook.append(rook)
                                            break

                        del_rook_list = [i for i in prev_R_list if i not in bad_rook]
                        good_rook = del_rook_list[0]

                        total_board_B[4][good_rook] = 0

                total_board_B[4][pos_B_int] = 1                

            ### adjust board position for pawns for black 

            if piece_B in ["a","b","c","d","e","f","g","h"]:

                if "=" in j:
                    if "x" in j: 
                        if j[0] < j[2]: 
                            total_board_B[0][pos_B_int + 7] = 0
                        else: 
                            total_board_B[0][pos_B_int + 9] = 0

                    if j[-1] == "Q": 
                        total_board_B[3][pos_B_int] = 1
                    elif j[-1] == "R": 
                        total_board_B[4][pos_B_int] = 1
                    elif j[-1] == "B": 
                        total_board_B[5][pos_B_int] = 1
                    elif j[-1] == "N": 
                        total_board_B[1][pos_B_int] = 1


                if ("x" in j) and not ("=" in j):
                    if pos2int(lastmove_W[-1]) in enpass_B and abs(pos_B_int - pos2int(lastmove_W[-1])) == 8 :
                        if j[0] < j[-2]: 
                            total_board_B[0][pos_B_int+9] = 0
                            total_board_W[0][pos_W_int + 8] = 0
                        else: 
                            total_board_B[0][pos_W_int+7] = 0                            
                            total_board_W[0][pos_W_int + 8] = 0

                    elif j[0] < j[-2]:
                        total_board_B[0][pos_B_int+7] = 0
                    else:
                        total_board_B[0][pos_B_int+9] = 0

                else:
                    if pos_B_int in enpass_W: 
                        if total_board_B[0][pos_B_int+16] == 1:
                            total_board_B[0][pos_B_int+16] = 0
                        else: 
                            total_board_B[0][pos_B_int+8] = 0 
                    else: 
                        total_board_B[0][pos_B_int+8] = 0 


                total_board_B[0][pos_B_int] = 1

    
    ### return masterlist of all boards/castle rights/ side to move 
    
    masterlist = total_board_W + total_board_B
    masterlist = sum(masterlist, [])
    for i in [king_castle_W,king_castle_B,queen_castle_W,queen_castle_B, [tomove],[resultW],[resultB]]: 
        masterlist.append(i[0])

    return masterlist 

