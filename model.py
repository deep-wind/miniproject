import pandas as pd
import datetime
import numpy as np
import pandas as pd
import tensorflow
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Bidirectional

''' Loading data '''
df = pd.read_csv('lstm.csv')
df.head()

''' Cleaning Data '''
#dataframe.drop['Date'].values
df['Power generated by system | (kW)'].replace(0, np.nan, inplace=True)
df['Power generated by system | (kW)'].fillna(method='ffill', inplace=True)


X = df.drop(columns=['Power generated by system | (kW)'])
Y = df[['Power generated by system | (kW)']]
X=np.array(X).reshape(-1,1,4)
Y=np.array(Y).reshape(-1,1,1)


model = Sequential()
model.add(Bidirectional(LSTM(150, activation='relu',input_shape=(-1,1,4))))
model.add(Dense(1))
model.compile(loss='mae', optimizer='adam')
model.fit(X, Y,epochs=100,callbacks=[keras.callbacks.EarlyStopping(patience=3)])

test_data = np.array([[-4.858,0.989741,6.651,273]])
o=model.predict(test_data.reshape(-1,1,4), batch_size=1)


# Saving model to disk
models=model.save('model.h5')

# # Loading model to compare the results


