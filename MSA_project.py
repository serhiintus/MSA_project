import pandas as pd

#take path to the data
path_top = "C:\\Users\\K90006169\\MSA_project\\PH71_top_Comp.csv" #"C:/MSA_project/data/PH59_bot_Comp.csv"
path_bot = "C:\\Users\\K90006169\\MSA_project\\PH71_bot_Comp.csv"

#read the data
df = pd.read_csv(path_top)

#define variables
df_columns = ["OffsetX", "OffsetY"]
modules = 5
components_top = ["R201", "R205"]
components_bot = ["R303", "R510"]
msa_data = pd.DataFrame(columns=[f"TOP_{components_top[0]}_X", f"TOP_{components_top[1]}_Y"])

for j in components_top:
    


    filtered_data = pd.DataFrame(columns=df_columns)
    for i in range(modules):
        filt = (df["ModuleID"] == i + 1) & (df["Location Name"] == j)
        filtered_data =pd.concat([filtered_data, df.loc[filt, df_columns].iloc[:9]], ignore_index=True)

msa_data.to_excel("PH71TOP_data_fo_MSA.xlsx", index=False) #("PH59_data_fo_MSA.xlsx", index=False)
