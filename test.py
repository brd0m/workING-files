import pandas as pd


file_a = pd.read_excel('sor.xlsx', 'SNOW CMDB DBNL')
file_b = pd.read_excel('cmdb.xlsx', 'Page 1')


names_a = set(file_a['Name'])
names_b = set(file_b['Name'])


both_files = names_a.union(names_b)


#output_data = pd.DataFrame({'Name': list(both_files), 'Present': ''})

output_rows = []


print(len(file_a))


for name in both_files:
    present = ''
    a_row = {}
    b_row = {}
  
    
    if name in names_a and name in names_b:
        present = 'BOTH'
        a_row = file_a[file_a['Name'] == name].iloc[0,1:].to_dict()
        b_row = file_b[file_b['Name'] == name].iloc[0,1:].to_dict()
    elif name in names_a:
        present = 'SoR'
        a_row = file_a[file_a['Name'] == name].iloc[0,1:].to_dict()
    elif name in names_b:
        present = 'CMDB'
        b_row = file_b[file_b['Name'] == name].iloc[0,1:].to_dict()
    
    output_row = {'Name':name, 'Present':present}
    output_row.update(a_row)
    output_row.update(b_row)
    output_rows.append(output_row)
    
output_data = pd.DataFrame(output_rows)
output_data.to_excel('newoutput.xlsx',index=False)


sor = output_data['System of Record'].value_counts(dropna=False)
presence = output_data['Present'].value_counts(dropna=False)

print(sor, presence)

print("Finish")
