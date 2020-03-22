#%%
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

base_dir = 'C:/Users/A/Desktop'
excel_file = '안전지수.xlsx'

excel_dir = os.path.join(base_dir,excel_file)


excel_duplicated_file = '안전지수_중복값_제거.xlsx'
excel_duplicated_dir = os.path.join(base_dir,excel_duplicated_file) 

# safe_score1 = pd.read_excel(excel_dir, sheet_name='Sheet1', usecols='A,F')
# safe_score2 = pd.read_excel(excel_dir, sheet_name='Sheet2', usecols='A,F')
# safe_score3 = pd.read_excel(excel_dir, sheet_name='Sheet3', usecols='A,F')

safe_score_not_duplicated = pd.read_excel(excel_duplicated_dir, sheet_name='Sheet1',usecols ='A,F')


#print(safe_score1.head(),safe_score2.head(),safe_score3.head())


# safe_score = pd.concat([safe_score1,safe_score2])
# safe_score = pd.concat([safe_score,safe_score3])

#safe_score의 정규화를 위해서 표준편차와 평균 계산
# safe_score_mean = safe_score['안전지수'].mean()
# safe_score_std = safe_score['안전지수'].std()


#safe_score에서 0은 위험단계이므로 0을 제외한 수 필터
# safe_score_only_Zero = safe_score['안전지수'].isin([0])
# safe_score_except_Zero = safe_score[~safe_score_only_Zero]

print("Safe Score Max: ",max(safe_score_not_duplicated['안전지수']))

print("Safe Score Min: ",min(safe_score_not_duplicated['안전지수']))
print("Safe Score 1사분위 수: ")
print('%.17f'% np.percentile(safe_score_not_duplicated['안전지수'],25))
print("Safe Score 2사분위 수: ")
print('%.17f'% np.percentile(safe_score_not_duplicated['안전지수'],50))
print("Safe Score 3사분위 수: ")
print('%.17f'% np.percentile(safe_score_not_duplicated['안전지수'],75))

#print('%.10f'% safe_score_except_Zero['안전지수'].describe())
# #safe_score_arr = safe_score['안전지수'].values
# #for i in range(len(safe_score_arr)):
# #    safe_score_arr[i] -= safe_score_mean

# safe_score1['안전지수'] -= safe_score_mean
# safe_score1['안전지수'] /= safe_score_std
# safe_score2['안전지수'] -= safe_score_mean
# safe_score2['안전지수'] /= safe_score_std
# safe_score3['안전지수'] -= safe_score_mean
# safe_score3['안전지수'] /= safe_score_std





#safe_score.plot(x = 'id', y = '안전지수')


#plt.xlim(0,100000)
#plt.ylim(0,0.5)
#plt.show()

