import numpy as np
import pandas as pd
from sklearn import *
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
training_data = np.genfromtxt('weather3.csv', delimiter=',')
inputs = training_data[:,:-1]
outputs = training_data[:, -1]
training_inputs = inputs[:360]
training_outputs = outputs[:360]
testing_inputs = inputs[360:]
testing_outputs = outputs[360:]
classifier = MultinomialNB()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
print ("The accuracy of MNB Classifier on testing data is: " + str(accuracy))
'''
testSet = [[8,21,6,6,78,1022]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('MNB prediction on the first test set is:',predictions)
testSet = [[0,11,0,0,41,997]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('MNB prediction on the second test set is:',predictions)
testSet = [[20,33,0,13,93,1027]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('MNB prediction on the third test set is:',predictions)
'''