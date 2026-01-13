import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from linear_regression import RegressionLineaire

# loading data into dataFrame
salary_data=pd.read_csv("data/salary_data.csv")


# showing the number of null values in each columns 
print(salary_data.isnull().sum())

# showing the size of data
print(salary_data.shape)

# separating the feature and targets 
X = salary_data.drop(columns=["Salary"]).values      
Y = salary_data["Salary"].values
# print(X)

# separating training and test data
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=3)


# creating instance of our RegressionLineaire Model 
regression_model=RegressionLineaire(learning_rate=0.002,no_of_iteration=1000)


#  training the model
regression_model.fit(X_train,Y_train)

# printing the parameters weight and bias
print("the weights is : ",regression_model.w)
print("the bias is : ",regression_model.b)



# prediciting  values 
predicted_values=regression_model.predict(X_test)



# ploting Y_test and predicted_values to compare the see the bias 
plt.title("The Salary in fonction of Years of experience")
plt.scatter(X_test,Y_test,color="red",label="Y test")
plt.plot(X_test,predicted_values,color="green",label="Y predicted")
plt.legend()


plt.show()