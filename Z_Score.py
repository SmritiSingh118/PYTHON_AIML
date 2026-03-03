import numpy as np
import pandas as pd

house={"type of house ":["Flat","Farmhouse","Villa","Penthouse","Apartment",
                         "Bunglow","Farmhouse","flat","Apartment"],
      "Area of house(sq foot)":[200,800,500,400,100,400,900,150,200],
       "size of house(BHK)":[2,10,12,6,2,5,11,1,4],
       "Cost of house":[2500000,100000000,200000000,30000000,1000000,5000000,150000000,1500000,3000000]}
print("original Data-\n")
df=pd.DataFrame(house)
df
print("\n")

#normalization
n1=np.array(df["Area of house(sq foot)"])
n2=np.array(df["Cost of house"])
mean_n1=np.mean(n1)
mean_n2=np.mean(n2)
std_n1=np.std(n1)
std_n2=np.std(n2)
df["Area of house(sq foot)"] = ((df["Area of house(sq foot)"] - mean_n1) / (std_n1)).round(2)
df["Cost of house"] = ((df["Cost of house"] - mean_n2) / (std_n2)).round(2)
print("new Data-\n")
print(df)
