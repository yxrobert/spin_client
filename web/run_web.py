#! /usr/bin/env
#coding=utf-8

from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "yx"

@app.route('/entry')
def entry_page():
    return render_template('spin_client.html', the_title='Spin Client')

@app.route('/send_cmd', methods=['POST'])
def spin1():
    print("send_cmd")
    print(request.form)
    return render_template('spin.html', the_title='Spin Client')

@app.route('/spin2', methods=['POST'])
def spin2():
    print(request.form)
    return render_template('spin.html', the_title='Spin Client')


@app.route('/spin', methods=['POST'])
def entry_login():
    print(request.form)
    acc = request.form['ThemeID']
    # token = request.form['token']
    print(acc)
    return render_template('spin.html', the_title='Spin Client')

@app.route('/spin')
def entry_spin():
    #     acc = request.form['account']
    #     token = request.form['token']
    #     player.login(acc, token)
    return render_template('spin.html', the_title='Spin Client')

def main():
    print(os.getcwd())
    app.run(debug=True)

if __name__ == '__main__':
	main()