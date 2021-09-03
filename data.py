import random
import time

words = [
  'The', 'he', 'at', 'but', 'there', 'of', 'was', 'be', 'not', 'use', 'and', 'for', 'this', 'what', 'an', 'a', 'on', 'have', 'all', 'each',
  'to', 'are', 'from', 'were', 'which', 'in', 'as', 'or', 'we', 'she', 'is', 'with', 'ine', 'when', 'do', 'you', 'his', 'had', 'your',
  'how', 'that', 'they', 'by', 'can', 'their', 'it', 'I', 'word', 'said', 'if'
]

cities = {
  'Arlington': 'Tarrant County',
  'Austin': 'Travis County',
  'Corpus Christi': 'Nueces County',
  'Dallas': 'Collin County',
  'El Paso': 'El Paso County',
  'Fort Worth': 'Denton County',
  'Garland': 'Collin County',
  'Houston': 'Fort Bend County',
  'Irving': 'Dallas County',
  'Laredo': 'Webb County',
  'Lubbock': 'Lubbock County',
  'Plano': 'Collin County',
  'San Antonio': 'Bexar County'
}

gop_members = [
  'Gary VanDeaver', 'Bryan Slaton', 'Cecil Bell Jr.', 'Keith Bell', 'Cole Hefner', 'Matt Schaefer', 'Jay Dean', 'Cody Harris',
  'Chris Paddie', 'Travis Clardy', 'Kyle Kacal', 'Ben Leman', 'John N. Raney', 'Steve Toth', 'Will Metcalf', 'John Cyrier', 'Ernest Bailes',
  'James White', 'Terry Wilson', 'Dade Phelan', 'Mayes Middleton', 'Greg Bonnen', 'Cody Vasut', 'Brooks Landgraf', 'Tom Craddick',
  'Dustin Burrows', 'John Frullo', 'Phil Stephenson', 'John T. Smithee', 'Four Price', 'Ken King', 'Candy Noble', 'Stephanie Klick',
  'Jeff Cason', 'Matt Krause', 'Tony Tinderholt', 'David Cook', 'Craig Goldman', 'Giovanni Capriglione', 'Charlie Geren', 'Sam Harless',
  'Dan Huberty', 'Briscoe Cain', 'Dennis Paul', 'Tom Oliverson', 'Mike Schofield'
]
firstNames = ['Hannah', 'Olivia', 'Marcia', 'Sarah', 'Tara', 'Brooke', 'Wanda', 'Andrea', 'Julie']
lastNames = ['Morgan', 'Walker', 'Lewis', 'Butler', 'Jones', 'Barnes', 'Martin', 'Wright', 'Foster']

info_location = [
  'A friend saw them', 'I work at the clinic', 'I know his secretary', 'He told me at the club', 'The police report', 'His wife told me'
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
  "15.180.224.",  # San Antonio
  "15.155.5.",  # San Antonio
  "15.153.133.",  # San Antonio
  "12.56.225.",  # Dallas
  "67.10.46."  # Edinburg
]
# random element from each list


def anonymous_form():
  while True:
    city, county = random.choice(list(cities.items()))
    form_data = {
      'textarea-1': random.choice(gop_members) + ' took their mistress ' + random.choice(firstNames) + ' ' + random.choice(lastNames) +
      ' to get an abortion after their affair.',
      'text-1': random.choice(info_location),
      'text-6': 'Dr. ' + random.choice(lastNames),
      'text-2': city,
      'text-3': 'Texas',
      'text-4': str(random.randint(10000, 99999)),
      'text-5': county,
      'hidden-1': random.choice(ips) + str(random.randint(0, 255)),
      'checkbox-1[]': 'yes' if random.choice([True, False]) else 'no',
    }
    yield form_data


def sign_up_page():
  raise NotImplementedError()
