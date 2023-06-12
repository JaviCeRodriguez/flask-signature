from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home(): 
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        rol = request.form.get('rol')
        linkedin = request.form.get('linkedin')
        cal = request.form.get('cal')
        return render_template('result.html', fullname=fullname, rol=rol, linkedin=linkedin, cal=cal)
    return render_template('index.html')


@app.route('/result')
def result():
    fullname = request.args.get('fullname')
    rol = request.args.get('rol')
    linkedin = request.args.get('linkedin')
    cal = request.args.get('cal')
    return render_template('results.html', fullname=fullname, rol=rol, linkedin=linkedin, cal=cal)
