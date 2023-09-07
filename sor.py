import pandas as pd


file_a = pd.read_excel('output.xlsx', 'Sheet1')
file_b = pd.read_excel('output2.xlsx', 'Sheet1')

merged_df = pd.merge(file_a,file_b[['Name','System of Record']], on='Name', how='left')


merged_df.to_excel('output3.xlsx',index=False)


print("Finish")
