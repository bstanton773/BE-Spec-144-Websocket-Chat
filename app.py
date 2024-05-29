from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def handle_connect():
    print('Client has connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client has disconnected')


@socketio.on('message')
def handle_message(data):
    print('The handle message received:', data, type(data))
    if isinstance(data, dict) and 'name' in data:
        socketio.send(f"Hello from the server {data['name']}")
    else:
        socketio.send('Hola')


@socketio.on('custom_test_event')
def handle_cusom(data):
    print('Server handle custom received:', data)
    socketio.emit('another_event', "I am ready for lunch!")


if __name__ == "__main__":
    socketio.run(app, debug=True)
