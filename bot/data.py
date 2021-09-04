#!/usr/bin/env python3

import os
import random
import requests
import json

TEXT_GEN_API_VAR = 'DEEP_AI_KEY'

words = [
  'The', 'he', 'at', 'but', 'there', 'of', 'was', 'be', 'not', 'use', 'and', 'for', 'this', 'what', 'an', 'a', 'on', 'have', 'all', 'each',
  'to', 'are', 'from', 'were', 'which', 'in', 'as', 'or', 'we', 'she', 'is', 'with', 'ine', 'when', 'do', 'you', 'his', 'had', 'your',
  'how', 'that', 'they', 'by', 'can', 'their', 'it', 'I', 'word', 'said', 'if'
]

with open(os.path.join(os.path.dirname(__file__), './data/cities.json')) as cities_file:
  cities = json.load(cities_file)

gop_members = [
  'Gary VanDeaver', 'Bryan Slaton', 'Cecil Bell Jr.', 'Keith Bell', 'Cole Hefner', 'Matt Schaefer', 'Jay Dean', 'Cody Harris',
  'Chris Paddie', 'Travis Clardy', 'Kyle Kacal', 'Ben Leman', 'John N. Raney', 'Steve Toth', 'Will Metcalf', 'John Cyrier', 'Ernest Bailes',
  'James White', 'Terry Wilson', 'Dade Phelan', 'Mayes Middleton', 'Greg Bonnen', 'Cody Vasut', 'Brooks Landgraf', 'Tom Craddick',
  'Dustin Burrows', 'John Frullo', 'Phil Stephenson', 'John T. Smithee', 'Four Price', 'Ken King', 'Candy Noble', 'Stephanie Klick',
  'Jeff Cason', 'Matt Krause', 'Tony Tinderholt', 'David Cook', 'Craig Goldman', 'Giovanni Capriglione', 'Charlie Geren', 'Sam Harless',
  'Dan Huberty', 'Briscoe Cain', 'Dennis Paul', 'Tom Oliverson', 'Mike Schofield'
]
firstNames = [
'Amy', 'Allison', 'Arya', 'Aly', 'Alicia', 'Anna', 'Brittany', 'Bella', 'Brianna', 'Brooke', 'Beth', 'Brandy',
'Courtney', 'Camille', 'Clara', 'Christina', 'Cara', 'Caitlin', 'Dana', 'Diana', 'Dakota', 'Dani',
'Devon', 'Danielle', 'Darcy', 'Dominique', 'Ella', 'Eva', 'Erin', 'Evelyn', 'Eve', 'Ellie', 'Felicia',
'Faye', 'Faith', 'Francesca', 'Gloria', 'Gwen', 'Grace', 'Gena', 'Gabrielle', 'Hannah', 'Heather', 'Hollie',
'Hayden', 'Hazel', 'Hailey', 'Helena', 'Isabella', 'Iris', 'Julia', 'Jennifer', 'Jessica', 'Jo', 'Jackie',
'Julie', 'Marcia', 'Olivia', 'Sarah', 'Tara', 'Wanda'
]

maleFirstNames = [
'Aaron', 'Abdul', 'Adam', 'Adrian', 'Ahmed', 'Alan', 'Alex', 'Allen', 'Andrew', 'Andy', 'Anthony', 'Blake', 'Brad', 'Bradley',
'Brandon', 'Brian', 'Bryant', 'Byron', 'Buddy', 'Cameron', 'Carl', 'Carlos', 'Carter', 'Christopher', 'Chris', 'Cody', 'Clark',
'Dallas', 'Daniel', 'Donnie', 'Dante', 'Darell', 'Darrel', 'Dave', 'David', 'Demetrius', 'Derek', 'Deon', 'Domenic',
'Evan', 'Emilio', 'Emmett', 'Enrique', 'Edward', 'Ethan', 'Eric', 'Esteban', 'Floyd', 'Forest',
'Frank', 'Fred', 'Floyd', 'Fidel', 'Felton', 'Foster', 'Gabriel', 'Gene', 'Geoffrey', 'George',
'Geraldo', 'Graham', 'Glen', 'Greg', 'Jacob', 'James', 'John', 'Joseph', 'Joshua', 'Justin', 'Matthew', 'Michael', 'Nicholas',
'Pat', 'Patrick', 'Robert', 'Ryan', 'Tyler', 'William', 'Zach', 'Zachary'
]

