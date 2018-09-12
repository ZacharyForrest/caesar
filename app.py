"""
This is our web application! It's built using a 'framework' (a bunch of tools) called Flask http://flask.pocoo.org/
"""


from flask import Flask, render_template, request, url_for


app = Flask(__name__)

app.debug = True


@app.route('/')

def index():

    return render_template('index.html')


@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'GET':
        return render_template('encrypt.html')
    #if the user POSTs us some data, let's encrypt it and return the encryptedmessage!
    elif request.method == 'POST':
        encryptedmessage = caesar(request.form["message"], request.form['key'])
        return render_template('encrypt.html', encrypted_message=encryptedmessage)


def caesar(message, key):
    #TODO
    pass



