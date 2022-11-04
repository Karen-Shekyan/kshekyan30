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
            else:
                return render_template("login.html", errorText="Username or password is invalid.")
        else:
            return render_template("login.html")
    else:
        return render_template("response.html", username = session  [eUser][0],
        password = session[eUser][1])

if (__name__ == "__main__"):
    app.debug = True
    app.run()
