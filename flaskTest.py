from flask import Flask, redirect, url_for,render_template, request, session
from datetime import timedelta

# create flash application
appFlask = Flask(__name__)
# secret key
appFlask.secret_key = "apples"
# set the session timer to time out session cooke
appFlask.permanent_session_lifetime = timedelta(minutes=5)



# default route
@appFlask.route("/")
def home():
    # return html
    return "<b>Hello World</b>"

# login route to show session examples
@appFlask.route("/login")
def login():
    session["user"] = "Pedro"
    return "<h1>Cookies Check</h1>".format(session["user"])

# new page to print session
@appFlask.route("/newpage")
def newpage():
    print(session)
    return "check console"

if __name__ == "__main__":
    appFlask.run(debug=True)