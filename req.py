from selenium import webdriver
import requests
import random
import time

chromedriver_location = "usr/bin/chromedriver"

url = 'https://prolifewhistleblower.com/anonymous-form/'

data = {
    'txtarea': '//*[@id="forminator-field-textarea-1"]',
    'txt1': '//*[@id="forminator-field-text-1"]',
    'txt6': '//*[@id="forminator-field-text-6"]',
    'txt2': '//*[@id="forminator-field-text-2"]',
    'txt3': '//*[@id="forminator-field-text-3"]',
    'txt4': '//*[@id="forminator-field-text-4"]',
    'txt5': '//*[@id="forminator-field-text-5"]'

}

words = [
'The',  'he',   'at',	'but',  'there',
'of',   'was',  'be', 	'not', 	'use',
'and', 	'for', 	'this', 'what',	'an',
'a',    'on',   'have', 'all',  'each',
'to', 	'are', 	'from', 'were', 'which',
'in', 	'as', 	'or', 	'we', 	'she',
'is', 	'with', 'ine', 	'when', 'do',
'you', 	'his', 	'had', 	'your', 'how',
'that', 'they', 'by', 	'can', 	'their',
'it', 	'I', 	'word',	'said',	'if'
]

cities = {'Arlington':	'Tarrant County',
'Austin':	'Travis County',
'Corpus Christi':	'Nueces County',
'Dallas':	'Collin County',
'El Paso':	'El Paso County',
'Fort Worth':	'Denton County',
'Garland':	'Collin County',
'Houston':	'Fort Bend County',
'Irving':	'Dallas County',
'Laredo':	'Webb County',
'Lubbock':	'Lubbock County',
'Plano':	'Collin County',
'San Antonio': 'Bexar County'}
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

    
