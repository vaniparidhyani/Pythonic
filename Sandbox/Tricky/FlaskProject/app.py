#!/usr/bin/python

import backend 
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def fill_the_form():
  return render_template('my-form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    inputs = {}
    inputs['Username'] = request.form.get('Username').lower()
    inputs['Shell'] = request.form.get('ShellType').lower()
    inputs['Home'] = request.form.get('HomeFolder').lower()
    inputs['Pswd'] = request.form.get('Password')
    inputs['Sudo'] = request.form.get('Sudo')
    inputs['Op'] = request.form.get('Op')
    return backend.MainFunction(inputs)


if __name__ == "__main__":
  app.run(debug=True)
