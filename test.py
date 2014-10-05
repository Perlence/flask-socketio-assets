from gevent import monkey
monkey.patch_all()

from functools import partial
from os import path

from flask import Flask
from flask.ext.assets import Environment, Bundle
from flask.ext.socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

env = Environment(app)

env.load_path = [
    path.join(path.dirname(__file__), 'bower_components'),
]

js_bundle = Bundle(
    'jquery/dist/jquery.min.js',
    'bootstrap-sass/dist/js/bootstrap.min.js',
    output='js_all.js')

css_bundle = Bundle(
    'bootstrap-sass/lib/bootstrap.scss',
    filters=['pyscss'],
    output='css_all.css')

env.register('js_all', js_bundle)
env.register('css_all', css_bundle)

env['js_all'].urls()
env['css_all'].urls()
print 'Testing'


@app.route('/')
def index():
    return 'Success'


def start(debug=False):
    app.debug = debug
    socketio.run(app, host='127.0.0.1', port=5000)

debug = partial(start, debug=True)

if __name__ == '__main__':
    start()
