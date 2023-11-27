import flask
import socket
import os


APP = flask.Flask(__name__)
num_visitas = 0

@APP.route('/')
def index():
    global num_visitas 
    num_visitas = num_visitas + 1
    hostname = socket.gethostname()
    userinfo = {
        'username': os.environ['CLIENT_NAME']
    }
    return flask.render_template(
            'index.html', 
            user=userinfo, 
            num_visitas=num_visitas, 
            hostname=hostname)

if __name__ == '__main__':
    PORT=os.environ['PORT']
    APP.debug = True
    APP.run(host='0.0.0.0', port=PORT)
