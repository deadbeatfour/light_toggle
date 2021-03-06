from bottle import run, get, post, request
import os

light = {
	'state' : 'off' 
} # Start off


@get('/state')
def get_status():
	return light

@post('/state')
def toggle_status():
	set_request = request.json.get('state')
	light['state'] = set_request
	return {'message': 'Light state set to {}'.format(set_request.lower())}


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
	run(host='localhost', port=8080, debug=True, reloader=True)