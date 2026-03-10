import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

house={"type of house ":["Flat","Farmhouse","Villa","Penthouse","Apartment",
                         "Bunglow","Farmhouse","flat","Apartment"],
      "area":[200,800,500,400,100,400,900,150,200],
       "size":[2,10,12,6,2,5,11,1,4],
       "price(cr)":[2500000,100000000,200000000,30000000,1000000,5000000,150000000,1500000,3000000]}
df=pd.DataFrame(house)
df

plt.xlabel("area")
plt.ylabel("price(cr)")
plt.plot(df["area"],df["price(cr)"],marker="*")
plt.show

#before Normalization
plt.scatter(df["size"], df["price(cr)"])
plt.xlabel("Size (BHK)")
plt.ylabel("Price (cr)")
plt.title("Size(BHK) and Price(cr){before normalized value}")
plt.grid(True)
plt.show()

plt.scatter( df["size"],  df["area"])
plt.xlabel("Size (BHK)")
plt.ylabel("area (square foot)")
plt.title("Size(BHK) and area(square foot){before normilized value}")
plt.grid(True)
plt.show()

#after Normalization
maxa = max( df["area"])
mina = min( df["area"])
df["area"] = ( df["area"] - mina) / (maxa - mina)
maxp=max( df["price(cr)"])
minp=min( df["price(cr)"])
df["price(cr)"] = ( df["price(cr)"] - minp) / (maxp - minp)
print("\n new data set after normalized value:\n")
print(df)

plt.scatter( df["size"],  df["price(cr)"])
plt.xlabel("Size (BHK)")
plt.ylabel("Price (cr)")
plt.title("Size(BHK) and Price(cr){after normilized value}")
plt.grid(True)
plt.show()

plt.scatter( df["size"], df["area"])
plt.xlabel("Size (BHK)")
plt.ylabel("area (square foot)")
plt.title("Size(BHK) and area(square foot){after normilized value}")
plt.grid(True)
plt.show()

y= df["price(cr)"]
x=( df["size"])
plt.title("Size(BHK) and Price(cr){after normilized value")
plt.xlabel("size(BHK)")
plt.ylabel("price(cr)")
plt.plot(x,y)
plt.show()    
