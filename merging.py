# import pandas as pd
import numpy as np
import pandas as pd
placehold = ["delete me"]
old_df=pd.DataFrame(placehold,columns = ['Lactobacillus'])
old_df["a"] = ["delete me"]
# indicesdel = range(0,159)
# old_df = pd.read_csv("/home/leen/Desktop/clean_csvs/donezos/currentlyworking.csv",index_col=0)
import os
paths = "/home/leen/Desktop/clean_csvs/allthings/"
names = []
i = 0
for filename in os.listdir(paths):
    # extract the sample name from the file (csv)
    i = i+1
    indicesdel = range(0,i)
    namesplitter = filename.split('.')
    sample_id = namesplitter[0]
    names.append(sample_id)

    print(sample_id)
    newname = paths + filename
    # read in the file 
    df = pd.read_csv(newname,index_col=0,engine='python')
    print(filename)
    # print(df)
    # transpose
    df = df.T
    # print(df)
    # make bacteria name the column name
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df.round(20)
    df["a"] = ["0"]
    print(df)

    newboy = pd.merge(old_df, df, how='outer')
    newboy.rename(index=dict(zip(names,indicesdel)))
    newboy.replace(np.nan, 0)
    # print(newboy)

    old_df = newboy
    with open("names.txt", "w") as output:
        output.write(str(names))
    old_df.replace(np.nan, 0)

    old_df.to_csv("currentlyworking_2.csv")

print(old_df)






