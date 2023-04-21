from flask import Flask, render_template, request, Response
# from flask_socketio import SocketIO, send
from flask_sock import Sock
import os
from completion import complete, complete_legacy
import markdown2
import time
import ipdb
import json

app = Flask(__name__)
sock = Sock(app)

@app.route('/')
def index():
    return render_template('index.html')

@sock.route('/completion')
def websocket(ws):
    print('websocket()')
    while True:
        # ipdb.set_trace()
        print("True, WEBSOCKET=", ws)
        data = ws.receive()
        # parse json
        data = json.loads(data)
        print("DATA", data)

        # response = complete(data['wall'])
        response = complete_legacy(data['wall'])
        collected_message = ""
        for chunk in response:
            print(chunk)
            collected_message += chunk['choices'][0]['text'] # legacy
            # collected_message += chunk['choices'][0]['delta'].get('content', '') # gpt-3.5-turbo
            print(collected_message)
            html = markdown2.markdown(collected_message)
            ws.send(render_template('response.html', response_text=html))

if __name__ == '__main__':
    app.run

