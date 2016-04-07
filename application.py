from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
from flask.ext.login import login_user, logout_user, current_user, login_required
from application.models import Data, Users, Questions, Results
from application.forms import EnterDBInfo, RetrieveDBInfo
from application.logic import *
from flask import session as login_session
from flask import make_response
import random, string
#from oauth2client.client import flow_from_clientsecrets, FlowExchangeError
#import httplib2
import json
#import requests
from application import db
import random

# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug=True
# change this to application specific key
application.secret_key = 'cC1YCIWOj9GgWspgNEo2'   

#.............................................................................................
#.....GET Requests.............................................................................
#.............................................................................................

# page with various http tests
@application.route('/test', methods=['GET'])
def testApp():
	return render_template('tests.html')

# Initial welcome page
@application.route('/', methods=['GET'])
def displaySplash():
    return render_template('welcome.html')

# About page
@application.route('/about', methods=['GET'])
def displayAbout():
    return render_template('about.html')
	
# Donate page
@application.route('/donate', methods=['GET'])
def donate():
    return render_template('donate.html')

# News page
@application.route('/news', methods=['GET'])
def displayNews():
    return render_template('messages.html')
	
# Visit us page
@application.route('/visit', methods=['GET'])
def visit():
    return render_template('visit.html')

# Hiker Info page
@application.route('/hikerinfo', methods=['GET'])
def displayHikerInfo():
    return render_template('hikerinfo.html')
	
# Order page
@application.route('/order', methods=['GET'])
def takeOrder():
    return render_template('order.html')

# Update Inventory page
@application.route('/updateinventory', methods=['GET'])
def updateInventory():
    return render_template('updateinventory.html')
	
#.............................................................................................
#.....POST Requests.............................................................................
#.............................................................................................

# Login page
@application.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    return render_template('login.html',
                           title='Sign In')

#.............................................................................................
#.....Helper requests.............................................................................
#.............................................................................................

@application.route('/authorize/<provider>')
def oauth_authorize(provider):
    # Flask-Login function
    if not current_user.is_anonymous():
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()

@application.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous():
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    username, email = oauth.callback()
    if email is None:
        # I need a valid email address for my user identification
        flash('Authentication failed.')
        return redirect(url_for('index'))
    # Look if the user already exists
    user=User.query.filter_by(email=email).first()
    if not user:
        # Create the user. Try and use their name returned by Google,
        # but if it is not set, split the email address at the @.
        nickname = username
        if nickname is None or nickname == "":
            nickname = email.split('@')[0]

        # We can do more work here to ensure a unique nickname, if you 
        # require that.
        user=User(nickname=nickname, email=email)
        db.session.add(user)
        db.session.commit()
    # Log in the user, by default remembering them for their next visit
    # unless they log out.
    login_user(user, remember=True)
    return redirect(url_for('index'))

#.............................................................................................
#.....Boiler plate.............................................................................
#.............................................................................................


if __name__ == '__main__':
    #application.run(host='0.0.0.0')<---works on aws eb
	application.run(host = '0.0.0.0', port = 5000)
