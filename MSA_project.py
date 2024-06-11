import pandas as pd

def read_data(path):
    
    df = pd.read_csv(path)
    return df

#take path to the data
path_top = "C:\\Users\\K90006169\\MSA_project\\PH71_top_Comp.csv" 
path_bot = "C:\\Users\\K90006169\\MSA_project\\PH71_bot_Comp.csv"

#read the data
df_top = pd.read_csv(path_top)
df_bot = pd.read_csv(path_bot)

#define variables
df_columns = ["OffsetX", "OffsetY"]
modules = 5
components_top = ["R201", "R205"]
components_bot = ["R303", "R510"]
columns_for_msa_data = {
    'Operator': [1 for i in range(45)],
    'Part': [i+1 for i in range(5) for j in range(9)]
}
msa_data = pd.DataFrame(columns_for_msa_data)

for i in components_top:
    #create a temporary dataframe
    filtered_data = pd.DataFrame(columns=df_columns)

    for j in range(modules):
        #create filter
        filt = (df_top["ModuleID"] == j + 1) & (df_top["Location Name"] == i)
        #filtered data from the .csv file and add it to the temporary dataframe
        filtered_data = pd.concat([filtered_data, df_top.loc[filt, df_columns].iloc[:9]], ignore_index=True)

    column_mapping = {
        df_columns[0]: f"TOP_{i}_X",
        df_columns[1]: f"TOP_{i}_Y"
    }
    #rename the columns and update the values of the temporary dataframe
    filtered_data = filtered_data.rename(columns=column_mapping).apply(lambda x: x/1000)
    #concatenate the MSA dataframe and the temporary dataframe with renaming columns of the temporary dataframe
    msa_data = pd.concat([msa_data, filtered_data], axis=1)

for i in components_bot:
    #create a temporary dataframe
    filtered_data = pd.DataFrame(columns=df_columns)

    for j in range(modules):
        #create filter
        filt = (df_bot["ModuleID"] == j + 1) & (df_bot["Location Name"] == i)
        #filtered data from the .csv file and add it to the temporary dataframe
        filtered_data = pd.concat([filtered_data, df_bot.loc[filt, df_columns].iloc[:9]], ignore_index=True)

    column_mapping = {
        df_columns[0]: f"BOT_{i}_X",
        df_columns[1]: f"BOT_{i}_Y"
    }
    #rename the columns and update the values of the temporary dataframe
    filtered_data = filtered_data.rename(columns=column_mapping).apply(lambda x: x/1000)
    #concatenate the MSA dataframe and the temporary dataframe
    msa_data = pd.concat([msa_data, filtered_data], axis=1)

#create a dataframe for measurement tolerance
components = components_top + components_bot
n = len(components)
columns_with_data = {
    'Desygnator': components,
    'Obudowa': ['none' for i in range(n)],
    'Tolerancja X': [0 for i in range(n)],
    'Tolerancja Y': [0 for i in range(n)]
}
tolerance_data = pd.DataFrame(columns_with_data)

#export MSA and tolerance dataframes to the Excel
with pd.ExcelWriter('MSA_data.xlsx', engine='xlsxwriter') as writer:
    msa_data.to_excel(writer, sheet_name='Sheet1', startrow=0, startcol=0, index=False)
    tolerance_data.to_excel(writer, sheet_name='Sheet1', startrow=0, startcol=len(msa_data.columns) + 2, index=False)
