import pandas as pd 
import numpy as np


# creating the Model Class

class RegressionLineaire():
    def __init__(self,learning_rate,no_of_iteration):
        self.learning_rate=learning_rate
        self.no_of_iteration=no_of_iteration
    
    def fit(self,X,Y):
        X=np.array(X)
        Y=np.array(Y)
        
        # number of training example and number of feature  
        self.m,self.n=X.shape

        # initializing the weight and bias
        self.w=np.zeros(self.n)
        self.b=0
        self.X=X
        self.Y=Y

        # implementing gradient descent
        for i in range(self.no_of_iteration):
            self.update_weights()
    
    def update_weights(self):
        Y_prediction=self.predict(self.X)

        # calculating gradient
        dw = -( 2 * (self.X.T).dot(self.Y - Y_prediction)) / self.m
        db = -( 2 * np.sum(self.Y - Y_prediction)) / self.m

        # applying gradient on w & b
        self.w = self.w - self.learning_rate * dw
        self.b = self.b - self.learning_rate * db


    
    def predict(self,X):
        return X.dot(self.w) + self.b



        
