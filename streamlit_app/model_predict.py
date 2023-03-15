import joblib
from lightgbm import LGBMClassifier

class model:
    def tier(self,data):
        # 학습된 모델 불러오기
        model = joblib.load('./lol_lgbm_model.pkl')
        # 필요없는 컬럼 삭제
        X = data.drop(columns=['user_id','current_season_tier'])
        
        # 모델 예측
        predict_value = model.predict(X)
        
        # 타켓값들 tier로 변환
        def return_value(value):
            # 이 구간들은 단일 티어만 있음
            if value > 24:
                if value == 29:
                    return 'Master'
                elif value == 33:
                    return 'Grandmaster'
                elif value == 37:
                    return 'Challenger'
            # 구간별 티어 여러개
            else:
                # 나머지로 구간별 티어 파악
                num = value % 4
                # 구간별 1티어
                if num == 0:
                    numm = 1
                # 나머지 존재할 경우
                else:
                    numm = 5 - num
                
                # 다이아모든 
                if value > 20:
                    return 'Diamond {}'.format(numm)
                # 플래티넘
                elif value > 16:
                    return 'Platinum {}'.format(numm)
                # 골드
                elif value > 12:
                    return 'Gold {}'.format(numm)
                # 실버
                elif value > 8:
                    return 'Silver {}'.format(numm)
                # 브론즈
                elif value > 4:
                    return 'Bronze {}'.format(numm)
                # 아이언
                elif value > 0:
                    return 'Iron {}'.format(numm)
                
        result = return_value(predict_value)
        return result