import os
import subprocess
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return '<form action="/echo" method="GET"><input name="text"><input type="submit" value="Echo"></form>'
 
@app.route("/echo")
def echo(): 
    return "You said: " + request.args.get('text', '')

@app.route("/post")
def submit():
    return subprocess.check_output("./main.py post "+ request.args.get('value', ''), shell=True)
    #return str(os.system("./main.py post "+ request.args.get('value', '')))

@app.route("/get_all")
def get_all():
    return subprocess.check_output("./main.py get_all all", shell=True)

@app.route("/get_specific")
def get_specific():
    return subprocess.check_output("./main.py get_specific "+ request.args.get('value', ''), shell=True)

@app.route("/delete")
def delete():
    return subprocess.check_output("./main.py delete "+ request.args.get('value', ''), shell=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
