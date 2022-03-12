
from selenium import webdriver      

import time  

import json
  
from selenium.webdriver.common.keys import Keys  
from linkedin_api import Linkedin

import os



def link_mine():
    # browser = webdriver.Chrome(executable_path = "chromedriver.exe")  
    # browser.get('https://www.linkedin.com') 
    

    # time.sleep(2) 

    # #PATH = input("Enter the Webdriver path: ")
    USERNAME = "kavishalgupta@gmail.com"
    PASSWORD = "Agentlinked47@"
    # #print(PATH)
    # print(USERNAME)
    # print(PASSWORD)

    # email=browser.find_element_by_xpath("//input[@name='session_key']")
    # email.send_keys(USERNAME)
    # password=browser.find_element_by_xpath("//input[@name='session_password']")
    # password.send_keys(PASSWORD)
    # time.sleep(3)
    # password.send_keys(Keys.RETURN)
    # t = browser.get('https://www.linkedin.com/in/vishalgupta47/')
    # connections = browser.find_elements_by_xpath("//span[starts-with(@class,'link-without-visited-state')]")
    # print(connections[0])

    api = Linkedin(USERNAME, PASSWORD)


    comp_data = api.get_company('Netflix')
    profile_data = api.get_profile('rohan')


    dict_1={
        'firstName':profile_data['firstName'],
        'lastname':profile_data['lastName'],
        'skills': [profile_data['skills'][i]['name'] for i in range(len (profile_data['skills']) )],
        'student':  profile_data['student'],
        'experience': [profile_data['experience'][i]['companyName'] for  i in range(len(profile_data['experience']))],
        'education':  profile_data['education'],
        'industryName':profile_data['industryName'],
        'summary':profile_data['summary'],
    }


    k = ['staffingCompany', 'companyIndustries', 'callToAction', 'staffCount', 'adsRule', 'companyEmployeesSearchPageUrl', 'viewerFollowingJobsUpdates', 'staffCountRange', 'permissions', 'logo', 'claimable', 'specialities', 'confirmedLocations', 'followingInfo', 'viewerEmployee',  'lcpTreatment',   'name', '$recipeType', 'fundingData', 'overviewPhoto', 'description', 'entityUrn','headquarter', 'coverPhoto', 'associatedHashtags', 'groups', 'url',  'claimableByViewer', 'jobSearchPageUrl',  'backgroundCoverImage' ]

    dict_2 = {}

    for i  in k:
        dict_2[i] = comp_data[i]



    return dict_1, dict_2


