import pandas as pd


path = "C:/MSA_project/data/PH59_bot_Comp.csv"
df = pd.read_csv(path)

columns = ["Index", "Location Name", "ModuleID", "OffsetX", "OffsetY", "Comp.Result", 'SizeX', 'SizeY']
modules = [1, 2, 3, 4, 5]
components = ["C1"]

filt = (df["ModuleID"].isin(modules)) & (df["Location Name"].isin(components))

filtered_data = df.loc[filt, columns]


df.to_excel("PH59_data_fo_MSA.xlsx", index=False)

#some = df.columns
#print(type(some))
#for i in some:
#    print(i)