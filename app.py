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
    #if the user POSTs us some data, let's encrypt it and return the encrypted message!
    elif request.method == 'POST':
        message = sanitise_text_input(request.form["message"])
        key = sanitise_number_input(request.form['key'])
        encryptedmessage = encrypt_caesar(message, key)
        return render_template('encrypt.html', encrypted_message=encryptedmessage)

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    return render_template('decrypt.html')

# input validation functions
# https://www.owasp.org/index.php/Input_Validation_Cheat_Sheet
# - removes potentially hazardous characters 
def sanitise_text_input(s):
    import re, html
    allowed_characters = "a-zA-Z0-9\_\,\s\.\-\!\?"
    s = re.sub(r'[^{}]+'.format(allowed_characters), '', s)
    return html.escape(s)
# - removes any non-numeric numbers and converts the string to an int 
def sanitise_number_input(n):
    import re
    allowed_characters = "0-9"
    n = re.sub(r'[^{}]+'.format(allowed_characters), '', str(n))
    try:
        return int(n)
    except ValueError:
        return 0

def encrypt_caesar(message, key):
    #TODO
    return


def decrypt_caesar(message):
    #TODO
    return

