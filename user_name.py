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

sql_connect = pymysql.Connect(
    host = 'localhost',#'129.154.62.175',
    user = 'root',#'streamlit',
    password = 'qjfjrdjaak2',#'bigdata1!',
    db = 'lol_db',#db 이름 입력,
    charset = 'utf8mb4'
)
cursor = sql_connect.cursor()
slq = 'insert into user_name (user_name) values(%s)'#inser구문 테이블 이름과 변수명 수정 필요

log_file_path = 'C:/VSCode/log/name_crwaring_log.log'#logging 결과 텍스트 파일 위치
logg = loger.mylog(log_file_path)

driver_path = 'C:/VSCode/study/study_venv/chromedriver'#크롬 driver 위치
num = [1,2,5,6,15,50,75,76,150,151,250,251,400,401,799,800,900,901,1300,1301,2499,2500,
       3000,3001,3500,3501,5000,5001,6000,6001,9000,9001,11000,11001,13000,13001,15000,
       15001,16000,16001,18000,18001,19000,19001,20000,20001]
driver = webdriver.Chrome(executable_path='driver_path')

for i in num:
    URL = 'https://www.op.gg/leaderboards/tier?page={}'.format(i)
    driver.get(url=URL)
    driver.implicitly_wait(3)
    name = driver.find_elements(By.CSS_SELECTOR,'#content-container > div.css-ndvmk6.e1fnyy5m0 > table > tbody > tr > td > a > strong')
    logg.log('{} 번째 페이지 크롤링'.format(i), level = logging.warning)
    name_list = list(map(lambda x: x.text,name))
    for x in name_list:
        cursor.execute(slq, x)
        sql_connect.commit()
        logg.log('유저닉네임 {} 삽입 위험'.format(x), level = logging.warning)
sql_connect.close()
driver.quit()