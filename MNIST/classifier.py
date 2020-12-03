import numpy as np
from tensorflow.keras import models
from tensorflow.keras import layers 


def update_dictionary_items(dict1, dict2):
    
    if dict2 is None:
        return dict1
    for k in dict1:
        if k in dict2:
            dict1[k] = dict2[k]

    return dict1


class convnet():
    def __init__(self, parameters={}):
        self.params = update_dictionary_items({'epochs':5,'batch_size':64,'act':'relu','filter1':32,'filter2':64,'filter3':64,'filter4':64}, parameters)
        self.params['filter1']
    def learn(self, X, y):
        
        #construction of model
        self.net = models.Sequential()
        self.net.add(layers.Conv2D(self.params['filter1'],(3,3),activation = self.params['act'],input_shape=(28,28,1)))
        self.net.add(layers.MaxPooling2D((2,2)))
        self.net.add(layers.Conv2D(self.params['filter2'],(3,3),activation = self.params['act']))
        self.net.add(layers.MaxPooling2D((2,2)))
        self.net.add(layers.Conv2D(self.params['filter3'],(3,3),activation = self.params['act']))
        self.net.add(layers.Flatten())
        self.net.add(layers.Dense(self.params['filter4'],activation=self.params['act']))
        self.net.add(layers.Dense(10,activation ='softmax'))

        #compile
        self.net.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

        #training
        self.net.fit(X,y,epochs=self.params['epochs'],batch_size=self.params['batch_size'])


        

    def predict(self, Xtest,ytest):
        test_loss,test_acc = self.net.evaluate(Xtest,ytest)
        return test_acc
      
