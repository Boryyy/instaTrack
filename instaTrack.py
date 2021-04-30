import os
import time
import selenium
import sys
import numpy as np

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager as CM
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import date

def greenPrint(message):
    CGREEN = '\33[32m'
    CEND = '\033[0m'
    print(CGREEN + message + CEND)
    return


def lastClose():
    greenPrint("\n..............................................\n")
    if input('\33[32m' + "[Enter] to exit\n" + '\033[0m'):
        quit()



USERNAME = '' # put your bot account username
PASSWORD = '' # put your bot account password


usr = ('') # put the account you want to track

#TIME = FOLLOWERS / TIME1 FOLLOWING

user_input = ('700')
TIME = 0.070 * int(user_input)

user_input = ('700')
TIME1 = 0.070 * int(user_input)


def scrape(username):
    options = webdriver.ChromeOptions()
    #options.add_argument("--incognito")
    #options.add_argument("--headless")        #nowindow

    mobile_emulation = {
        "userAgent": 'Mozilla/5.0 (Linux; Android 4.0.3; HTC One X Build/IML74K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/83.0.1025.133 Mobile Safari/535.19'
    }
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    bot = webdriver.Chrome(executable_path=CM().install(), options=options)

    bot.get('https://instagram.com/')
    bot.set_window_size(500, 950)
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
    time.sleep(5)

    link = 'https://www.instagram.com/{}/'.format(usr)
    bot.get(link)
    time.sleep(5)

    bot.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/ul/li[2]/a').click()

    time.sleep(3)
    print('Scrapping followers...')
    for i in range(round(TIME)):
        ActionChains(bot).send_keys(Keys.END).perform()
        time.sleep(0.5)

        followers = bot.find_elements_by_xpath(
            '//*[@id="react-root"]/section/main/div/ul/div/li/div/div[1]/div[2]/div[1]/a')

        urls = []

        for i in followers:
            if i.get_attribute('href') != None:
                urls.append(i.get_attribute('href'))
            else:
                continue

    print('Converting followers...')
    users = []
    for url in urls:
        user = url.replace('https://www.instagram.com/', '').replace('/', '')
        users.append(user)

    print('Saving...')
    f = open('followers.txt', 'w')
    s1 = '\n'.join(users)
    f.write(s1)
    f.close()
    
    time.sleep(5)

    link = 'https://www.instagram.com/{}/'.format(usr)
    bot.get(link)
    time.sleep(5)

    bot.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/ul/li[3]/a/span').click()

    time.sleep(3)
    print('Scrapping following...')
    for i in range(round(TIME1)):
        ActionChains(bot).send_keys(Keys.END).perform()
        time.sleep(0.5)

        following = bot.find_elements_by_xpath(
            '//*[@id="react-root"]/section/main/div/ul/div/li/div/div[1]/div[2]/div[1]/a')
     
        ActionChains(bot).send_keys(Keys.END).perform()

        urls = []

        for i in following:
            if i.get_attribute('href') != None:
                urls.append(i.get_attribute('href'))
            else:
                continue

    print('Converting following...')
    users1 = []
    for url in urls:
        user = url.replace('https://www.instagram.com/', '').replace('/', '')
        users1.append(user)

    print('Saving...')
    f = open('following.txt', 'w')
    s2 = '\n'.join(users1)
    f.write(s2)
    f.close()   


    if os.path.exists('oldfollowers.txt'):
    
        file1 = open("oldfollowers.txt","r+")
        file2 = open("followers.txt","r+") 
        greenPrint("\n\nComparing lists now\n")
        notFollower = list(set(users1) - set(users))  # following these people, but they are not following you back
        match = (set(file1) - set(file2))    # getting unfollowers   
        file1.close()
        file2.close()
        file3 = open("oldfollowers.txt","r")
        file4 = open("followers.txt","r")   
        added = list(set(file4) - set(file3)) # who added and removed u
        greenPrint("\nPeople that you are following, but they do not follow you back:\n\n" + ' || '.join(notFollower) + "\n")
        greenPrint("\nPeople that removed u:\n\n" ' || '+ ' || '.join(match))
        greenPrint("\nPeople that added u:\n\n" ' || '+ ' || '.join(added))
        f1 = open('oldfollowers.txt', 'w')
        greenPrint("\noldfollowers.txt has been updated!")
        s3 = '\n'.join(users)
        f1.write(s3)
        f1.close()
        
        greenPrint("\nEveryhing saved - instaTrack.txt'\n")       
        instaTrack = open("instaTrack.txt", "a+")
      
        instaTrack.write("\n=================================\n\n")
        instaTrack.write('%s\n' % date.today().strftime("%B %d, %Y"))
        
        instaTrack.write("\n=================================\n\nList 1 - People that you are following, but they do not follow you back:\n\n")
        for count, follower in enumerate(notFollower):
            instaTrack.write(("{:02d}: {}\n".format(count+1, follower)))
        
        instaTrack.write("\n=================================\n\nList 2 - People that removed u:\n\n")
        for count, removed in enumerate(match):
            instaTrack.write(("{:02d}: {}".format(count+1, removed)))

        
        instaTrack.write("\n=================================\n\nList 3 - People that added u:\n")
        for count, addedusr in enumerate(added):
            instaTrack.write(("{:02d}: {}".format(count+1, addedusr))) 
        instaTrack.close()            
   
    else:
       
        notFollower = list(set(users1) - set(users))
        greenPrint("\nPeople that you are following, but they do not follow you back:\n\n" + ' || '.join(notFollower) + "\n")
        greenPrint("\n\nThis is your first time running the script , run again to get unfollowers/added.\n")
       
        lastClose()
scrape(usr)
