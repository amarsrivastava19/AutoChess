#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import chess
import chess.pgn
import numpy as np
import random
import pandas as pd


# PGN_initializer opens a .pgn file and reads it into memory

# PGN_Counter grabs the number of games in a .pgn file.
# This is used to loop through the .pgn files within the pipeline.


def PGN_initializer(file):

    pgn = open(file)
    return pgn


def PGN_Counter(filepath):

    pgn = PGN_initializer(filepath)
    counter = 0
    for i in range(0, 60000):
        first_game = chess.pgn.read_game(pgn)
        if first_game is None:
            break
        else:
            counter = counter + 1

    pgn = PGN_initializer(filepath)

    return counter, pgn


def string_cleaner(stringy):
    x = "".join("x"*int(char) if char.isdigit() else char for char in stringy)
    return x


def board_creator(array, peice):
    board = np.zeros((8, 8))
    for i in range(0, len(array)):
        if peice in array[i]:
            indices = [n for (n, e) in enumerate(array[i]) if e == peice]
            for j in indices:
                board[i, j] = 1

    return board


def extra_detail_extractor(stringy):

    listy = []
    fen_array = stringy.split("/")
    extra_details = fen_array[-1].split(" ")[1:]

    side = extra_details[0]

    if side.lower() == 'w':
        tomove = [1.0]
    else:
        tomove = [0.0]

    castling = extra_details[1]

    rights = [0.0, 0.0, 0.0, 0.0]

    if "K" in castling:
        rights[0] = 1.0
    if "Q" in castling:
        rights[1] = 1.0
    if "k" in castling:
        rights[2] = 1.0
    if "q" in castling:
        rights[3] = 1.0

    listy = listy + tomove+rights

    return listy


def fen_to_vec(stringy, resultW, resultB):

    masterlist = []

    fen_array = stringy.split("/")
    fen_array[-1] = fen_array[-1].split(" ")[0]

    for i in range(0, len(fen_array)):
        fen_array[i] = string_cleaner(fen_array[i])

    for peice in ["R", "N", "B", "Q", "K", "P"]:
        w_board = board_creator(fen_array, peice)
        b_board = board_creator(fen_array, peice.lower())
        masterlist = masterlist+w_board.flatten().tolist() +
        b_board.flatten().tolist()

    extra_details = extra_detail_extractor(stringy)
    masterlist = masterlist + extra_details
    masterlist = masterlist+[resultW, resultB]

    return masterlist


def Pipeline(filepath):

    total_list = []
    num_games, pgn = PGN_Counter(filepath)

    for i in range(0, num_games):

        game = chess.pgn.read_game(pgn)
        result = game.headers["Result"]

        if result == "1/2-1/2":
            continue

        if result == "1-0":
            resultW = 1.0
            resultB = 0.0

        if result == "0-1":
            resultW = 0.0
            resultB = 1.0

        if result != "1/2-1/2" and result != "1-0" and result != "0-1":
            print("ERROR ERRROR ERRROR ERROR R")

        x = str(game.mainline_moves())
        first_split = x.split(".")
        second_split = [i.split(" ")[1:3] for i in
                        first_split if len(i.split(" ")) == 4]

        white_moves = [i[0] for i in second_split]
        black_moves = [i[1] for i in second_split]

        viable_moves = [i for i, x in enumerate(white_moves) if
                        ("x" not in white_moves[i]) and
                        ("x" not in black_moves[i]) and
                        (i > 5)]

        # pick 10 random moves
        try:
            move_picker = random.sample(viable_moves, k=10)

            to_move = [random.randint(0, 1) for i in range(0, 10)]

        except:
            move_picker = viable_moves
            to_move = [random.randint(0, 1) for i in viable_moves]

        for j, k in zip(move_picker, to_move):
            try:
                board = game.board()
                moves = [move for move in game.mainline_moves()]
                for move in moves[0:(2*j+k)]:
                    board.push(move)
                fen = board.fen()
                vector = fen_to_vec(fen, resultW, resultB)

                total_list.append(vector)

            except:
                print("Bad PGN Parser; Skipping...")

    return total_list


def File2Pipeline(in_path, out_path):
    listy = []
    files = os.listdir(in_path)

    for i, file in enumerate(files):
        try:
            print("Reading file# " + str(i) + "/" + str(len(files)))
            pathy = path + "\\" + file
            x = Pipeline(pathy)
            listy = listy + x
        except:
            print("This is a bad file, skipping and moving onto the next...")

    df = pd.DataFrame(listy)

    df.to_csv(out_path)

    return df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[17]:





# In[ ]:





# In[ ]:




