from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chatroom():
    return render_template('chat.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
