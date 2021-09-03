import requests
import dns.resolver

target_ip = dns.resolver.resolve('prolifewhistleblower.com', 'A').response.answer[0].to_text()[len('prolifewhistleblower.com. 0 IN A '):]

def anonymous_form(token):
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'DNT': '1',
		'Origin': 'https://prolifewhistleblower.com',
		'Referer': 'https://prolifewhistleblower.com/anonymous-form/',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.58 Safari/537.36',
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
		'hidden-1': '98.218.129.19',
		'referer_url': 'https://prolifewhistleblower.com/anonymous-form/',
		'forminator_nonce': 'dde67b9a73',
		'_wp_http_referer': '/anonymous-form/',
		'form_id': '26',
		'page_id': '27',
		'form_type': 'default',
		'current_url': 'https://prolifewhistleblower.com/',
		'render_id': '0',
		'action': 'forminator_submit_form_custom-forms',
		'input_11': ''
	}

	print(data)
	# response = requests.post('https://{}/anonymous-form'.format(target_ip), headers=headers, data=data)

def sign_up_page(token):
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'DNT': '1',
		'Origin': 'https://prolifewhistleblower.com',
		'Referer': 'https://prolifewhistleblower.com/sign-up-page/',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.58 Safari/537.36',
	}

	raise NotImplementedError()
	# TODO: Add randomization of filled out data
	data = [
		('name-1', 'Name'),
		('address-1-street_address', 'Street Address'),
		('address-1-address_line', ''),
		('address-1-city', 'City'),
		('address-1-state', 'Texas'),
		('address-1-zip', 'ZIP'),
		('address-1-country', 'United States of America (USA)'),
		('phone-1', 'Phone'),
		('email-1', 'email@email.com'),
		('text-1', 'Job'),
		('text-2', 'Employer'),
		('radio-1', 'no'),
		('text-3', ''),
		('checkbox-2[]', 'other'),
		('radio-2', 'yes'),
		('text-4', 'Fake Organization'),
		('checkbox-4[]', 'plaintiff'),
		('checkbox-4[]', 'other'),
		('radio-3', 'yes'),
		('time-1-hours', '10'),
		('time-1-minutes', '30'),
		('time-1-ampm', 'am'),
		('textarea-1', 'Violation of the heartbeat act'),
		('g-recaptcha-response', token),
		('hidden-1', '98.218.129.19'),
		('referer_url', 'https://prolifewhistleblower.com/anonymous-form/'),
		('forminator_nonce', 'dde67b9a73'),
		('_wp_http_referer', '/sign-up-page/'),
		('form_id', '25'),
		('page_id', '32'),
		('form_type', 'default'),
		('current_url', 'https://prolifewhistleblower.com/'),
		('render_id', '0'),
		('action', 'forminator_submit_form_custom-forms'),
		('input_18', ''),
	]

	response = requests.post('https://{}/sign-up-page'.format(target_ip), headers=headers, data=data)

