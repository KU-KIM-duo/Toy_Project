import pymysql
import pandas as pd

# 데이터베이스 연결
sql_connect = pymysql.Connect(
    host = '129.154.62.175',#'129.154.62.175',
    user = 'streamlit',#'streamlit',
    password = 'bigdata1!',#'bigdata1!',
    db = 'streamlit_db',#db 이름 입력,
    charset = 'utf8mb4'
)

# cursor 생성(통로 역할)
cursor = sql_connect.cursor()

# 크롤링한 데이터 op_gg테이블에 넣어줌
slq = 'select * from your_gg'
    
cursor.execute(slq)

# fetchall함수는 테이블에있는 모든 데이터를 가지고옴 
load_data = cursor.fetchall()

sql_connect.close()

col_mean = pd.DataFrame(load_data)

# 각 티어별별로 데이터 분리
iron_col = col_mean[(col_mean[26] == 'Iron 1')+(col_mean[26] == 'Iron 2')+(col_mean[26] == 'Iron 3')+(col_mean[26] == 'Iron 4')]
bronze_col = col_mean[(col_mean[26] == 'Bronze 1')+(col_mean[26] == 'Bronze 2')+(col_mean[26] == 'Bronze 3')+(col_mean[26] == 'Bronze 4')]
silver_col = col_mean[(col_mean[26] == 'Silver 1')+(col_mean[26] == 'Silver 2')+(col_mean[26] == 'Silver 3')+(col_mean[26] == 'Silver 4')]
gold_col = col_mean[(col_mean[26] == 'Gold 1')+(col_mean[26] == 'Gold 2')+(col_mean[26] == 'Gold 3')+(col_mean[26] == 'Gold 4')]
platinum_col = col_mean[(col_mean[26] == 'Platinum 1')+(col_mean[26] == 'Platinum 2')+(col_mean[26] == 'Platinum 3')+(col_mean[26] == 'Platinum 4')]
diamond_col = col_mean[(col_mean[26] == 'Diamond 1')+(col_mean[26] == 'Diamond 2')+(col_mean[26] == 'Diamond 3')+(col_mean[26] == 'Diamond 4')]
master_col = col_mean[(col_mean[26] == 'Master')]
grandmaster_col = col_mean[(col_mean[26] == 'Grandmaster')]
challenger_col = col_mean[(col_mean[26] == 'Challenger')]

