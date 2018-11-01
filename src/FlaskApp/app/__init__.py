# _*_ coding: utf-8 _*_
from flask import Flask, flash, g, request, render_template, url_for, redirect
from app import db
from datetime import datetime
import json, requests, os, jinja2

app = Flask(__name__)

@app.route('/')
def login():
	return render_template('auth/login.html')

@app.route('/validateLogin', methods=["POST"])
def validateLogin():
	try:
		userid = request.form['userid']
		passwd = request.form['passwd']
		if db.getauth(userid, passwd):
				return redirect(url_for('main', userid=userid))
		else:
				return render_template('auth/login.html')
	except Exception as e:
		return render_template('auth/login.html')

@app.route('/addTodo', methods=["POST"])
def addTodo():
	try:
		userid = request.form['userid']
		priority = request.form['priority']
		title = request.form['title']
		contain = request.form['contents']
		deadline = request.form['deadline']
		data = [userid, int(priority), title, contain, deadline]
		db.insertSchedule(data)
		return redirect(url_for('main', userid=userid))
	except Exception as e:
		return redirect(url_for('main', userid=userid))

@app.route('/deleteTodo', methods=['Post'])
def deleteTodo():
	userid = request.form['userid']
	data = request.form.getlist('checkbox')
	db.deleteSchedule(userid, data)
	return redirect(url_for('main', userid=userid))

	
@app.route('/main/<userid>')
def main(userid):
	todo = db.getScheduler(userid)
	todo = sorted(todo, key=lambda do: do["priority"])
	for do in todo:
			do["deadline"] = [str(do["deadline"]), datetime.now().strftime("%Y-%m-%d")]
	return render_template('auth/index.html', data=todo, userid=userid)


 
