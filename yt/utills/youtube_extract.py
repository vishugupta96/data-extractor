import json
import pandas as pd

from selenium import webdriver     
#from datamine import settings 
  

import time  
import os
   
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By



  

def yt_data_mine():
    youtube = {'followers':'','description':'','lifetime_views':''}
    #executable_path = os.path.join(settings.MEDIA_ROOT,"chromedriver.exe")
    # executable_path = 'chromedriver.exe'
    # print('executable_path: ', executable_path)

    # browser = webdriver.Chrome(executable_path)  
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
    browser.get('https://www.youtube.com/channel/UCfLdIEPs1tYj4ieEdJnyNyw') 
    time.sleep(2) 
    followers = browser.find_elements_by_xpath("//yt-formatted-string[starts-with(@id,'subscriber-count')]")
    # print(followers[0].text)
    youtube['followers'] = followers[0].text
    #PATH = input("Enter the Webdriver path: ")
    browser.maximize_window()
    time.sleep(2)
    description = browser.find_elements_by_xpath('//*[@id="tabsContent"]/tp-yt-paper-tab[7]/div')
    print(description[0].text)
    time.sleep(2)
    description[0].click()
    time.sleep(2)

    youtube['description'] = description[0].text
    description = browser.find_element_by_xpath("//yt-formatted-string[starts-with(@id,'description')]")
    # print(description.text)
    lifetime_views = browser.find_element_by_xpath("//*[@id='right-column']/yt-formatted-string[3]")
    # print(lifetime_views.text)
    youtube['lifetime_views'] = lifetime_views.text
    vids_tab = browser.find_element_by_xpath('//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div')
    # print(vids_tab.text)

    time.sleep(2)
    vids_tab.click()
    time.sleep(2)
    browser.execute_script("window.scrollTo(2, 1080)")
    time.sleep(2)

    browser.execute_script("window.scrollTo(2, 1080)")
    videos = browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]')
    a = []


    for i in range(1,25):
        c = {}
        t = videos.find_element_by_xpath('//*[@id="items"]/ytd-grid-video-renderer['+ str(i)+']')
        print(t.text.split('\n'))
        list_ = t.text.split('\n')
        for i in range(len(list_)):
            if i == 0:
                c['duration'] = list_[i]
            if i == 1:
                c['name'] = list_[i]
            if i == 2:
                c['views'] = list_[i]
            if i == 3:
                c['time'] = list_[i]
        a.append(c)
    
    #video data
    youtube['videos']  = a
    time.sleep(2)



    element = browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[8]')
    ast = element.find_element_by_tag_name('a')
    browser.execute_script("arguments[0].click();", ast)

    time.sleep(2)
    for i in range(15):
        browser.execute_script("window.scrollTo(0, 1080)")
    time.sleep(1)

    asd = browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[1]/h2')
    # asd.text.split(' ')

    youtube['comments_count'] = asd.text.split(' ')[0]

    # COMMENTS COUNT
    youtube['comments_count']

    a = []

    comments = browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]')
    time.sleep(4)

    
    time.sleep(4)
    for i in range(2,20):
        if i == 10:
            browser.execute_script("window.scrollTo(2, 1080)")
        c = {}
        t = comments.find_element_by_xpath('//*[@id="contents"]/ytd-comment-thread-renderer['+ str(i)+']')
        print(t.text.split('\n'))
        list_ = t.text.split('\n')
        for i in range(len(list_)):
            if i == 0:
                c['name'] = list_[i]
            if i == 1:
                c['time'] = list_[i]
            if i == 2:
                c['comments'] = list_[i]
            if i == 3:
                c['likes'] = list_[i]
        a.append(c)
    # COMMENTS DATA
    youtube['comments']  = a


    # ff = {'comment_count':youtube['comments_count']}
    # df_v = pd.DataFrame.from_dict(youtube['videos'])
    # df_c = pd.DataFrame.from_dict(youtube['comments'])
    # df_d  = pd.DataFrame.from_dict([ff])


    # df_v.to_csv('yt_videos.csv', index=False)
    # df_c.to_csv('yt_comments.csv', index=False)
    # df_d.to_csv('yt_comments.csv', index=False)


    return (youtube)




# x = yt_data_mine()
# print(x)

# print(r['vids'])



#yt = pd.DataFrame.from_dict(r['vid'])
# pd.tocsv





