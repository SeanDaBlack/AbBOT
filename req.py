from selenium import webdriver
import requests
import random
import time

# For Mac
## chromedriver_location = "./chromedriver"
# For Windows
chromedriver_location = "./chromedriver.exe"


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

infoLocation = [
    'A friend saw them',
    'I work at the clinic',
    'I know their secretary',
    'He told me at the club',
    'The police report',
    'His wife told me',
    'I live near the clinic',
    'My friend works in the clinic',
    'I overheard them at a bar',
    'I heard them arguing at a restaurant'
]

gopMembers = [
    'Gary VanDeaver',
    'Bryan Slaton',
    'Cecil Bell Jr.',
    'Keith Bell',
    'Cole Hefner',
    'Matt Schaefer',
    'Jay Dean',
    'Cody Harris',
    'Chris Paddie',
    'Travis Clardy',
    'Kyle Kacal',
    'Ben Leman',
    'John N. Raney',
    'Steve Toth',
    'Will Metcalf',
    'John Cyrier',
    'Ernest Bailes',
    'James White',
    'Terry Wilson',
    'Dade Phelan',
    'Mayes Middleton',
    'Greg Bonnen',
    'Cody Vasut',
    'Brooks Landgraf',
    'Tom Craddick',
    'Dustin Burrows',
    'John Frullo',
    'Phil Stephenson',
    'John T. Smithee',
    'Four Price',
    'Ken King',
    'Candy Noble',
    'Stephanie Klick',
    'Jeff Cason',
    'Matt Krause',
    'Tony Tinderholt',
    'David Cook',
    'Craig Goldman',
    'Giovanni Capriglione',
    'Charlie Geren',
    'Sam Harless',
    'Dan Huberty',
    'Briscoe Cain',
    'Dennis Paul',
    'Tom Oliverson',
    'Mike Schofield'
]

firstNames = [
    'Hannah',   'Olivia',
    'Marcia',   'Sarah',
    'Tara',     'Brooke',
    'Wanda',    'Andrea',
    'Julie',    'Brenda',
    'Lindsey',  'Danielle'
]

lastNames = [
    'Morgan',   'Walker',
    'Lewis',    'Butler',
    'Jones',    'Barnes',
    'Martin',   'Wright',
    'Foster',   'Colson',
    'Tantoro',  'Hill',
    'Platter',  'Soprano'
]

verbs = [
    'took', 'encouraged', 'brought', 'helped', 'forced',
]

hatePhrase = [
    ' I wouldn\'t breath the same air.',                    ' I wouldn\'t touch them with a ten-foot pole!',
    ' I unfortunately won\'t be voting red for a while.',   ' I\'m sick to my stomach just thinking about it.',
    ' Oh, that makes my skin crawl!',                       ' I think it\'s quite nauseating!', 
    ' "You shall not murder." Exodus 20:13',                ' Shame on these monsters!',
    ' "Children are a heritage from the LORD, offspring a reward from him." Psalm 127:3',
    ' "Like arrows in the hands of a warrior are children born in one’s youth." Psalm 127:4', '',
]

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

cities = {
    'Arlington':        'Tarrant County',
    'Austin':           'Travis County',
    'Corpus Christi':	'Nueces County',
    'Dallas':	        'Collin County',
    'El Paso':	        'El Paso County',
    'Fort Worth':	    'Denton County',
    'Garland':	        'Collin County',
    'Houston':	        'Fort Bend County',
    'Irving':	        'Dallas County',
    'Laredo':	        'Webb County',
    'Lubbock':	        'Lubbock County',
    'Plano':	        'Collin County',
    'San Antonio':      'Bexar County'
          }
i = 1
driver = webdriver.Chrome(chromedriver_location)

while(i < 10000):
    try:
        driver.get(url)
        driver.manage().timeouts().pageLoadTimeout(5)

        driver.find_element_by_xpath(
            '//*[@id="et-boc"]/header/div/div[2]/section/div[1]/div/div/a[2]').click()
    except:
        pass
    time.sleep(5)
    # print(random.choice(list(cities.items()))[0])
    for key in data.keys():
        info = 'Placeholder'
        # if key == 'txtarea':
        #     info = ' '.join(random.sample(words, 40))
        if key == 'txtarea':
            info = random.choice(list(gopMembers)) + ' ' + random.choice(list(verbs)) + ' their mistress, ' + random.choice(list(
                firstNames)) + ' ' + random.choice(list(lastNames)) + ' to get an abortion after their affair.' + random.choice(list(hatePhrase))
        # if key == 'txt1':
        #     info = ' '.join(random.sample(words, 4))
        if key == 'txt1':
            info = random.choice(list(infoLocation))
        if key == 'txt6':
            info = 'Dr. ' + random.choice(list(lastNames))
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
        time.sleep(random.randint(1, 3))
    try:
        driver.find_element_by_xpath(
            '//*[@id="checkbox-1"]/div/label[2]/span[1]').click()
        time.sleep(1.5)
        driver.find_element_by_xpath(
            '//*[@id="forminator-module-26"]/div[13]/div/div/button').click()
        print(i)
        i += 1
    except:
        pass