lastNames = [
'Smith', 'Jones', 'Brown', 'Johnson', 'Williams', 'Miller', 'Taylor', 'Tyler', 'Wilson', 'Davis', 'Harris', 'Clark', 
'Hall', 'Thomas', 'Thompson', 'Moore', 'Hill', 'Walker', 'Anderson', 'Wright', 'Martin', 'Wood', 'Allen', 'Butler',
'Garcia', 'Martinez', 'Robinson', 'Rodriguez', 'Lewis', 'Lee', 'Young', 'Hernandez', 'King', 'Lopez', 'Morgan', 'Jackson',
'Scott', 'Green', 'Adams', 'Baker', 'Gonzalez', 'Nelson', 'Carter', 'Mitchell', 'Perez', 'Roberts', 'White', 'Foster',
'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins', 'Edwards', 'Stewart', 'Sanchez', 'Barnes'
]

# Seeds for text body generation
gpt2_prompts = [
  'My neighbor got an illegal abortion.', 'I suspect my father has violated the abortion ban.',
  random.choice(firstNames) + ' ' + random.choice(lastNames) + ' is helping people get abortions.',
  random.choice(gop_members) + ' has been sneaking around the abortion clinic in ' + random.choice(list(cities)) + '.'
]

info_location = [
  'A friend saw them', 'I work at the clinic', 'I know his secretary', 'He told me at the club', 'The police report', 'His wife told me',
  'From a coworker', 'From a neighbor', 'From a family member.', 'Heard from a friend', 'a relative told me', 'a private source',
  'A confession at church', 'I know their cousin', 'a taxi driver', 'From a cashier', 'Got a confidential tip', 'From a fellow parent',
  'a concerned citizen', 'From a relative.', 'A PP volunteer', 'A charity worker', 'A social worker', 'From my friend who knows cops',
  'from a lawyer', 'From a government employee', 'She told me privately', 'Her mother told me', 'I overheard them talking'
]

zip_codes = [
  75001,
  75006,
  75011,
  75014,
  75015,
  75016,
  75017,
  75019,
  75030,
  75038,
  75039,
  75040,
  75041,
  75042,
  75043,
  75044,
  75045,
  75046,
  75047,
  75048,
  75048,
  75049,
  75050,
  75051,
  75052,
  75053,
  75054,
  75060,
  75061,
  75062,
  75063,
  75080,
  75081,
  75082,
  75083,
  75085,
  75088,
  75089,
  75104,
  75106,
  75115,
  75116,
  75123,
  75134,
  75137,
  75138,
  75141,
  75146,
  75149,
  75150,
  75159,
  75159,
  75172,
  75180,
  75180,
  75181,
  75182,
  75182,
  75185,
  75187,
  75201,
  75202,
  75203,
  75204,
  75205,
  75206,
  75207,
  75208,
  75209,
  75210,
  75211,
  75212,
  75214,
  75215,
  75216,
  75217,
  75218,
  75219,
  75220,
  75221,
  75222,
  75223,
  75224,
  75225,
  75226,
  75227,
  75228,
  75229,
  75230,
  75231,
  75232,
  75233,
  75234,
  75234,
  75235,
  75236,
  75237,
  75238,
  75239,
  75240,
  75241,
  75242,
  75243,
  75244,
  75244,
  75245,
  75246,
  75247,
  75248,
  75249,
  75250,
  75251,
  75253,
  75254,
  75258,
  75260,
  75261,
  75262,
  75263,
  75264,
  75265,
  75266,
  75267,
  75270,
  75295,
  75313,
  75315,
  75336,
  75339,
  75342,
  75354,
  75355,
  75356,
  75357,
  75359,
  75360,
  75367,
  75370,
  75371,
  75372,
  75374,
  75376,
  75378,
  75379,
  75380,
  75381,
  75382,
  75398,
]
# TX IPs gathered from here: https://www.xmyip.com/ip-addresses/united--states/texas
ips = [
  "64.46.160.",  # Addison
  "50.26.131.",  # Amarillo
  "8.34.145.",  # Austin
  "24.155.228.",  # Austin
  "24.32.117.",  # Clarksville
  "66.170.212.",  # Conroe
  "67.67.45.",  # Coppell
  "12.53.23.",  # Dallas
  "12.56.225.",  # Dallas
  "12.134.216.",  # Dallas
  "12.135.64.",  # Dallas
  "12.209.171.",  # Dallas
  "23.95.39.",  # Dallas
  "23.216.55.",  # Dallas
  "23.218.192.",  # Dallas
  "24.219.28.",  # Dallas
  "32.144.40.",  # Dallas
  "50.84.221.",  # Dallas
  "63.25.84.",  # Dallas
  "63.133.145.",  # Dallas
  "63.234.233.",  # Dallas
  "64.195.173.",  # Dallas
  "65.44.75.",  # Dallas
  "67.48.192.",  # Dallas
  "68.95.146.",  # Dallas
  "24.219.171.",  # Denton
  "68.116.255.",  # Denton
  "67.10.46.",  # Edinburg
  "47.185.148.",  # Flower Mound
  "12.251.72.",  # Fort Stockton
  "12.210.27.",  # Fort Worth
  "24.219.163.",  # Fort Worth
  "50.11.19.",  # Fort Worth
  "68.113.154.",  # Fort Worth
  "12.8.38.",  # Houston
  "12.68.245.",  # Houston
  "12.198.216.",  # Houston
  "16.35.199.",  # Houston
  "16.160.30.",  # Houston
  "16.186.156.",  # Houston
  "24.206.72.",  # Houston
  "24.206.173.",  # Houston
  "34.9.77.",  # Houston
  "34.131.207.",  # Houston
  "38.100.150.",  # Houston
  "45.33.171.",  # Houston
  "65.124.92.",  # Houston
  "66.67.94.",  # Houston
  "66.25.22.",  # Irving
  "50.84.181.",  # Irving
  "24.32.224.",  # Kingwood
  "68.88.193.",  # Lancaster
  "38.114.200.",  # Lufkin
  "24.242.89.",  # Pflugerville
  "67.10.20.",  # Pharr
  "24.173.213.",  # Plano
  "50.84.81.",  # Plano
  "68.22.119.",  # Plano
  "68.72.56.",  # Plano
  "68.90.204.",  # Plano
  "68.93.19.",  # Plano
  "23.113.179.",  # Richardson
  "23.123.121.",  # Richardson
  "23.126.17.",  # Richardson
  "63.204.90.",  # Richardson
  "63.204.168.", # Richardson
  "65.69.103.",  # Richardson
  "65.70.203.",  # Richardson
  "66.138.5.",  # Richardson
  "67.39.101.",  # Richardson
  "68.72.114.",  # Richardson
  "63.174.141.",  # Rocksprings
  "8.9.196.",  # San Antonio
  "12.211.20.",  # San Antonio
  "15.105.182.",  # San Antonio
  "15.120.150.",  # San Antonio
  "15.126.8.",  # San Antonio
  "15.129.118.",  # San Antonio
  "15.132.18.",  # San Antonio
  "15.142.164.",  # San Antonio
  "15.145.145.",  # San Antonio
  "15.155.5.",  # San Antonio
  "15.152.9.",  # San Antonio
  "15.153.121.",  # San Antonio
  "15.153.133.",  # San Antonio
  "15.162.231.",  # San Antonio
  "15.170.117.",  # San Antonio
  "15.173.25.",  # San Antonio
  "15.180.1.",  # San Antonio
  "15.180.224.",  # San Antonio
  "15.181.177.",  # San Antonio
  "15.193.183.",  # San Antonio
  "15.204.186.",  # San Antonio
  "15.213.214.",  # San Antonio
  "15.214.133.",  # San Antonio
  "15.214.237.",  # San Antonio
  "15.216.199.",  # San Antonio
  "15.224.247.",  # San Antonio
  "24.173.86.",  # San Antonio
  "50.84.228.",  # San Antonio
  "50.95.50.",  # San Antonio
  "67.155.93.",  # San Antonio
  "68.98.252.",  # San Antonio
  "67.179.27.",  # Seguin
  "12.205.32.",  # Sugar Land
  "50.162.51.",  # Sugar Land
  "64.61.53.",  # Sugar Land
  "24.119.145.",  # Texarkana
  "66.76.230.",  # Tyler
  "24.32.200.",  # Vernon
]
# random element from each list


