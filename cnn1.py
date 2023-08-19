#Importing Numpy
import numpy as np


#Importing Pandas
import pandas as pd


#Importing Matpplotlib
import matplotlib.pyplot as plt



#Importing Tensorflow
import tensorflow as tf


#Importing Keras backend
import tensorflow.keras.backend as K



#Print Tensorflow Version
print(tf.__version__)



#Importing Warnings
import warnings

#Ignoring Warnings
warnings.filterwarnings("ignore")


#Function for getting F1-Score
def get_f1(y_true, y_pred): #taken from old keras source code
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2*(precision*recall)/(precision+recall+K.epsilon())
    return f1_val


#Read the dataset into a dataframe
df = pd.read_csv('weather3.csv')

data = df.to_numpy()


#All columns except last column are considered as inputs
inputs = data[:,:-1]


#Last Column is considered as outputs
outputs = data[:, -1]



#First Thousand rows are considered for training.
training_data = inputs[:180]


#Training labels are set to the last column values of first thousand rows
training_labels = outputs[:180]



#Remaining Rows, Beyond 180 are considered for testing
test_data = inputs[180:]


#Testing labels are set to the last column values of remaining rows
test_labels = outputs[180:]


#Tensorflow Initiation
tf.keras.backend.clear_session()




#Configure the model
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(), 
                                    tf.keras.layers.Dense(128, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(64, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(32, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])
									
									
#Comiling the model
model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=[get_f1])



#Creation of the model
model.fit(training_data, training_labels, epochs=100)

#First Test Set Assinment
testSet = [[8,21,6,6,78,1022]]


#First Test Set Conversion to Pandas Data Frame
test = pd.DataFrame(testSet)


#Prediction on First Test Set Using the Model
predictions = model.predict(test)


#Finding the first test set label
classes=np.argmax(predictions,axis=1)


#printing the first test set label
print('DL Model Prediction on the first test set is:',classes)



#Second Test Set Assinment
testSet = [[8,21,6,6,78,1022]]


#Second Test Set Conversion to Pandas Data Frame
test = pd.DataFrame(testSet)


#Prediction on Second Test Set Using the Model
predictions =  model.predict(test)


#Finding the second test set label
classes=np.argmax(predictions,axis=1)


#printing the second test set label
print('DL Model Prediction on the second test set is:',classes)

#Third Test Set Assinment
testSet = [[20,33,0,13,93,1027]]


#Third Test Set Conversion to Pandas Data Frame
test = pd.DataFrame(testSet)


#Prediction on Third Test Set Using the Model
predictions =  model.predict(test)


#Finding the Third test set label
classes=np.argmax(predictions,axis=1)


#printing the Third test set label
print('DL Model Prediction on the Third test set is:',classes)

