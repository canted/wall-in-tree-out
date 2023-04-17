from flask import Flask, render_template, request, jsonify
import os
from completion import complete

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    response_text = complete(request.form['message'])
    return render_template('response.html', response_text=response_text)

if __name__ == '__main__':
    app.run