# 아이언 티어 열별 데이터의 평균값 및 최빈값
iron_col1 = pd.DataFrame([iron_col.loc[:,4:6].astype(float).mean()])
iron_col2 = pd.DataFrame([iron_col.loc[:,7].mode()[0]])
iron_col3 = pd.DataFrame([iron_col.loc[:,8].mode()[0]])
iron_col4 = pd.DataFrame([iron_col.loc[:,9:11].astype(float).mean()])
iron_col5 = pd.DataFrame([round(iron_col.loc[:,12].str.replace(pat=',', repl='').astype(float).mean())])
iron_col6 = pd.DataFrame([iron_col.loc[:,13:18].astype(float).mean()])
iron_col7 = pd.DataFrame([iron_col.loc[:,19].mode()[0]])
iron_col8 = pd.DataFrame([iron_col.loc[:,20].mode()[0]])
iron_col9 = pd.DataFrame([iron_col.loc[:,21].mode()[0]])
iron_col10 = pd.DataFrame([str(round(iron_col.loc[:,22].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
iron_col11 = pd.DataFrame([str(round(iron_col.loc[:,23].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
iron_col12 = pd.DataFrame([iron_col.loc[:,24:25].astype(float).mean()])
iron_col_mean = pd.concat([iron_col1,iron_col2,iron_col3,iron_col4,iron_col5,iron_col6,iron_col7,iron_col8,iron_col9,
                                  iron_col10,iron_col11,iron_col12], axis = 1)
iron_col_mean.columns = ['4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']

# 브론즈 티어 열별 데이터의 평균값 및 최빈값
bronze_col1 = pd.DataFrame([bronze_col.loc[:,4:6].astype(float).mean()])
bronze_col2 = pd.DataFrame([bronze_col.loc[:,7].mode()[0]])
bronze_col3 = pd.DataFrame([bronze_col.loc[:,8].mode()[0]])
bronze_col4 = pd.DataFrame([bronze_col.loc[:,9:11].astype(float).mean()])
bronze_col5 = pd.DataFrame([round(bronze_col.loc[:,12].str.replace(pat=',', repl='').astype(float).mean())])
bronze_col6 = pd.DataFrame([bronze_col.loc[:,13:18].astype(float).mean()])
bronze_col7 = pd.DataFrame([bronze_col.loc[:,19].mode()[0]])
bronze_col8 = pd.DataFrame([bronze_col.loc[:,20].mode()[0]])
bronze_col9 = pd.DataFrame([bronze_col.loc[:,21].mode()[0]])
bronze_col10 = pd.DataFrame([str(round(bronze_col.loc[:,22].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
bronze_col11 = pd.DataFrame([str(round(bronze_col.loc[:,23].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
bronze_col12 = pd.DataFrame([bronze_col.loc[:,24:25].astype(float).mean()])
bronze_col_mean = pd.concat([bronze_col1,bronze_col2,bronze_col3,bronze_col4,bronze_col5,bronze_col6,bronze_col7,bronze_col8,bronze_col9,
                                  bronze_col10,bronze_col11,bronze_col12], axis = 1)
bronze_col_mean.columns = ['4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']

# 실버 티어 열별 데이터의 평균값 및 최빈값
silver_col1 = pd.DataFrame([silver_col.loc[:,4:6].astype(float).mean()])
silver_col2 = pd.DataFrame([silver_col.loc[:,7].mode()[0]])
silver_col3 = pd.DataFrame([silver_col.loc[:,8].mode()[0]])
silver_col4 = pd.DataFrame([silver_col.loc[:,9:11].astype(float).mean()])
silver_col5 = pd.DataFrame([round(silver_col.loc[:,12].str.replace(pat=',', repl='').astype(float).mean())])
silver_col6 = pd.DataFrame([silver_col.loc[:,13:18].astype(float).mean()])
silver_col7 = pd.DataFrame([silver_col.loc[:,19].mode()[0]])
silver_col8 = pd.DataFrame([silver_col.loc[:,20].mode()[0]])
silver_col9 = pd.DataFrame([silver_col.loc[:,21].mode()[0]])
silver_col10 = pd.DataFrame([str(round(silver_col.loc[:,22].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
silver_col11 = pd.DataFrame([str(round(silver_col.loc[:,23].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
silver_col12 = pd.DataFrame([silver_col.loc[:,24:25].astype(float).mean()])
silver_col_mean = pd.concat([silver_col1,silver_col2,silver_col3,silver_col4,silver_col5,silver_col6,silver_col7,silver_col8,silver_col9,
                                  silver_col10,silver_col11,silver_col12], axis = 1)
silver_col_mean.columns = ['4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']

# 골드 티어 열별 데이터의 평균값 및 최빈값
gold_col1 = pd.DataFrame([gold_col.loc[:,4:6].astype(float).mean()])
gold_col2 = pd.DataFrame([gold_col.loc[:,7].mode()[0]])
gold_col3 = pd.DataFrame([gold_col.loc[:,8].mode()[0]])
gold_col4 = pd.DataFrame([gold_col.loc[:,9:11].astype(float).mean()])
gold_col5 = pd.DataFrame([round(gold_col.loc[:,12].str.replace(pat=',', repl='').astype(float).mean())])
gold_col6 = pd.DataFrame([gold_col.loc[:,13:18].astype(float).mean()])
gold_col7 = pd.DataFrame([gold_col.loc[:,19].mode()[0]])
gold_col8 = pd.DataFrame([gold_col.loc[:,20].mode()[0]])
gold_col9 = pd.DataFrame([gold_col.loc[:,21].mode()[0]])
gold_col10 = pd.DataFrame([str(round(gold_col.loc[:,22].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
gold_col11 = pd.DataFrame([str(round(gold_col.loc[:,23].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
gold_col12 = pd.DataFrame([gold_col.loc[:,24:25].astype(float).mean()])
gold_col_mean = pd.concat([gold_col1,gold_col2,gold_col3,gold_col4,gold_col5,gold_col6,gold_col7,gold_col8,gold_col9,
                                  gold_col10,gold_col11,gold_col12], axis = 1)
gold_col_mean.columns = ['4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']

# 플래티넘 티어 열별 데이터의 평균값 및 최빈값
platinum_col1 = pd.DataFrame([platinum_col.loc[:,4:6].astype(float).mean()])
platinum_col2 = pd.DataFrame([platinum_col.loc[:,7].mode()[0]])
platinum_col3 = pd.DataFrame([platinum_col.loc[:,8].mode()[0]])
platinum_col4 = pd.DataFrame([platinum_col.loc[:,9:11].astype(float).mean()])
platinum_col5 = pd.DataFrame([round(platinum_col.loc[:,12].str.replace(pat=',', repl='').astype(float).mean())])
platinum_col6 = pd.DataFrame([platinum_col.loc[:,13:18].astype(float).mean()])
platinum_col7 = pd.DataFrame([platinum_col.loc[:,19].mode()[0]])
platinum_col8 = pd.DataFrame([platinum_col.loc[:,20].mode()[0]])
platinum_col9 = pd.DataFrame([platinum_col.loc[:,21].mode()[0]])
platinum_col10 = pd.DataFrame([str(round(platinum_col.loc[:,22].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
platinum_col11 = pd.DataFrame([str(round(platinum_col.loc[:,23].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
platinum_col12 = pd.DataFrame([platinum_col.loc[:,24:25].astype(float).mean()])
platinum_col_mean = pd.concat([platinum_col1,platinum_col2,platinum_col3,platinum_col4,platinum_col5,platinum_col6,platinum_col7,platinum_col8,platinum_col9,
                                  platinum_col10,platinum_col11,platinum_col12], axis = 1)
platinum_col_mean.columns = ['4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']

# 다이아몬드 티어 열별 데이터의 평균값 및 최빈값
diamond_col1 = pd.DataFrame([diamond_col.loc[:,4:6].astype(float).mean()])
diamond_col2 = pd.DataFrame([diamond_col.loc[:,7].mode()[0]])
diamond_col3 = pd.DataFrame([diamond_col.loc[:,8].mode()[0]])
diamond_col4 = pd.DataFrame([diamond_col.loc[:,9:11].astype(float).mean()])
diamond_col5 = pd.DataFrame([round(diamond_col.loc[:,12].str.replace(pat=',', repl='').astype(float).mean())])
diamond_col6 = pd.DataFrame([diamond_col.loc[:,13:18].astype(float).mean()])
diamond_col7 = pd.DataFrame([diamond_col.loc[:,19].mode()[0]])
diamond_col8 = pd.DataFrame([diamond_col.loc[:,20].mode()[0]])
diamond_col9 = pd.DataFrame([diamond_col.loc[:,21].mode()[0]])
diamond_col10 = pd.DataFrame([str(round(diamond_col.loc[:,22].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
diamond_col11 = pd.DataFrame([str(round(diamond_col.loc[:,23].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
diamond_col12 = pd.DataFrame([diamond_col.loc[:,24:25].astype(float).mean()])
diamond_col_mean = pd.concat([diamond_col1,diamond_col2,diamond_col3,diamond_col4,diamond_col5,diamond_col6,diamond_col7,diamond_col8,diamond_col9,
                                  diamond_col10,diamond_col11,diamond_col12], axis = 1)
diamond_col_mean.columns = ['4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']

# 마스터 티어 열별 데이터의 평균값 및 최빈값
master_col1 = pd.DataFrame([master_col.loc[:,4:6].astype(float).mean()])
master_col2 = pd.DataFrame([master_col.loc[:,7].mode()[0]])
master_col3 = pd.DataFrame([master_col.loc[:,8].mode()[0]])
master_col4 = pd.DataFrame([master_col.loc[:,9:11].astype(float).mean()])
master_col5 = pd.DataFrame([round(master_col.loc[:,12].str.replace(pat=',', repl='').astype(float).mean())])
master_col6 = pd.DataFrame([master_col.loc[:,13:18].astype(float).mean()])
master_col7 = pd.DataFrame([master_col.loc[:,19].mode()[0]])
master_col8 = pd.DataFrame([master_col.loc[:,20].mode()[0]])
master_col9 = pd.DataFrame([master_col.loc[:,21].mode()[0]])
master_col10 = pd.DataFrame([str(round(master_col.loc[:,22].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
master_col11 = pd.DataFrame([str(round(master_col.loc[:,23].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
master_col12 = pd.DataFrame([master_col.loc[:,24:25].astype(float).mean()])
master_col_mean = pd.concat([master_col1,master_col2,master_col3,master_col4,master_col5,master_col6,master_col7,master_col8,master_col9,
                                  master_col10,master_col11,master_col12], axis = 1)
master_col_mean.columns = ['4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']

# 그랜드마스터 티어 열별 데이터의 평균값 및 최빈값
grandmaster_col1 = pd.DataFrame([grandmaster_col.loc[:,4:6].astype(float).mean()])
grandmaster_col2 = pd.DataFrame([grandmaster_col.loc[:,7].mode()[0]])
grandmaster_col3 = pd.DataFrame([grandmaster_col.loc[:,8].mode()[0]])
grandmaster_col4 = pd.DataFrame([grandmaster_col.loc[:,9:11].astype(float).mean()])
grandmaster_col5 = pd.DataFrame([round(grandmaster_col.loc[:,12].str.replace(pat=',', repl='').astype(float).mean())])
grandmaster_col6 = pd.DataFrame([grandmaster_col.loc[:,13:18].astype(float).mean()])
grandmaster_col7 = pd.DataFrame([grandmaster_col.loc[:,19].mode()[0]])
grandmaster_col8 = pd.DataFrame([grandmaster_col.loc[:,20].mode()[0]])
grandmaster_col9 = pd.DataFrame([grandmaster_col.loc[:,21].mode()[0]])
grandmaster_col10 = pd.DataFrame([str(round(grandmaster_col.loc[:,22].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
grandmaster_col11 = pd.DataFrame([str(round(grandmaster_col.loc[:,23].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
grandmaster_col12 = pd.DataFrame([grandmaster_col.loc[:,24:25].astype(float).mean()])
grandmaster_col_mean = pd.concat([grandmaster_col1,grandmaster_col2,grandmaster_col3,grandmaster_col4,grandmaster_col5,grandmaster_col6,grandmaster_col7,grandmaster_col8,grandmaster_col9,
                                  grandmaster_col10,grandmaster_col11,grandmaster_col12], axis = 1)
grandmaster_col_mean.columns = ['4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']

# 챌린저 티어 열별 데이터의 평균값 및 최빈값
challenger_col1 = pd.DataFrame([challenger_col.loc[:,4:6].astype(float).mean()])
challenger_col2 = pd.DataFrame([challenger_col.loc[:,7].mode()[0]])
challenger_col3 = pd.DataFrame([challenger_col.loc[:,8].mode()[0]])
challenger_col4 = pd.DataFrame([challenger_col.loc[:,9:11].astype(float).mean()])
challenger_col5 = pd.DataFrame([round(challenger_col.loc[:,12].str.replace(pat=',', repl='').astype(float).mean())])
challenger_col6 = pd.DataFrame([challenger_col.loc[:,13:18].astype(float).mean()])
challenger_col7 = pd.DataFrame([challenger_col.loc[:,19].mode()[0]])
challenger_col8 = pd.DataFrame([challenger_col.loc[:,20].mode()[0]])
challenger_col9 = pd.DataFrame([challenger_col.loc[:,21].mode()[0]])
challenger_col10 = pd.DataFrame([str(round(challenger_col.loc[:,22].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
challenger_col11 = pd.DataFrame([str(round(challenger_col.loc[:,23].str.replace(pat='%', repl='').astype(float).mean())) + '%'])
challenger_col12 = pd.DataFrame([challenger_col.loc[:,24:25].astype(float).mean()])
challenger_col_mean = pd.concat([challenger_col1,challenger_col2,challenger_col3,challenger_col4,challenger_col5,challenger_col6,challenger_col7,challenger_col8,challenger_col9,
                                  challenger_col10,challenger_col11,challenger_col12], axis = 1)
challenger_col_mean.columns = ['4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']

# 티어별 데이터프레임 병합 및 인덱스명 변경
tier_mean = pd.concat([iron_col_mean,bronze_col_mean,silver_col_mean,gold_col_mean,platinum_col_mean,diamond_col_mean,master_col_mean,grandmaster_col_mean,challenger_col_mean], axis = 0)
tier_mean.index= ['iron','bronze','silver','gold','platinum','diamond','master','grandmaster','challenger']

# 최종 데이터프레임 저장
tier_mean.to_csv('preprocessing1.csv')


