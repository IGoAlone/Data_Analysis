import pandas as pd 
import numpy as np 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
import os 

base_dir = '/Users/woneyhoney/Desktop/weight/Again/Data_Analysis'
excel_file = '안전지수_.xlsx'
excel_dir = os.path.join(base_dir,excel_file)

df1 = pd.read_excel(excel_dir, sheet_name='Sheet1', usecols='A, B') # id, safe_score
df2 = pd.read_excel(excel_dir, sheet_name='Sheet2', usecols='A, B')
df3 = pd.read_excel(excel_dir, sheet_name='Sheet3', usecols='A, B')

# safe_score = 0 제거 
df1 = df1[df1.safe_score != 0]
df2 = df2[df2.safe_score != 0]
df3 = df3[df3.safe_score != 0]

df = pd.concat([df1, df2])
df = pd.concat([df, df3])

data_points = df['safe_score'].values.reshape(-1, 1) 

kmeans = KMeans(n_clusters=4).fit(data_points) # 4개의 클러스터
df['cluster_id'] = kmeans.labels_

writer = pd.ExcelWriter('안전지수_클러스터(k=4).xlsx')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()