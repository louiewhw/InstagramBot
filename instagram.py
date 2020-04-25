#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 00:07:57 2019

@author: louiewhw
"""

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from time import sleep, strftime
from selenium.webdriver.common.keys import Keys
import random
import pandas as pd 

class InstagramBot:
    

    def __init__(self, driverPath = './chromedriver'):
        self.driverPath = driverPath
        
        options = ChromeOptions()
#        options.add_argument("--headless") 
        self.browser = Chrome(executable_path = self.driverPath,chrome_options=options )

        
    def login(self, userName, passWord):


        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(1)
        username = self.browser.find_element_by_name('username')
        username.send_keys(userName)
        
        password = self.browser.find_element_by_name('password')
        password.send_keys(passWord)
        sleep(1)
        
        button_login = self.browser.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div')
        button_login.click()
        
        sleep(3)
        notificationOff = self.browser.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
        notificationOff.click()
        
        
        sleep(3)

    
    def likeAndFollow(self, tags, num=5):
        
        followedCount = 0
        likeCount = 0
        
        for tag in tags:
            
            self.browser.get('https://www.instagram.com/explore/tags/' + tag + '/')
            openPic = self.browser.find_element_by_css_selector('#react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1) > a > div')
            openPic.click()
           
            
            for i in range(num):
                
                try:
                    
                    sleep(random.randint(2, 5))
                    like = self.browser.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button')
                    like.click()
                    likeCount += 1
                    
                    sleep(random.randint(2, 5))
                    follow = self.browser.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button')
                    follow.click()
                    sleep(2)
                except:
                    pass
                try:
                    cancel = self.browser.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
                    cancel.click()
                    print('Already followed')
                except Exception:
                    pass
                finally:
                    sleep(random.randint(2, 5))
                    next = self.browser.find_element_by_css_selector('body > div._2dDPU.vCf6V > div.EfHg9 > div > div > a.HBoOv.coreSpriteRightPaginationArrow')
                    next.click()
                    followedCount += 1
                    
        print('Total followed: ' + str(followedCount))
        
    def unfollow(self, path):
        df = pd.read_csv(path)
        unfollowedCount = 0
        for username in df.username:
            
            try:
                    
                self.browser.get('https://www.instagram.com/' + username)
                
                sleep(random.randint(4, 10))
                following = self.browser.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > div.Igw0E.IwRSH.eGOV_._4EzTm > span > span.vBF20._1OSdk > button')
                following.click()
                sleep(random.randint(4, 10))
                
                unfollow = self.browser.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.-Cab_')
                unfollow.click()
                sleep(random.randint(4, 10))
                
                unfollowedCount += 1
                print('unfollowed ' + username)
            except:
                print('User not found')
        print('Total Unfollowed: ' + str(unfollowedCount))
        

            
            
if __name__ == "__main__":
    
    a = ['love', 'instagood', 'photooftheday']
    b = ['followforfollow', 'followback', 'follow4follow']
    c = ['catofinstagram']
    
    ints = InstagramBot('./chromedriver')   
    userName
    pw 
    ints.login(userName, pw)
#    ints.unfollow('unfollowList.csv')
    

    ints.likeAndFollow(c, 30)

       


