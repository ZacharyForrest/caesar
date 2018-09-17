"""
This is our web application! It's built using a 'framework' (a bunch of tools) called Flask http://flask.pocoo.org/
"""
#import some modules from flask
from flask import Flask, render_template, request, url_for
#import some 2 functions from helpers.py
from helpers import sanitise_text_input, sanitise_number_input

#Instantiate (create) our flask app object
app = Flask(__name__)
#debug mode so our browser doesn't cache (save) our page
app.debug = True

#our index (main) page
@app.route('/')
def index():
    return render_template('index.html')

#encyption page
@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    #if the user is requesting the page via GET request, just return our webpage in html
    if request.method == 'GET':
        return render_template('encrypt.html')
    #if the user POSTs us some data, let's encrypt it and return the encrypted message
    elif request.method == 'POST':
        message = sanitise_text_input(request.form["message"])
        key = sanitise_number_input(request.form['key'])
        encryptedmessage = encrypt_caesar(message, key)
        return render_template('encrypt.html', encrypted_message=encryptedmessage)

#decryption page
@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    return render_template('decrypt.html')


#function to encrypt users message using key provided
def encrypt_caesar(message, key):
    #TODO
    return

#function to decrypt a message
def decrypt_caesar(message):
    #TODO
    return

