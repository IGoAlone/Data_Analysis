#%%
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

base_dir = 'C:/Users/A/Desktop'
excel_file = '안전지수.xlsx'
output_file = 'result.xlsx'
excel_dir = os.path.join(base_dir,excel_file)
output_dir = os.path.join(base_dir,output_file)

excel_duplicated_file = '안전지수_중복값_제거.xlsx'
excel_duplicated_dir = os.path.join(base_dir,excel_duplicated_file) 

safe_score1 = pd.read_excel(excel_dir, sheet_name='Sheet1', usecols='A,F')
safe_score2 = pd.read_excel(excel_dir, sheet_name='Sheet2', usecols='A,F')
safe_score3 = pd.read_excel(excel_dir, sheet_name='Sheet3', usecols='A,F')

safe_score_not_duplicated = pd.read_excel(excel_duplicated_dir, sheet_name='Sheet1',usecols ='A,F')


#print(safe_score1.head(),safe_score2.head(),safe_score3.head())


safe_score = pd.concat([safe_score1,safe_score2])
safe_score = pd.concat([safe_score,safe_score3])



#safe_score에서 0은 위험단계이므로 0을 제외한 수 필터
# safe_score_only_Zero = safe_score['안전지수'].isin([0])
# safe_score_except_Zero = safe_score[~safe_score_only_Zero]

print("Safe Score Max: ",max(safe_score['안전지수']))

print("Safe Score Min: ",min(safe_score_not_duplicated['안전지수']))
print("Safe Score 1사분위 수: ")
print('%.17f'% np.percentile(safe_score_not_duplicated['안전지수'],25))
print("Safe Score 2사분위 수: ")
print('%.17f'% np.percentile(safe_score_not_duplicated['안전지수'],50))
print("Safe Score 3사분위 수: ")
print('%.17f'% np.percentile(safe_score_not_duplicated['안전지수'],75))

first_grade = np.percentile(safe_score_not_duplicated['안전지수'],25)
second_grade = np.percentile(safe_score_not_duplicated['안전지수'],50)
third_grade = np.percentile(safe_score_not_duplicated['안전지수'],75)
max_score = max(safe_score['안전지수'])


#데이터 등급 나누기
safe_score1['안전등급'] = safe_score1['안전지수'].apply(lambda x: 0 if x < first_grade else
         1 if x >= first_grade and x < second_grade else 
         2 if x >= second_grade and x < third_grade else 3)

safe_score2['안전등급'] = safe_score2['안전지수'].apply(lambda x: 0 if x < first_grade else
         1 if x >= first_grade and x < second_grade else 
         2 if x >= second_grade and x < third_grade else 3)

safe_score3['안전등급'] = safe_score3['안전지수'].apply(lambda x: 0 if x < first_grade else
         1 if x >= first_grade and x < second_grade else 
         2 if x >= second_grade and x < third_grade else 3)





#안전등급 결과가 추가된 excel 저장

with pd.ExcelWriter(output_dir) as writer:
    safe_score1.to_excel(writer,sheet_name = 'Sheet1')
    safe_score2.to_excel(writer,sheet_name = 'Sheet2')
    safe_score3.to_excel(writer,sheet_name = 'Sheet3')

#safe_score.plot(x = 'id', y = '안전지수')


#plt.xlim(0,100000)
#plt.ylim(0,0.5)
#plt.show()