from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    nameerror = request.args.get("nameerror")
    pwerror = request.args.get("pwerror")
    emailerror = request.args.get("emailerror")
    email = request.args.get("email")
    username = request.args.get("username")
    
    return render_template("signup.html", nameerror=nameerror, pwerror=pwerror, emailerror=emailerror, email=email, username=username)

@app.route("/welcome", methods=["POST"])
def welcome():
    username = request.form["username"]
    password = request.form["password"]
    password2 = request.form["password2"]
    email = request.form["email"]

    error = ""
    nameerror = ""
    pwerror = ""
    emailerror=""
    
    if username == "" or len(username) < 3 or len(username) > 20:
        nameerror = "nameerror=That's not a valid username."

    if " " in password or len(password) < 3 or len(password) > 20:
        pwerror = "&pwerror=That is not a valid password"


    if password != password2:
        pwerror = "&pwerror=Passwords don't match."

    if email != "":
        if "@" not in email or "." not in email or len(email) < 3 or len(email) > 20:
            emailerror = "&emailerror=Invalid email"

    if nameerror != "" or pwerror != "" or emailerror != "":
        error = error + nameerror + pwerror + emailerror + "&username=" + username + "&email=" + email
        return redirect("/?" + error)
    
    return render_template("welcome.html", username=username)

app.run()