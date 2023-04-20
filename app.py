from flask import Flask, render_template, request, Response
# from flask_socketio import SocketIO, send
from flask_sock import Sock
import os
from completion import complete
import markdown2
import time
import ipdb

app = Flask(__name__)
sock = Sock(app)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     # response_text = complete(request.form['message'])
#     return render_template('response.html', prompt=request.form['wall'])

@sock.route('/completion')
def websocket(ws):
    print('websocket()')
    while True:
        # ipdb.set_trace()
        print("True, WEBSOCKET=", ws)
        data = ws.receive()
        print("DATA", data)
        response = complete(data['wall'])
        collected_message = ""
        for chunk in response:
            # collected_messages.append(chunk['choices'][0]['delta'])
            # collected_message = ''.join([m.get('content', '') for m in collected_messages])
            collected_message += chunk['choices'][0]['delta'].get('content', '')
            print(collected_message)
            html = markdown2.markdown(collected_message)
            ws.send(render_template('response.html', response_text=html))


        # html = ""
        # for i in [1,2,3,4,5,6,7,8,9]:
        #     collected_message = "- the number is " + str(i) + "\n"
        #     html = markdown2.markdown(collected_message)
        #     time.sleep(1)
        #     # data = ws.receive()
        #     ws.send(render_template('response.html', response_text=html))

        # # ipdb.set_trace()


if __name__ == '__main__':
    app.run

