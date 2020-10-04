#!/usr/bin/env python
# coding: utf-8

# In[2]:


import s3fs
import pandas as pd
from keras.models import Sequential
from keras import layers
from keras.layers import Input, Dense
from keras.models import Model
import numpy as np

fs = s3fs.S3FileSystem(
    anon=False,
    key='AKIAJIS3ASQIL5AV5WZQ',
    secret='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')

autoencoder = Sequential()


autoencoder.add(layers.Dense(773, activation='relu'))
autoencoder.add(layers.Dense(600, activation='relu'))
autoencoder.add(layers.Dense(400, activation='relu'))
autoencoder.add(layers.Dense(200, activation='relu'))
autoencoder.add(layers.Dense(100, activation='relu'))
autoencoder.add(layers.Dense(200, activation='relu'))
autoencoder.add(layers.Dense(400, activation='relu'))
autoencoder.add(layers.Dense(600, activation='relu'))
autoencoder.add(layers.Dense(773, activation='sigmoid'))

autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

chunksize = 10 ** 4

for chunk in pd.read_csv(
        "s3://masterchess999/partial_training_data.csv",
        chunksize=chunksize):

    training_data = chunk.iloc[:, 1: 774]
    rows = len(training_data)
    x_train = training_data[0:int(0.8*rows)].to_numpy()
    x_test = training_data[int(0.8*rows):rows].to_numpy()

    autoencoder.fit(x_train,
                    x_train,
                    epochs=200,
                    batch_size=200,
                    shuffle=True,
                    validation_data=(x_test, x_test))

autoencoder.save("autoencoder")


# In[3]:





# In[4]:





# In[6]:





# In[ ]:




