from flask import Flask, render_template, request
app = Flask(__name__, template_folder='template')


@app.route('/')
def main():
    return render_template('base.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/api/signUp',methods=['POST'])
def signUp():
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']


if __name__ == "__main__":
    app.run(debug=True)
