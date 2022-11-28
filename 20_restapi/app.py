from flask import Flask, render_template
import requests
import json
app = Flask(__name__)
@app.route('/', methods=["GET"])
def main():
	file = open("key_nasa.txt", "r")
	key = file.read()
	dict1= requests.get("https://api.nasa.gov/planetary/apod?api_key="+key).json()
	print(dict1)
	return render_template("main.html", pic = dict1["url"], title = dict1["title"], exp = dict1["explanation"])
if __name__ == '__main__':
	app.debug = True
	app.run()
