import matplotlib.pyplot as plt

import pandas as pd

house={"type of house ":["Flat","Farmhouse","Villa","Penthouse","Apartment",
                         "Bunglow","Farmhouse","flat","Apartment"],
      "Area of house(sq foot)":[200,800,500,400,100,400,900,150,200],
       "size of house(BHK)":[2,10,12,6,2,5,11,1,4],
       "Cost of house":[2500000,100000000,200000000,30000000,1000000,5000000,150000000,1500000,3000000]}
df=pd.DataFrame(house)
df

plt.xlabel("Area of house(sq foot)")
plt.ylabel("Cost of house")
plt.plot(df["Area of house(sq foot)"],df["Cost of house"],marker="*")
plt.show
mini=df["Area of house(sq foot)"].min()
maxi=df["Cost of house"].max()
list_area=[]
for i in df["Area of house(sq foot)"]:
    x=(i-mini)/(maxi-mini)
    list_area.append(x)
df["Normalized Area"]=list_area
df
