# HelloCaesar

A flask web app that can encrypt and decrypt messages using the Caesar encryption method - to learn about Caesar encryption take a look at [https://cryptii.com/caesar-cipher](https://cryptii.com/caesar-cipher)

## Welcome to web development!

Hopefully we've covered the fundamentals like variables, data types, functions and loops. It's time to put them into practice!

### Installation and dependencies

First things first, let's install all the dependencies. It's standard to list all the python programs you need in a file called 'requirements.txt'. Open it and take a look.

Just one thing listed - Flask. Flask is a 'web framework' - basically a bunch of tools that we can use to build a website more easily than implementing everything from scratch.

let's go ahead an install Flask by entering this command:

>> pip3 install -r requirements.txt

Okay, now let's look at the code!

### app.py

The important things in app.py are our 3 'routes' (@app.route(Some Url). These tell Flask what to do when users try to access the url we pass in as a parameter.

Our website has 3 pages, and thus we have 3 routes:

> @app.route('/')

> @app.route('/encrypt', methods=['GET', 'POST'])

> @app.route('/decrypt', methods=['GET', 'POST'])

This weird @app.route() syntax is a 'decorator'. Basically it adds functionality to the functions defined beneath.

Then we've got 2 functions called encrypt_caesar and decrypt_caesar that look a bit unfinished! That's your job!

### helpers.py

Just two helper functions here that remove any potentially malicious inputs and convert the users key into an integer. Nothing to worry about here.


### templates

Hey, there's another folder here called 'templates/'. This folder contains our html or hypertext markup language! HTML tells the user's browser how to format our data. Flask knows to look in our templates folder to retrieve our html

Take a look at index.html - this is our welcome page.

The tags for example \<html> tell the browser how to treat the contents within the tags e.g \<p> treat me like a paragraph! \</p>

html is fiddly and boring but if you're interested: https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics

Now take a look at encrypt.html . This tells the browser to display a form that the user can enter stuff into, it also tells the users browser where to send that contents of the form when the user hits confirm

### Usage

Tell our OS what our flask app is by entering:

> FLASK_APP=app.py

to run our app enter:

> flask run

you should see:

 > Serving Flask app "app.py"

 > Environment: production

 > WARNING: Do not use the development server in a production environment.
 > Use a production WSGI server instead.
 > Debug mode: on
 > Running on http://ide50-yourname.cs50.io:8080/ (Press CTRL+C to quit)
 > Restarting with stat
 > Debugger is active!
 > Debugger PIN: xxx-xxx-xxx

open the  link httpL//ide50 blah blah in your browser

Hello, Caesar!

Your website (or rather 'development server') will keep running as long as you're in your IDE. Hit ctrl-c to turn off the server.

### TODO

Finish the implementation of the caesar() function to return an encrypted message to the user using their message and key!


