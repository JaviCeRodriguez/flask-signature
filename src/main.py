from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def lionel(): 
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def lionel(): 
    return render_template('index.html')
