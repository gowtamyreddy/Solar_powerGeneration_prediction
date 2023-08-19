import sys
import numpy as np
import pandas as pd
from sklearn import *
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
training_data = np.genfromtxt('weather3.csv', delimiter=',')
inputs = training_data[:,:-1]
outputs = training_data[:, -1]
training_inputs = inputs[:180]
training_outputs = outputs[:180]
testing_inputs = inputs[180:]
testing_outputs = outputs[180:]
classifier = MultinomialNB()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
testSet = [[float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6])]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('MNB prediction on the given set is:',predictions)