import os

from flask import Flask
from flask import render_template

app = Flask(__name__)
# For Heroku, something like
# heroku config:set APP_SETTINGS=config.ProductionConfig is appropriate.
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/robots.txt')
def robots():
    res = app.make_response('User-agent: *\nAllow: /')
    res.mimetype = 'text/plain'
    return res

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
