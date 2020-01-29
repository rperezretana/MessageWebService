from datetime import datetime
from flask import render_template
from WebApi import app
import cPickle as c
import os
from sklearn import *
from collections import Counter

# region Routes and views for the flask application.

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.jade',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.jade',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.jade',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

# endregion

def make_dict():
    direc = "emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    words = []
    c = len(emails)

    for email in emails:
     f = open(email)
     blob = f.read()
     words += blob.split(" ")
     print c
     c -= 1

    for i in range(len(words)):
     if not words[i].isalpha():
     words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(3000)


clf = load("LeadsClasification.mdl")
d = make_dict()