def anonymous_form():
  while True:
    city, county = random.choice(list(cities.items()))
    form_data = {
      'textarea-1': get_tip_body(),
      'text-1': random.choice(info_location),
      'text-6': 'Dr. ' + random.choice(maleFirstNames) + ' ' + random.choice(lastNames),
      'text-2': city,
      'text-3': 'Texas',
      'text-4': str(random.randint(75001, 79942)),
      'text-5': county,
      'hidden-1': random.choice(ips) + str(random.randint(0, 255)),
      'checkbox-1[]': 'yes' if random.choice([True, False]) else 'no',
    }
    yield form_data


def sign_up_page():
  raise NotImplementedError()


def get_tip_body():
  # If we have an API key for GPT2, use it
  if TEXT_GEN_API_VAR in os.environ:
    prompt = random.choice(gpt2_prompts)
    r = requests.post(
      "https://api.deepai.org/api/text-generator", data={
        'text': prompt,
      }, headers={'api-key': os.environ[TEXT_GEN_API_VAR]}
    )
    rv = str(r.json()['output'].encode('utf-8'))
    # cut out the prompt, which comes from a limited set and can be filtered on
    rv = rv.replace(prompt, '').lstrip()
    # take string up through last complete sentence since we occasionally get trailing words
    if '.' in rv:
      rv = rv[0:rv.rindex('.')] + '.'
    return rv
  else:
    # standard tip body generation
    return random.choice(gop_members) + ' took their mistress ' + random.choice(firstNames) + ' ' + random.choice(
      lastNames
    ) + ' to get an abortion after their affair.'
