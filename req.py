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
zipDict = {
    'ArlingtonZips': [76010, 76017, 76014, 76001, 76002, 76016, 76013, 76018, 76012, 76006, 76011, 76015, 76060, 76063, 75050, 75051, 75052, 76005, 76040, 76112, 76119, 76120, 76019, 76003, 76004, 76007, 76094, 76096, ],
    'AustinZips': [78745, 78745, 78753, 78741, 78758, 78704, 78744, 78759, 78748, 78749, 78705, 78723, 78727, 78750, 78731, 78702, 78757, 78703, 78752, 78717, 78724, 78739, 78751, 78735, 78746, 78721, 78726, 78747, 78754, 78617, 78729, 78730, 78701, 78756, 78722, 78736, 78653, 78660, 78732, 78652, 78712, 78725, 78733, 78742, 78610, 78613, 78641, 78664, 78681, 78710, 78719, 78728, 78734, 78737, 78738, 78798, 78799, ],
    'Corpus ChristiZips': [78415, 78413, 78412, 78414, 78418, 78411, 78410, 78404, 78408, 78401, 78417, 78407, 78409, 78406, 78402, 78419, 78373, 78374, 78380, 78470, 78471, 78473, 78474, 78475, 78405, 78416, 78362, 78370, 78476, 78477, 78478, ],
    'DallasZips': [75217, 75211, 75228, 75227, 75243, 75216, 75287, 75220, 75231, 75206, 75214, 75224, 75248, 75229, 75208, 75238, 75232, 75204, 75230, 75241, 75212, 75240, 75252, 75254, 75218, 75219, 75253, 75235, 75237, 75203, 75236, 75215, 75223, 75233, 75209, ],
    'El PasoZips': [79936, 79912, 79924, 79907, 79925, 79915, 79938, 79904, 79930, 79905, 79932, 79902, 79934, 79903, 79935, 79901, 79922, 79928, 79927, 79908, 79911, 79835, 79821, 79906, ],
    'Fort WorthZips': [76244, 76133, 76116, 76137, 76112, 76119, 76106, 76110, 76123, 76179, 76107, 76132, 76105, 76115, ],
    'GarlandZips': [75040, 75043, 75044, 75042, 75041, 75048, 75081, 75082, 75089, 75098, 5150, 75218, 75228, 75238, 75243, 75045, 75046, 75047, 75049, ],
    'HoustonZips': [77036, 77072, 77077, 77081, 77080, 77099, 77057, 77009, 77055, 77074, 77075, 77035, 77042, 77087, 77004, 77034, 77063, 77076, 77082, 77092, 77096, 77339, 77007, 77008, 77017, 77045, 77079, 77088, 77022, 77023, 77060, 77016, 77033, 77053, 77018, 77020, 77021, 77025, 77061, 77062, 77093, 77345, 77026, 77043, 77054, 77089, 77091, 77012, 77024, 77071, 77006, 77011, 77019, 77040, 77056, 77002, 77013, 77028, 77085, 77489, 77015, 77027, 77031, 77047, 77048, 77051, 77059, 77078, 77084, 77098, 77003, 77005, 77030, 77598, 77041, 77044, 77058, 77067, 77029, ],
    'IrvingZips': [75061, 75062, 75060, 75063, 75038, 75039, 75050, 75220, 75234, 75247, 75037, 75059, 75064, 75014, 75015, 75016, 75017,	],
    'LaredoZips': [78046, 78045, 78041, 78040, 78043, 78049, 78042, 78044, ],
    'LubbockZips': [79311, 79329, 79343, 79401, 79403, 79404, 79406, 79407, 79410, 79411, 79412, 79413, 79414, 79415, 79416, 79423, 79424, 79350, 79250, 79366, 79358, 79363, 79364, 79382, ],
    'PlanoZips': [75025, 75093, 75023, 75074, 75024, 75075, 75094, 75010, 75013, 75082, 75252, 75287, 75026, 75086, ],
    'San AntonioZips': [78228, 78207, 78250, 78247, 78249, 78251, 78240, 78227, 78223, 78201, 78216, 78230, 78210, 78237, 78213, 78258, 78221, 78211, 78217, 78218, 78242, 78232, 78233, 78229, 78209, 78245, 78212, 78214, 78254, 78259, 78222, 78224, 78238, 78220, 78225, 78248, 78202, 78023, 78204, 78244, 78203, 78219, 78226, 78231, 78234, 78256, 78239, 78260, 78109, 78208, 78255, 78257, 78205, 78215, 78252, 78266, 78056, 78073, 78112, 78154, 78206, 78235, 78236, 78241, 78243, 78253, 78261, 78262, 78263, 78264, 78284, 78285, 78275, 78286, 78287, 78288, 78289, 78246, 78265, 78268, 78269, 78270, 78278, 78279, 78280, 78283, 78291, 78292, 78293, 78294, 78295, 78296, 78297, 78298, 78299, ],
}
i = 1
driver = webdriver.Chrome(chromedriver_location)


def randItem(aList):
    return random.choice(list(aList))


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
            info = randItem(gopMembers) + ' ' + randItem(verbs) + ' their mistress, ' + randItem(
                firstNames) + ' ' + randItem(lastNames) + ' to get an abortion after their affair.' + randItem(hatePhrase)
        if key == 'txt1':
            info = randItem(infoLocation)
        if key == 'txt6':
            info = 'Dr. ' + (randItem(gopMembers)[0] if random.randint(0, 1) == 0 else randItem(firstNames)) + ' ' + randItem(lastNames)
        if key == 'txt2':
            cityNum = random.randint(0, len(cities))
            info = list(cities)[cityNum-1]
        if key == 'txt3':
            info = 'Texas'
        if key == 'txt4':
            info = random.choice(zipDict.get(f'{list(cities)[cityNum-1]}Zips'))
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
        time.sleep(random.randint(1, 3))
        driver.find_element_by_xpath(
            '//*[@id="forminator-module-26"]/div[13]/div/div/button').click()
        print(i)
        i += 1
    except:
        pass
