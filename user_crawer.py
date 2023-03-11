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
import re
import time
import random

class yourgg:
    def __init__(self):
        self.log_file_path = 'C:/VSCode/log/user_crwaring_log.log' #로그 기록 위치
        self.driver_path = 'C:/VSCode/study/study_venv/chromedriver' #크롬 드라이버 위치
    
    def nickname(self,name):
        self.driver = webdriver.Chrome(executable_path = self.driver_path)
        self.logg = loger.mylog(self.log_file_path)
        URL = 'https://your.gg/ko/kr/profile/{}'.format(name)
        self.driver.get(url=URL)
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/header/div/div[2]/button').click()
            time.sleep(3)
            self.driver.implicitly_wait(10)
        
            self.driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[1]/div/div[2]/div[2]/button').click()
            self.driver.implicitly_wait(3)
        
            target = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/header/div/div[1]/div[2]/div/span[1]').text
            try:
                before_season = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/header/div/div[1]/div[3]/div[1]').text.split('\n')[1]
            except:
                before_season = 'unranked'
            main_position = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[1]/div/div[2]/div[2]/div[1]/div[2]/div[1]/label[1]/div/span[1]').text 
            num_gamee = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/header/div/div[1]/div[2]/div/span[3]').text
            num_game = int(re.sub('\D','',num_gamee.split()[2])) + int(re.sub('\D','',num_gamee.split()[3]))
            info = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[1]/div/div[2]/div[2]/div[3]/div/ul').text.split('\n')
            self.logg.log('유저: {} 크롤링'.format(name), level = logging.warning)
            result = [info[i * 3:(i + 1) * 3][0] for i in range((len(info) + 3 - 1) // 3 )]
            data = list([name,before_season,main_position,num_game] + result + [target])
            return data
        except:
            print('없는 소환사 명입니다. 다시 한번 입력해 주십시오')