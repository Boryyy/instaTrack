import os
import time
import selenium
import wget
import pickle
import datetime
import difflib
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager as CM
from datetime import date
import random

USERNAME = '' # put your main account username
PASSWORD = '' # put your main account password

SUSERNAME = '' # put your bot account username
SPASSWORD = '' # put your bot account password

usr = USERNAME

def grab(username):
    options = webdriver.ChromeOptions()

    mobile_emulation = {
        "userAgent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57'
    }
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    bot = webdriver.Chrome(executable_path=CM().install(), options=options)

    if os.path.exists('first.pkl'):
        print("Cookies found!")
        bot.get('https://instagram.com/')
        bot.set_window_size(600, 1000)
        time.sleep(5)
        cookies = pickle.load(open("first.pkl", "rb"))
        for cookie in cookies:
            bot.add_cookie(cookie)   
        time.sleep(2)     
        bot.get('https://instagram.com/')
        print("Logged in!")
        time.sleep(5)

    else:
        print("Cookies not found!")
        bot.get('https://instagram.com/')
        bot.set_window_size(400, 900)
        time.sleep(5)
        bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div/div/div/div[3]/button[1]').click()
        print("Logging in...")

        time.sleep(1)
        username_field = bot.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input')
        username_field.send_keys(USERNAME)
        find_pass_field = (
            By.XPATH, '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input')
        WebDriverWait(bot, 50).until(
            EC.presence_of_element_located(find_pass_field))
        pass_field = bot.find_element(*find_pass_field)
        WebDriverWait(bot, 50).until(
            EC.element_to_be_clickable(find_pass_field))
        pass_field.send_keys(PASSWORD)
        bot.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button').click()
           
        time.sleep(2)

        link = 'https://www.instagram.com/'
        bot.get(link)

        time.sleep(2)
        pickle.dump( bot.get_cookies() , open("first.pkl","wb"))
        print("Cookes saved!")
        time.sleep(2)


    time.sleep(1)
    link = 'https://www.instagram.com/accounts/access_tool/accounts_following_you'
    bot.get(link)
    time.sleep(2)

    try:
        while True:
                button = bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/main/button')
                bot.execute_script("arguments[0].click();", button)
                bot.find_element_by_xpath('//body').send_keys(Keys.CONTROL+Keys.END)
                time.sleep(2)
    except:
        pass

    content = bot.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/main/section')[0].text
    time.sleep(2)

    print("Followers Saved!")
    f1 = open('followers.txt', 'w')
    s3 = ''.join(content)
    f1.write(s3)
    f1.close()  

    if os.path.exists('oldfollowers.txt'):
    
        small_file = open('oldfollowers.txt','r')
        long_file = open('followers.txt','r')
        output_file = open('whoremovedyou.txt','w')

        try:
            small_lines = small_file.readlines()
            long_lines = long_file.readlines()
            small_lines_cleaned = [line.rstrip().lower() for line in small_lines]
            long_file_lines = long_file.readlines()
            long_lines_cleaned = [line.rstrip().lower() for line in long_lines]

            for line in small_lines_cleaned:
                if line not in long_lines_cleaned:
                    output_file.writelines(line + '\n')

        finally:
            small_file.close()
            long_file.close()
            output_file.close()
                

        small_file1 = open('followers.txt','r')
        long_file1 = open('oldfollowers.txt','r')
        output_file1 = open('whoaddedyou.txt','w')

        try:
            small_lines = small_file1.readlines()
            long_lines = long_file1.readlines()
            small_lines_cleaned = [line.rstrip().lower() for line in small_lines]
            long_file_lines = long_file1.readlines()
            long_lines_cleaned = [line.rstrip().lower() for line in long_lines]

            for line in small_lines_cleaned:
                if line not in long_lines_cleaned:
                    output_file1.writelines(line + '\n')

        finally:
            small_file1.close()
            long_file1.close()
            output_file1.close()

        whoremovedyou = open("whoremovedyou.txt","r")
        whoaddedyou = open("whoaddedyou.txt","r") 
        
        print("Printing in Instagram DM shortly!")
        instaTrackDM = open("instaTrackDM.txt", "w+")
      
        instaTrackDM.write("===========================\n")
        instaTrackDM.write('%s\n' % date.today().strftime("%B %d, %Y"))
       
        
        instaTrackDM.write("===========================\n\nPeople that removed u:\n\n")
        for count, removed in enumerate(whoremovedyou):
            instaTrackDM.write(("{:02d}: @{}".format(count+1, removed)))

        
        instaTrackDM.write("\n===========================\n\nPeople that added u:\n")
        for count, addedusr in enumerate(whoaddedyou):
            instaTrackDM.write(("{:02d}: @{}".format(count+1, addedusr)))
        instaTrackDM.close()

        print("Oldollowers Saved!")
        f1 = open('oldfollowers.txt', 'w')
        s3 = ''.join(content)
        f1.write(s3)
        f1.close()  
        
    else:

        print("This is the first time running the script , run again to get results! (Best time after 24 hours)")
        s5 = open('oldfollowers.txt','w')   
    
    if os.path.exists('second.pkl'):

        bot.delete_all_cookies() #clearing data so can login in bot account

        bot.get('https://instagram.com/')
        cookies = pickle.load(open("second.pkl", "rb"))
        for cookie in cookies:
            bot.add_cookie(cookie)   
        time.sleep(2)     
        bot.get('https://instagram.com/')

        link = 'https://www.instagram.com/{}/'.format(usr)
        bot.get(link)
        time.sleep(1)
        
        f5 = open('instaTrackDM.txt', 'r', encoding="utf-8")
        file_contents = f5.read()
        
        bot.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/header/section/div[2]/div/div[1]/button/div').click() 
        time.sleep(1) 
        bot.find_element_by_xpath(
        '/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div/textarea').click()
        time.sleep(2)
        l = [file_contents]
        mbox = bot.find_element_by_tag_name('textarea')
        mbox.send_keys(random.choice(l))
        bot.find_element_by_xpath(
        '/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div[2]/button').click() 
        time.sleep(1)

        bot.quit()

    else:

        bot.delete_all_cookies()
        
        bot.get('https://instagram.com/')
        time.sleep(3)
        bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div/div/div/div[3]/button[1]').click()
        time.sleep(1)
        username_field = bot.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input')
        username_field.send_keys(SUSERNAME)
        find_pass_field = (
            By.XPATH, '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input')
        WebDriverWait(bot, 50).until(
            EC.presence_of_element_located(find_pass_field))
        pass_field = bot.find_element(*find_pass_field)
        WebDriverWait(bot, 50).until(
            EC.element_to_be_clickable(find_pass_field))
        pass_field.send_keys(SPASSWORD)
        bot.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button').click()
        time.sleep(2)

        link = 'https://www.instagram.com/'
        bot.get(link)
        time.sleep(2)

        pickle.dump( bot.get_cookies() , open("second.pkl","wb"))
        time.sleep(2)
        print("Second account cookies saved!")

        link = 'https://www.instagram.com/{}/'.format(usr)
        bot.get(link)
        time.sleep(1)
        
        f5 = open('instaTrackDM.txt', 'r', encoding="utf-8")
        file_contents = f5.read()
        
        bot.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/header/section/div[2]/div/div[1]/button/div').click() 
        time.sleep(2) 
        bot.find_element_by_xpath(
        '/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div/textarea').click()
        time.sleep(2)
        l = [file_contents]
        mbox = bot.find_element_by_tag_name('textarea')
        mbox.send_keys(random.choice(l))
        bot.find_element_by_xpath(
        '/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div[2]/button').click() 
        time.sleep(1)
        bot.quit()

grab(usr)
