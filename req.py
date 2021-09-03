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
    'I heard them arguing at a restaurant',
    'I worked with the mistress.',
    'Our kids go to school together.',
    'The choir director at church told me!'
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
    'Mike Schofield',
    'Ted Cruz',
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
    'took', 'encouraged', 'brought', 'helped', 'forced', 'paid', 'bribed', 'allowed', 'went with',
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

zipCodes = [75001,75006,75011,75014,75015,75016,75017,75019,75030,75038,75039,75040,75041,75042,75043,75044,75045,75046,75047,75048,75048,75049,75050,75051,75052,75053,75054,75060,75061,75062,75063,75080,75081,75082,75083,75085,75088,75089,75104,75106,75115,75116,75123,75134,75137,75138,75141,75146,75149,75150,75159,75159,75172,75180,75180,75181,75182,75182,75185,75187,75201,75202,75203,75204,75205,75206,75207,75208,75209,75210,75211,75212,75214,75215,75216,75217,75218,75219,75220,75221,75222,75223,75224,75225,75226,75227,75228,75229,75230,75231,75232,75233,75234,75234,75235,75236,75237,75238,75239,75240,75241,75242,75243,75244,75244,75245,75246,75247,75248,75249,75250,75251,75253,75254,75258,75260,75261,75262,75263,75264,75265,75266,75267,75270,75295,75313,75315,75336,75339,75342,75354,75355,75356,75357,75359,75360,75367,75370,75371,75372,75374,75376,75378,75379,75380,75381,75382,75398,]

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
        if key == 'txtarea':
            info = random.choice(list(gopMembers)) + ' ' + random.choice(list(verbs)) + ' their mistress, ' + random.choice(list(
                firstNames)) + ' ' + random.choice(list(lastNames)) + ' to get an abortion after their affair.' + random.choice(list(hatePhrase))
        if key == 'txt1':
            info = random.choice(list(infoLocation))
        if key == 'txt6':
            info = 'Dr. ' + random.choice(list(lastNames))
        if key == 'txt2':
            cityNum = random.randint(0, len(cities))
            info = list(cities)[cityNum-1]
        if key == 'txt3':
            info = 'Texas'
        if key == 'txt4':
            info = random.choice(list(zipCodes))
        if key == 'txt5':
            info = list(cities.values())[cityNum-1]

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
