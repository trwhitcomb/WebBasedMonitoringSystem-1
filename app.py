# app.py
import os, flask, flask_socketio,requests
from flask_socketio import emit,send
import json
from flask import jsonify
from requests.auth import HTTPDigestAuth
app = flask.Flask(__name__)



socketio = flask_socketio.SocketIO(app)



@app.route('/')
def hello():
 return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
 print "%s USER CONNECTED " %  flask.request.sid

@socketio.on('data')
def message(message):
 app.logger.warning('A warning occurred (%d apples)', 42)
 app.logger.error('An error occurred')
 app.logger.info('Info')

 link = "http://"+ str( message["hostName"]) + ":" + str(message["portNumber"]) + '/state/get_state_summary'
 #Verify not necessary: TODO: Verify = FALSE should not skip authentication.
 r=requests.get(link,auth=HTTPDigestAuth('anon','the quick brown fox'))
 data = r.json()
 emit ('summary_info',data)
  
@socketio.on('disconnect')
def on_disconnect():
 print "USER DISCONNECTED"

@socketio.on('stop_suite')
def stop_suite(message):
    stop_link = "https://"+ str( message["hostName"]) + ":" + str(message["portNumber"]) + '/state/get_state_summary'
    stopped_task=requests.get(link,auth=HTTPDigestAuth('anon','the quick brown fox'), verify=False)

    
if __name__ == '__main__':# __name__!

 socketio.run(
 app,
 debug=True
 )
