import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
dataset={
    "age":[10,14,17,20,25,3],
    "vote":[1,0,0,1,1,0]
}
df=pd.DataFrame(dataset)
print(df)
x=df[["age"]]
y=df["vote"]
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LogisticRegression()
model.fit(x_train,y_train)
prediction=model.predict([[18]])
print(prediction)
