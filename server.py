from flask import Flask, render_template, url_for, request, redirect
import csv
from critical import *

app = Flask(__name__)



@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/critical')
def critical():
    return render_template('critical.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return '[-] Did not save to database'
    else:
        return 'something went wrong, try again!'

# CRITICALS
@app.route('/generate_critical', methods=['POST', 'GET'])
def generate_critical():
    if request.method == 'POST':
        weaponDmg = request.form['weaponDmg']
        selected = request.form.getlist('severity')
        severity = selected.count('1')
        total_severity = int(weaponDmg) + severity
        crit_array = severity_gen(total_severity)
        critical_effects = crit_gen(crit_array)
        # check for duplicate results and add/multiply numeric values
        return render_template('critical.html', critical_effects = critical_effects)
    else:
        return 'something went wrong, try again!'