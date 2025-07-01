from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return redirect(url_for('thank_you', name=name))
    return render_template('index.html')

@app.route('/thank-you/<name>')
def thank_you(name):
    return render_template('thank_you.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)