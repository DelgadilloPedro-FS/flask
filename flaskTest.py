from flask import Flask, redirect, url_for,render_template, request, session
from datetime import timedelta

# create flash application
appFlask = Flask(__name__)
# secret key
appFlask.secret_key= "apples"
# set the session timer to time out session cooke
appFlask.permanent_session_lifetime = timedelta(minutes=5)


if __name__ == "__main__":
    appFlask.run(debug=True)