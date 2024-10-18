from flask import Flask, render_template, request, redirect, url_for, flash
import csv

app = Flask(__name__)
app.secret_key = 'your-secret-key'

def save_application(name, email, course):
    with open('applications.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, course])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash('Ваше сообщение успешно отправлено!', 'success')
        return redirect(url_for('contact_success'))
    return render_template('contact.html')

@app.route('/application', methods=['GET', 'POST'])
def application():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']
        save_application(name, email, course)
        flash('Ваша заявка успешно отправлена!', 'success')
        return redirect(url_for('application_success'))
    return render_template('application.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/contact_success')
def contact_success():
    return render_template('contact_success.html')

@app.route('/application_success')
def application_success():
    return render_template('application_success.html')

if __name__ == '__main__':
    app.run(debug=True)