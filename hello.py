def wsgi_application(env, start_response):
	status ='200 OK'
	headers=[('Content-Type', 'text/plain')]
	q_string= env.get('QUERY_STRING')
	q=q_string.split('&')
	body=''
	for i in q:
		body+=i + '/n'
	start_response(status, headers)
	return [body.strip().encode()]