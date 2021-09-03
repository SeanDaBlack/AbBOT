from requests_toolbelt import MultipartEncoder
import requests
import data
import redirection

anonymous_form_data = data.anonymous_form()
session = requests.Session()
session.verify = True

def anonymous_form(token):
	headers = {
		'authority': 'prolifewhistleblower.com',
		'accept': '*/*',
		'dnt': '1',
		'x-requested-with': 'XMLHttpRequest',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.58 Safari/537.36',
		'content-type': '', # Will be set below
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
	headers['content-type'] = encoded_data.content_type
	data = encoded_data.to_string()
	print('Sending multipart data.')
	print(data)

	redirection.end_redirect()
	try:
		response = session.post('https://prolifewhistleblower.com/wp-admin/admin-ajax.php', headers=headers, data=data)
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
