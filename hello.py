def wsgi_application(env, start_response):
	status ='200 OK'
	headers=[('Content-Type', 'text/plain')]
	q_string= str(env.get('QUERY_STRING'))
	body=q_string.replace('&', '\n')
	body=body.encode()
	start_response(status, headers)
	return [body]