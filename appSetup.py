topBoilerPlate = """from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
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
#............................................................................................."""

