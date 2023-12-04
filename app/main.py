import flask
import socket
import os
import redis

APP = flask.Flask(__name__)

@APP.route('/')
def index():

    r = redis.Redis(host=REDISHOST, port=REDISPORT, decode_responses=True)

    num_visitas = r.incr("contrador_visitas")

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
    REDISPORT=os.environ['REDISPORT']
    REDISHOST=os.environ['REDISHOST']
    APP.debug = True
    APP.run(host='0.0.0.0', port=PORT)
