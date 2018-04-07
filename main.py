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
    
    if username == "":
        error = "That's not a valid username."
        return redirect("/?nameerror=" + error + "&username=" + username + "&email=" + email)

    if password != password2:
        error = "Passwords don't match."
        return redirect("/?pwerror=" + error + "&username=" + username + "&email=" + email)

    if " " in password or len(password) < 3 or len(password) > 20:
        error = "That is not a valid password"
        return redirect("/?pwerror=" + error + "&username=" + username + "&email=" + email)

    if email != "":
        if "@" not in email or "." not in email or len(email) < 3 or len(email) > 20:
            error = "That is not a valid email"
            return redirect("/?emailerror=" + error + "&username=" + username + "&email=" + email)
    
    return render_template("welcome.html", username=username)

app.run()