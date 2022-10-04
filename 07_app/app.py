'''
<NAME>
SoftDev
K07 --
2022-10-03
Time Spent:
'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:

QCC:
0. This syntax looks like Java's syntax for initializing objects with a
   parameter.
1. '/' is used when navigating directories and in web addresses (related?).
   Signifies that <left> contains <right>(?)
      - Changing the string here results in a 'URL not found' error.
2. This prints in the terminal where this program runs.
3. This will print the __name__ attribute of app??
4. The string will print on the webpage found at the http link provided by
   running this script, since the output reads "Running on
   http://127.0.0.1:5000/".
5. This looks like an object method. In Java, an object's method can be called
   by an instance of it with the '.' operator.
...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
