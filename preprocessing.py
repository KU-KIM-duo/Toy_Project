
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from pickle import load
import re

class pre:
    def __init__(self, data):
        self.colum =['user_id','last_season_tier','main_position','num_games','servings','kda','line_war','carry_power','team_luck','per_minute_cs','per_minute_gold',
                               'dif_15min_cs','dif_15min_gold','dif_15min_level','total_kill','assist','death','solo_kill','allow_solo_kill','per_minute_deal','gold_deal','per_death_deal','kill_engage_15min'
                               ,'kill_engage','vision_score','control_ward','current_season_tier']
        self.col =['last_season_tier','num_games','servings','kda','line_war','carry_power','team_luck','per_minute_cs','per_minute_gold','dif_15min_cs',
                          'dif_15min_gold','dif_15min_level','total_kill','assist','death','solo_kill','allow_solo_kill','per_minute_deal','gold_deal','per_death_deal',
                          'kill_engage_15min','kill_engage','vision_score','control_ward',]
        self.df =  pd.DataFrame(columns = self.colum)
        self.df.loc[0] = data
        
        
        self.df['kill_engage_15min'] = self.df['kill_engage_15min'][0].replace('%','')
        self.df['kill_engage'] = self.df['kill_engage'][0].replace('%','')
        
    
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
            elif tier == 'unranked':
                return 0
            
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
        scaler = load(open('standardscaler.pkl','rb'))
        self.df[self.col] = scaler.transform(self.df[self.col])
    def data(self):
        return self.df

