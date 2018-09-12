# HelloCaesar


## Welcome to web development!

Hopefully we've covered the fundementals like variables, data types, functions and loops. It's time to put them into practice!

### Installation and dependencies

First things first, let's install all the dependencies. It's standard to list all the python programs you need in a file called 'requirements.txt'. Open it and take a look.

Just one thing listed - Flask. Flask is a 'web framework' - basically a bunch of tools that we can use to build a website more easily than implementing everything from scratch.

let's go ahead an install Flask by entering this command:

pip3 install -r requirements.txt

### app.py

The important things in app.py are our 2 'routes' (@app.route(Some Url). These tell Flask what to do when users try to access the url in the brackets. Our website has two pages, and thus we have 2 routes

The other main thing is our function called caesar. This is what we want to call to encode the data supplied by the user, using the key the user provides. It's currently unfinished. that's your job!

### templates

Hey, there's another folder here called 'templates/'. This folder contains our html or hypertext markup language! HTML tells the user's browser how to format our data. Flask knows to look in our templates folder to retrieve our html

Take a look at index.html - this is our welcome page.

The tags for example <html> tell the browser how to treat the contents within the tags e.g <p> treat me like a paragraph! </p>

html is fiddly and boring but if you're interested: https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics

Now take a look at encrypt.html . Ooh a form! This tells the browser to display a form that the user can enter stuff into, it also tells the users browser where to send that contents of the form when the user hits confirm

### Usage

Tell our OS what our flask app is by entering:

> EXPORT FLASK_APP=app.py

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

Your website (or rather 'development server') will keep running as long as you're in your IDE

### TODO

Finish the implementation of the caesar() function to return an encrypted message to the user using their message and key!


