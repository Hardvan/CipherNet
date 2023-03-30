from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/morse')
def morse():

    return render_template('morse.html')


@app.route('/rsa')
def rsa():

    return render_template('rsa.html')


if __name__ == "__main__":
    app.run(debug=True)
