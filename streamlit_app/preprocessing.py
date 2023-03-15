
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from pickle import load
import re

# 데이터 전처리 코드
class pre:
    def __init__(self, data):
        # colum은 전체 컬럼
        self.colum =['user_id','last_season_tier','main_position','num_games','servings','kda','line_war','carry_power',
                     'team_luck','per_minute_cs','per_minute_gold','dif_15min_cs','dif_15min_gold','dif_15min_level',
                     'total_kill','assist','death','solo_kill','allow_solo_kill','per_minute_deal','gold_deal','per_death_deal',
                     'kill_engage_15min','kill_engage','vision_score','control_ward','current_season_tier']
        # col은 숫자형 컬럼들
        self.col =['last_season_tier','num_games','servings','kda','line_war','carry_power','team_luck','per_minute_cs',
                   'per_minute_gold','dif_15min_cs','dif_15min_gold','dif_15min_level','total_kill','assist','death',
                   'solo_kill','allow_solo_kill','per_minute_deal','gold_deal','per_death_deal',
                   'kill_engage_15min','kill_engage','vision_score','control_ward',]
        self.df =  pd.DataFrame(columns = self.colum)
        self.df.loc[0] = data
        
        # 데이터에 안에있는 '%'기호 삭제
        self.df['kill_engage_15min'] = self.df['kill_engage_15min'][0].replace('%','')
        self.df['kill_engage'] = self.df['kill_engage'][0].replace('%','')
        
        # 티어를 숫자로 변환
        def tier_label(d):
            tier = re.sub('[^a-zA-z]','',d)
            try:
                num = 5 - int(re.sub('\D','', d))
            except ValueError:
                num = 5
                
            if tier == 'Iron':
                return num
            elif tier == 'Bronze':
                return 4 + num
            elif tier == 'Silver':
                return 8 + num
            elif tier == 'Gold':
                return 12 + num
            elif tier == 'Platinum':
                return 16 + num
            elif tier == 'Diamond':
                return 20 + num
            elif tier == 'Master':
                return 24 + num
            elif tier == 'Grandmaster':
                return 28 + num
            elif tier == 'Challenger':
                return 32 + num
            elif tier == 'Unranked' or tier == 'unranked':
                return 0
        
        # 팀운
        def tram_luck_labeling(d):
            if d == '최고':
                return 5
            elif d == '좋음':
                return 4
            elif d == '보통':
                return 3
            elif d == '나쁨':
                return 2
            elif d == '극악':
                return 1        
        
        # 알파벳 데이터들 숫자로 변환 
        def stat_rank_label(d):
            if d == 'D':
                return 0
            elif d == 'C-':
                return 1
            elif d == 'C':
                return 2
            elif d == 'C+':
                return 3
            elif d == 'B-':
                return 4
            elif d == 'B':
                return 5
            elif d == 'B+':
                return 6
            elif d == 'A-':
                return 7
            elif d == 'A':
                return 8
            elif d == 'A+':
                return 9
            elif d == 'S':
                return 10
            elif d == 'SS':
                return 11
            elif d == 'SSS':
                return 12 
            
        self.df['last_season_tier'] = tier_label(self.df['last_season_tier'][0])
        self.df['carry_power'] = stat_rank_label(self.df['carry_power'][0])
        self.df['gold_deal'] = stat_rank_label(self.df['gold_deal'][0])
        self.df['per_death_deal'] = stat_rank_label(self.df['per_death_deal'][0])
        self.df['per_minute_deal'] = stat_rank_label(self.df['per_minute_deal'][0])
        self.df['team_luck'] = tram_luck_labeling(self.df['team_luck'][0])
        self.df['dif_15min_gold'] = self.df['dif_15min_gold'].replace(',','')
        self.df['current_season_tier'] = tier_label(self.df['current_season_tier'][0])
        self.df['main_position'] = self.df['main_position'].astype('category')
        self.df[self.col] = self.df[self.col].astype('float')
        
        # 기존 scaler 모델 불러오기
        scaler = load(open('standardscaler.pkl','rb'))
        self.df[self.col] = scaler.transform(self.df[self.col])
        
    def data(self):
        return self.df
    
class tier_mean:
    def __init__ (self):
        self.tier_mean_col = pd.read_csv('preprocessing1.csv',index_col=0).reset_index()
        self.tier_mean_col.iloc[:,1:4] = self.tier_mean_col.iloc[:,1:4].round(2)
        self.tier_mean_col.iloc[:,6:16] = self.tier_mean_col.iloc[:,6:16].round(2)
        self.tier_mean_col.iloc[:,21:23] = self.tier_mean_col.iloc[:,21:23].round(2)
        
    # user_data는 사용자의 티어 데이터, tier_mean은 티어별 평균 데이터들이 저장된 데이터프레임
    def tier_metric(self, user_data):
        # 들어온 데이터 전처리
        user_data[26] = user_data[26].split(' ')[0].lower()
        tier_graph = self.tier_mean_col[self.tier_mean_col['index'] == user_data[26]]
        
        return tier_graph
    
    # 사용자 데이터를 티어별 평균 데이터들과 UI 그래프에서 덧셈 뺄셈 할 수 있게 전처리해줌
    def tier_metric_pre(self, user_data):
        user_data = pd.DataFrame([user_data])

        user_data.loc[:,4:6] = user_data.loc[:,4:6].astype(float)
        user_data.loc[:,9:11] = user_data.loc[:,9:11].astype(float)
        user_data.loc[:,12] = user_data.loc[:,12].str.replace(pat=',', repl='').astype(float)
        user_data.loc[:,13:18] = user_data.loc[:,13:18].astype(float)
        user_data.loc[:,24:25] = user_data.loc[:,24:25].astype(float)
        
        return user_data


