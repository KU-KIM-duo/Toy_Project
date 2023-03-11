import pandas as pd

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import logging
import loger


import itertools
import pymysql
import re
import time
import random


sql_connect = pymysql.Connect(
    host = 'localhost',#'129.154.62.175',
    user = 'root',#'streamlit',
    password = 'qjfjrdjaak2',#'bigdata1!',
    db = 'lol_db',#유저 닉네임 있는 디비 입력,
    charset = 'utf8mb4'
)
cursor = sql_connect.cursor()
cursor.execute('select * from user_name')
load_data = cursor.fetchall()
user_name = pd.DataFrame(load_data)[1]
sql_connect.close()

sql_connect = pymysql.Connect(
    host = 'localhost',#'129.154.62.175',
    user = 'root',#'streamlit',
    password = 'qjfjrdjaak2',#'bigdata1!',
    db = 'lol_db',#유저 지표 데이터 넣을 디비 입력,
    charset = 'utf8mb4'
)
cursor = sql_connect.cursor()
slq = 'insert into user_name (user_name) values(%s)'#inser구문 테이블 이름과 변수명 수정 필요


log_file_path = 'C:/VSCode/log/user_crwaring_log.log'
driver_path = 'C:/VSCode/study/study_venv/chromedriver'

driver = webdriver.Chrome(executable_path='driver_path')
logg = loger.mylog(log_file_path)




for x,i in enumerate(user_name):
    URL = 'https://your.gg/ko/kr/profile/{}'.format(i)
    driver.get(url=URL)
    driver.implicitly_wait(10)
    try:
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/header/div/div[2]/button').click()
        time.sleep(time.sleep(4,8))
        
        driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[1]/div/div[2]/div[2]/button').click()
        driver.implicitly_wait(2)
        
        target = driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/header/div/div[1]/div[2]/div/span[1]').text
        
        try:
            before_season = driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/header/div/div[1]/div[3]/div[1]').text.split('\n')[1]
        except:
            before_season = 'unranked'
        
        
        main_position = driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/label[1]/div/span[1]').text 
        
        num_gamee = driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/header/div/div[1]/div[2]/div/span[3]').text
        num_game = int(re.sub('\D','',num_gamee.split()[2])) + int(re.sub('\D','',num_gamee.split()[3]))
        
        info = driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[1]/div/div[2]/div[2]/div[3]/div/ul').text.split('\n')
        
        logg.log('유저: {} 크롤링'.format(i), level = logging.warning)
        
        result = [info[i * 3:(i + 1) * 3][0] for i in range((len(info) + 3 - 1) // 3 )]
        
        va = tuple(list([i,before_season,main_position,num_game] + result + [target]))
        
        cursor.execute(slq, va)
        sql_connect.commit()
        logg.log('유저: {} MySQL Insert'.format(i), level = logging.warning)
    except:
        pass

sql_connect.close()
driver.quit()