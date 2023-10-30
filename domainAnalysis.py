import pandas as pd
import re

df=pd.read_csv("illegal1.csv")
for i in df.index:
    withoutProtocol=re.split("//",df["url"][i])[1]
    hostName=re.split("/",withoutProtocol)[0]
    specialCharacters = ['?', '-', '%', '=', '@', '!', '^', '&', '#']
    for j in specialCharacters:
        df[j][i]=0
    for j in hostName:
        if j in specialCharacters:
            df[j][i]+=1
    if i>810:
        break

df.to_csv("illegalFiltered1.csv")