#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import pandas as pd
import numpy as np
import keras
import gc
import time
from random import randint

np.random.seed(55555)
random.seed(444444)

files = [r"C:\Users\amars\Desktop\R_Zero Github\1100_training_data.csv",
         r"C:\Users\amars\Desktop\R_Zero Github\953_training_data.csv",
         r"C:\Users\amars\Desktop\R_Zero Github\992_training_data.csv",
         r"C:\Users\amars\Desktop\R_Zero Github\1253_training_data.csv",
         r"C:\Users\amars\Desktop\R_Zero Github\1310_training_data.csv",
         r"C:\Users\amars\Desktop\R_Zero Github\1279_training_data.csv",
         r"C:\Users\amars\Desktop\R_Zero Github\1253_training_data.csv",
         r"C:\Users\amars\Desktop\R_Zero Github\1200_training_data.csv",
         r"C:\Users\amars\Desktop\R_Zero Github\1035_training_data.csv",
         r"C:\Users\amars\Desktop\R_Zero Github\1010_training_data.csv"]

lengths = [315250, 290495, 256224, 585376, 772750, 637912, 585376,
           460465, 212329, 369435]


def dataframe_sampler(files):
  
    listy = []

    for file, i in zip(files, lengths):       
            n = i
            s = random.randint(30000, 50000)
            skip = sorted(random.sample(range(1, n+1), n-s))
            df_add = pd.read_csv(file, skiprows=skip)
            df_add = df_add.drop('Unnamed: 0', axis=1)
            df_add = df_add[df_add['773'] < 2]
            
            listy.append(df_add)
            
    df = pd.concat(listy)
    df.head()
    
    return df


def dataframe_splitter(df):
    
    n = len(df)
    np_main = np.empty([n, 775])
    np_comp = np.empty([n, 775])
    
    df_np = df.to_numpy()
    np_1 = df[df['773'] == 1.0].to_numpy()
    np_0 = df[df['773'] == 0.0].to_numpy()
    
    n_1 = len(np_1)
    n_0 = len(np_0)
    
    for i in range(0, n): 
        np_main[i] = df_np[np.random.choice(n)]
        if np_main[i][773] == 1.0: 
            np_comp[i] = np_0[np.random.choice(n_0)]
        else: 
            np_comp[i] = np_1[np.random.choice(n_1)]
                
    df_main = pd.DataFrame(np_main)
    df_comp = pd.DataFrame(np_comp)
    
    return df_main, df_comp
    

for i in range(0, 200):
    
    try:
        
        print("Starting Trial# " + str(i))
        
        model = keras.models.load_model(r"C:\Users\amars\Desktop\R_Zero Github\Evaluation_Network")
        
        df = dataframe_sampler(files)
        df = df.sample(frac=1).reset_index(drop=True)
        
        train = df[0:int(0.85*len(df))]
        val = df[int(0.85*len(df)):len(df)].reset_index(drop=True)

        df_main, df_comp = dataframe_splitter(train)

        val_main, val_comp = dataframe_splitter(val)

        train_output = df_main.iloc[:, 773::].to_numpy()

        val_output = val_main.iloc[:, 773::].to_numpy()

        df_main = df_main.drop([773, 774], axis=1)
        df_comp = df_comp.drop([773, 774], axis=1)
        val_main = val_main.drop([773, 774], axis=1)
        val_comp = val_comp.drop([773, 774], axis=1)

        train_input = [df_main, df_comp]

        val_input = [val_main, val_comp]

        model.fit(train_input, train_output,
                epochs=1,
                batch_size=2300,
                shuffle=True,
                validation_data=(val_input, val_output))
        
        model.save(r"C:\Users\amars\Desktop\R_Zero Github\Evaluation_Network")

    except Exception as e: 
        
        print("ERROR ERROR ERROR: WARNING")
        print(e)
        gc.collect()
        continue 
        

