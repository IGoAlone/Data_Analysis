from pyproj import Proj, transform
import pandas as pd 
import numpy as np
import openpyxl
import os 

inProj = Proj(init='epsg:5179')
outProj = Proj(init='epsg:4326')

base_dir = '/Users/woneyhoney/Desktop/weight/Again/Data_Analysis'
excel_file = '중심점좌표.xlsx'
excel_dir = os.path.join(base_dir,excel_file)

df1 = pd.read_excel(excel_dir, sheet_name='Sheet1', usecols='A, H, I') # id, xcoord, ycoord
df2 = pd.read_excel(excel_dir, sheet_name='Sheet2', usecols='A, H, I')
df3 = pd.read_excel(excel_dir, sheet_name='Sheet3', usecols='A, H, I')

# x, y 컬럼을 이용하여 EPSG:5179좌표를 EPSG:4326로 변환한 Series데이터 반환
def transform_5179_to_4326(df):
    return pd.Series(transform(inProj, outProj, df['xcoord'], df['ycoord']), index=['xcoord', 'ycoord'])

df1[['x_latitude', 'y_longitude']] = df1.apply(transform_5179_to_4326, axis=1)
df2[['x_latitude', 'y_longitude']] = df2.apply(transform_5179_to_4326, axis=1)
df3[['x_latitude', 'y_longitude']] = df3.apply(transform_5179_to_4326, axis=1)

writer = pd.ExcelWriter('중심점좌표_위경도변환.xlsx')
df1.to_excel(writer, sheet_name='Sheet1')
df2.to_excel(writer, sheet_name='Sheet2')
df3.to_excel(writer, sheet_name='Sheet3')
writer.save()