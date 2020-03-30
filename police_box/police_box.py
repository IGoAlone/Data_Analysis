import pandas as pd
import openpyxl
import os 

base_dir = '/Users/woneyhoney/Desktop/weight/Again'
excel_file1 = '지구대거리.xlsx'
excel_file2 = '지구대면적.xlsx'

excel_dir = os.path.join(base_dir, excel_file1)
df1 = pd.read_excel(excel_dir, sheet_name='Sheet1', usecols='A, D')

excel_dir = os.path.join(base_dir, excel_file2)
df2 = pd.read_excel(excel_dir, sheet_name='Sheet1', usecols='D, F')

df = pd.merge(df1, df2) # df1, df2의 공통 column 이름인 id를 기준으로 inner join
# print(df.head())

pb_weight = df['police_distance'] * df['police_area']

arr_id = df['id'].values
col_dup = df['id'].duplicated(keep=False)  # 중복, 미중복 구분

try:
    for i in range(len(pb_weight)):
        if col_dup[i] == True:  # 중복
            if arr_id[i] == arr_id[i + 1]:    # 동일 InputID
                pb_weight[i + 1] += pb_weight[i]
                pb_weight[i] = 0
except IndexError:
    pass

df['pb_weight'] = pb_weight
for i in range(len(pb_weight)):
    if pb_weight[i] == 0:
        df = df.drop(index=i)

writer = pd.ExcelWriter('pb_weight_unduplicated.xlsx')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
