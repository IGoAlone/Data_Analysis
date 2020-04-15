from sklearn_extra.cluster import KMedoids
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
import os 

import numbers
import math

class GeoUtil:
    """
    Geographical Utils
    """
    @staticmethod
    def degree2radius(degree):
        return degree * (math.pi/180)
    
    @staticmethod
    def get_harversion_distance(x1, y1, x2, y2, round_decimal_digits=5):
        """
        경위도 (x1,y1)과 (x2,y2) 점의 거리를 반환
        Harversion Formula 이용하여 2개의 경위도간 거래를 구함(단위:Km)
        """
        if x1 is None or y1 is None or x2 is None or y2 is None:
            return None
        assert isinstance(x1, numbers.Number) and -180 <= x1 and x1 <= 180
        assert isinstance(y1, numbers.Number) and  -90 <= y1 and y1 <=  90
        assert isinstance(x2, numbers.Number) and -180 <= x2 and x2 <= 180
        assert isinstance(y2, numbers.Number) and  -90 <= y2 and y2 <=  90

        R = 6371 # 지구의 반경(단위: km)
        dLon = GeoUtil.degree2radius(x2-x1)    
        dLat = GeoUtil.degree2radius(y2-y1)

        a = math.sin(dLat/2) * math.sin(dLat/2) \
            + (math.cos(GeoUtil.degree2radius(y1)) \
              *math.cos(GeoUtil.degree2radius(y2)) \
              *math.sin(dLon/2) * math.sin(dLon/2))
        b = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return round(R * b, round_decimal_digits)

    @staticmethod
    def get_euclidean_distance(x1, y1, x2, y2, round_decimal_digits=5):        
        """
        유클리안 Formula 이용하여 (x1,y1)과 (x2,y2) 점의 거리를 반환
        """
        if x1 is None or y1 is None or x2 is None or y2 is None:
            return None
        assert isinstance(x1, numbers.Number) and -180 <= x1 and x1 <= 180
        assert isinstance(y1, numbers.Number) and  -90 <= y1 and y1 <=  90
        assert isinstance(x2, numbers.Number) and -180 <= x2 and x2 <= 180
        assert isinstance(y2, numbers.Number) and  -90 <= y2 and y2 <=  90

        dLon = abs(x2-x1) # 경도 차이
        if dLon >= 180:   # 반대편으로 갈 수 있는 경우
            dLon -= 360   # 반대편 각을 구한다
        dLat = y2-y1      # 위도 차이
        return round(math.sqrt(pow(dLon,2)+pow(dLat,2)),round_decimal_digits)


base_dir = 'C:/Users/A/Desktop/I_Go_Alone/Data_Analysis/clustering'
excel_file = '안전지수_클러스터(k=50).xlsx'
excel_dir = os.path.join(base_dir,excel_file)

df = pd.read_excel(excel_dir, sheet_name='Sheet1', usecols='B,C, D') # x_latitude, y_longititude, cluster_id


cluster = [0 for i in range(0,50)]
max_index1 = [0 for i in range(0,50)]
max_index2 = [0 for i in range(0,50)] #first id, second id

for i in range(0,50) :
    cluster[i] = df[df.cluster_id == i].to_numpy()

# print(cluster[0].head)
# print(cluster[1].head)
# print(cluster[2].head)
x_maxvalue = -1
y_maxvalue = -1
 
for i in range(0,50) :
    for index in range(len(cluster[i])) :
        for k in range(index+1,len(cluster[i])) : #index 다음부터 탐색할 수 있도록 
            if(abs(cluster[i][index][0]-cluster[i][k][0]) > x_maxvalue and abs(cluster[i][index][1]-cluster[i][k][1]) > y_maxvalue) :
                x_maxvalue = abs(cluster[i][index][0]-cluster[i][k][0])
                y_maxvalue = abs(cluster[i][index][1]-cluster[i][k][1])
                max1 = index
                max2 = k
    max_index1[i] = max1
    max_index2[i] = max2
    #print(i,max_index1[i],max_index2[i])
    x_maxvalue = -1
    y_maxvalue = -1
max_distance = np.column_stack([max_index1,max_index2])
#print(max_distance[0][0])
distance = [0 for i in range(0,50)]
center_x = [0 for i in range(0,50)]
center_y = [0 for i in range(0,50)]
for i in range(len(cluster)) :
    distance[i]=GeoUtil.get_harversion_distance(cluster[i][max_distance[i][0]][0],cluster[i][max_distance[i][0]][1],cluster[i][max_distance[i][1]][0],cluster[i][max_distance[i][1]][1])
    center_x[i] = (cluster[i][max_distance[i][0]][0] + cluster[i][max_distance[i][1]][0])/2
    center_y[i] = (cluster[i][max_distance[i][0]][1] + cluster[i][max_distance[i][1]][1])/2

safe_level2_clustering = np.column_stack([center_x,center_y])
safe_level2_clustering = np.column_stack([safe_level2_clustering,distance])

df = pd.DataFrame(safe_level2_clustering)
writer = pd.ExcelWriter('safe_level2_distance.xlsx')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
