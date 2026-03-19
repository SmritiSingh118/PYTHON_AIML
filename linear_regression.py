import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
dataset={
    "age":[10,14,17,20,30],
    "weight":[45,32,23,28,25]
}
df=pd.DataFrame(dataset)
print(df)
x=df[["age"]]
y=df[["weight"]]
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
prediction=model.predict([[25]])
print(prediction)
