from sklearn_extra.cluster import KMedoids
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
import os 

base_dir = 'C:/Users/A/Desktop/I_Go_Alone/Data_Analysis/clustering'
excel_file = 'safety_level_2.xlsx'
excel_dir = os.path.join(base_dir,excel_file)

df = pd.read_excel(excel_dir, sheet_name='Sheet1', usecols='C, D') # id, x_latitude, y_longititude, safety_level
# arr_x = df['x_latitude'].values
# arr_y = df['y_longitude'].values
# np.reshape(arr_x,arr_y)
data_points_x = df['x_latitude'].values.reshape(-1, 1)
data_points_y = df['y_longitude'].values.reshape(-1, 1)
data_points = np.hstack((data_points_x,data_points_y))
kmedoids = KMeans(n_clusters=150, random_state=0).fit(data_points)
df['cluster_id'] = kmeans.labels_

writer = pd.ExcelWriter('안전지수_클러스터(k=50).xlsx')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()

