# Team Scooby-Doo Dog Erasers - Karen Shekyan, Gabriel Thompson, Russell Goyachev`
# SoftDev
# K14 -- Serving Looks
# 2022-10-19
# time spent: 0.2 hrs

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def root():
	return render_template('index.html')

app.debug = True
app.run()
