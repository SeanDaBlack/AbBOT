from requests_toolbelt import MultipartEncoder
import requests
import data
import redirection

anonymous_form_data = data.anonymous_form()

def anonymous_form(token):
	headers = {
    'authority': 'prolifewhistleblower.com',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'accept': '*/*',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundarymzEZsVNq7gOZvSGA',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'sec-ch-ua-platform': '"Linux"',
    'origin': 'https://prolifewhistleblower.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://prolifewhistleblower.com/anonymous-form/',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'sucuri_cloudproxy_uuid_983586173=ebf1582f789f61d67345a0786a519292; _ga=GA1.1.1279513551.1630646088; hustle_module_show_count-social_sharing-1=3; _ga_M5WWGNMLR8=GS1.1.1630646087.1.1.1630646164.0',
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
		'forminator_nonce': 'dde67b9a73',
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

	redirection.end_redirect()
	try:
		response = requests.post('https://prolifewhistleblower.com/wp-admin/admin-ajax.php', headers=headers, data=encoded_data)
		print('Successfully sent submitted form.')
		print(response)
		print(response.headers)
		print(response.text)
	except Exception as e:
		print('Had an issue.')
		print(e)
	redirection.redirect()

def sign_up_page(token):
	raise NotImplementedError()
