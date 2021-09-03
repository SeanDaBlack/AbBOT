from selenium import webdriver
import requests
import random
import time
from cities import cities
from data import data
from words import words

chromedriver_location = "./chromedriver"

url = 'https://prolifewhistleblower.com/anonymous-form/'

i =1
driver = webdriver.Chrome(chromedriver_location)

while(i < 10000):
    try:
        driver.get(url)
        driver.manage().timeouts().pageLoadTimeout(5, SECONDS)
    
        driver.find_element_by_xpath('//*[@id="et-boc"]/header/div/div[2]/section/div[1]/div/div/a[2]').click()
    except:
        pass
    time.sleep(5)
    # print(random.choice(list(cities.items()))[0])
    for key in data.keys():
        info = 'Placeholder'
        if key == 'txtarea':
            info = ' '.join(random.sample(words, 40))
        if key == 'txt1':
            info = ' '.join(random.sample(words, 4))
        if key == 'txt6':
            info = 'Dr. ' + random.choice(list(cities.items()))[0]
        if key == 'txt2':
            info = random.choice(list(cities.items()))[0]
        if key == 'txt3':
            info = 'Texas'
        if key == 'txt4':
            info = random.randint(10000, 99999)
        if key == 'txt5':
            info = random.choice(list(cities.items()))[1]
        
        try:
            driver.find_element_by_xpath(data.get(key)).send_keys(info)

        except:
            print("failed")
        time.sleep(random.randint(1,3))
    try:
        driver.find_element_by_xpath('//*[@id="checkbox-1"]/div/label[2]/span[1]').click()
        time.sleep(1.5)
        driver.find_element_by_xpath('//*[@id="forminator-module-26"]/div[13]/div/div/button').click()
        print(i)
        i +=1 
    except:
        pass

    
