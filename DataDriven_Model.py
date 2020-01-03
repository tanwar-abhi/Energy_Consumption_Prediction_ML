#!/usr/bin/env python
# coding: utf-8



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
import random



DATA = pd.read_csv('//home//abhishek//Programs_practice//Machine_Learning//Projects_Practice//Energy_Consumption_Prediction_ML//energydata_complete.csv')




print(DATA.shape,'\n')
print(DATA.columns,'\n')
DATA.info()


DATA.head()



dframe = DATA[['Appliances', 'lights', 'T1', 'RH_1', 'T2', 'RH_2','T_out', 'Press_mm_hg', 'RH_out', 'Windspeed']]
dframe.corr()





plt.scatter(dframe.Appliances, dframe.T1,color='red')
plt.xlabel('Appliances')
plt.ylabel('Temperature')



plt.scatter(dframe.T1,dframe.Appliances, color='red')



plt.scatter(dframe.RH_1, dframe.Appliances, color='blue')
plt.xlabel('Humidity in percentage')
plt.ylabel('Power usage of appliance')



plt.scatter(dframe.T2,dframe.Appliances, color='red')



x = dframe.T1
y = dframe.Appliances



msk = np.random.rand(len(dframe)) < 0.8
trainSet = dframe[msk]
testSet = dframe[~msk]


'''
from sklearn import linear model
regressionModel = linear_model_LinearRegression()
train_x = np.asanyarray(trainSet[['T1']])


from sklearn import linear_model
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit(train_x,train_y)
print('Coefficients : ',regr.coef_)

print('Intercept : ',regr.intercept_)

'''