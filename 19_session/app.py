# Team Scooby-Doo Dog Erasers - Karen Shekyan, Gabriel Thompson, Russell Goyachev
# SoftDev
# K19 -- Sessions Greetings
# 2022-11-04
# time spent: 1.2hrs

from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)

app.secret_key = "AAAAA";
username = "BOB"
password = "PINEAPPLE"
eUser = ""
ePass = ""

@app.route('/', methods = ['GET', 'POST'])
def login():
    print(session)
    if (not session):
        if (request.method == "POST"):
            global eUser
            eUser = request.form['user']
            global ePass
            ePass = request.form['pass']

            if (request.form['user'] == username and request.form['pass'] == password):
                try:
                    session[eUser] = [request.form["user"], request.form["pass"]]
                except KeyError:
                    return render_template("login.html")

                return render_template("response.html", username = session[eUser][0],
                password = session[eUser][1])
            elif request.form['user'] == username:
                return render_template("login.html", errorText="Password is invalid.")
            elif request.form['pass'] == password:
                return render_template("login.html", errorText="Username is invalid.")
            else:
                return render_template("login.html", errorText="Username and password is invalid.")
        else:
            return render_template("login.html")
    else:
        return render_template("response.html", username = session  [eUser][0],
        password = session[eUser][1])

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop(eUser, None)
    return redirect('/')

if (__name__ == "__main__"):
    app.debug = True
    app.run()
