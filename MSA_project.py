import pandas as pd


df = pd.read_csv("C:/MSA_project/data/PH59_bot_Comp.csv")
df.to_excel("PH59_data_fo_MSA.xlsx", index=False)