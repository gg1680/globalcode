from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import datetime

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my_ping')
def ping_pong():
    emit('my_pong')

@socketio.on('my_event')
def handle_event(message):
    print("handle_event method called")

if __name__ == '__main__':
    socketio.run(app, debug=True)
