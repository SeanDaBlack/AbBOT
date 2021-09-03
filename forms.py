#!/usr/bin/env python3
from requests_toolbelt import MultipartEncoder
import requests
import re

import data
import redirection

anonymous_form_data = data.anonymous_form()
session = requests.Session()
session.verify = True


def get_nonce():
  payload = "action=forminator_load_form&type=forminator_forms&id=26&render_id=0&is_preview=false&preview_data=%255B%255D&extra%255B_wp_http_referer%255D=%252Fanonymous-form%252F&extra%255Bpage_id%255D=27&extra%255Breferer_url%255D=https%253A%252F%252Fprolifewhistleblower.com%252Fanonymous-form%252F&nonce=518cbad128"
  headers = {
    "authority": "prolifewhistleblower.com",
    "accept": "*/*",
    "dnt": "1",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.58 Safari/537.36",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "sec-gpc": "1",
    "origin": "https://prolifewhistleblower.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://prolifewhistleblower.com/anonymous-form/",
    "accept-language": "en-US,en;q=0.9",
    "cookie": "sucuri_cloudproxy_uuid_a3e8df9b2=a48734bc1fde52c7762880d406add9e7; hustle_module_show_count-social_sharing-1=2"
  }

  print('Getting the nonce.')
  try:
    response = requests.post('https://prolifewhistleblower.com/wp-admin/admin-ajax.php', data=payload, headers=headers)
    match = re.search(r'name=\\"forminator_nonce\\" value=\\"(?P<nonce>.+?)\\"', response.text)
    if match == None:
      return None
    else:
      return match.group('nonce') or None
  except requests.exception.RequestException as error:
    print('Had an issue getting the nonce.')
    print(error)
    return None


def anonymous_form(token):
  headers = {
    'authority': 'prolifewhistleblower.com',
    'accept': '*/*',
    'dnt': '1',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.58 Safari/537.36',
    'content-type': '',  # Will be set below
    'sec-gpc': '1',
    'origin': 'https://prolifewhistleblower.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://prolifewhistleblower.com/anonymous-form/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'sucuri_cloudproxy_uuid_a3e8df9b2=a48734bc1fde52c7762880d406add9e7; hustle_module_show_count-social_sharing-1=36',
  }

  data = {
    'textarea-1': 'Violation',
    'text-1': 'Obtained evidence',
    'text-6': 'Clinic',
    'text-2': 'City',
    'text-3': 'State',
    'text-4': 'Zip',
    'text-5': 'County',
    'checkbox-1[]': 'no',
    'g-recaptcha-response': token,
    'hidden-1': 'IP address',
    'referer_url': 'https://prolifewhistleblower.com/anonymous-form/',
    'forminator_nonce': '2e6325bdf9',
    '_wp_https_referer': '/anonymous-form/',
    'form_id': '26',
    'page_id': '27',
    'form_type': 'default',
    'current_url': 'https://prolifewhistleblower.com/',
    'render_id': '0',
    'action': 'forminator_submit_form_custom-forms',
    'input_11': ''
  }

  generated_data = next(anonymous_form_data)
  for key in generated_data:
    data[key] = generated_data[key]
  encoded_data = MultipartEncoder(fields=data)
  headers['content-type'] = encoded_data.content_type
  data = encoded_data.to_string()
  print('Making POST request.')

  redirection.end_redirect()
  nonce = get_nonce()
  if nonce == None:
    print('No nonce found, stopping.')
    redirection.redirect()
    return
  else:
    print('Got the nonce.')

  try:
    response = session.post('https://prolifewhistleblower.com/wp-admin/admin-ajax.php', headers=headers, data=data)
    print('POST request complete.')
    print(response.text)
  except requests.exception.RequestException as error:
    print('Had an issue making the POST request.')
    print(error)
  redirection.redirect()


def sign_up_page(token):
  raise NotImplementedError()
