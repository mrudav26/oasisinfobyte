# -*- coding: utf-8 -*-
"""TASK 5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17OF2jhnhT9yoYRthj3LWhAEX5nRTOmKn

## **Task-5 : SALES PREDICTION USING PYTHON**

## **Name: Mrudav Pranav Patel**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/Advertising.csv')
df.head()

df.shape

df1 = df.drop(['Unnamed: 0'],axis = 'columns')
df1.head()

df1.columns

df1.isnull().sum()

x = df1.drop(['Sales'], axis = 'columns')
x.head()

y = df1['Sales']
y.head()

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2)

x_train

len(x_train)

x_test.head()

len(x_test)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x_train,y_train)

model.score(x_test,y_test)

model.predict(x_test)

