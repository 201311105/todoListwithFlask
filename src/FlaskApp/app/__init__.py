# _*_ coding: utf-8 _*_
from flask import Flask, flash, request, render_template, url_for, redirect
from app import db
from datetime import datetime
import json, os, jinja2

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def redir():
    return redirect(url_for('login'))

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/validateSignup', methods=["POST"])
def validateSignup():
	userid = request.form['userid']
	passwd1 = request.form['passwd1']
	passwd2 = request.form['passwd2']
	if passwd1 != passwd2:
			flash("비밀번호가 서로 다릅니다")
			return redirect(url_for('signup'))
	else:
		res = db.signUp(userid, passwd1)
		if not res:
			flash("이미 존재하는 아이디")
			return redirect(url_for('login'))
		else:		
			flash("회원가입 완료")
			return redirect(url_for('login'))

@app.route('/validateLogin', methods=["POST"])
def validateLogin():
	try:
		userid = request.form['userid']
		passwd = request.form['passwd']
		if db.getauth(userid, passwd):
				return redirect(url_for('main', userid=userid))
		else:
				return render_template('login.html')
	except Exception as e:
		return render_template('login.html')

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

@app.route('/modify', methods=['POST'])
def chkBtn():
	userid = request.form['userid']
	btn = request.form['button']
	if btn == 'delete':
		data = request.form.getlist('checkbox')
		db.deleteSchedule(userid, data)
		return redirect(url_for('main', userid=userid))	

	elif btn == 'modify':
		chk = request.form.getlist('checkbox')
		select = []
		todo = db.getScheduler(userid)
		todo = sorted(todo, key=lambda do: do["priority"])
		for do in todo:
			do["deadline"] = [str(do["deadline"]), datetime.now().strftime("%Y-%m-%d")]
		for s in chk:
			select.append(int(s))
		return render_template('modify.html', userid=userid, data=todo, select=select)

@app.route('/modifyTodo', methods=["POST"])
def modifyTodo():
	try:
		seq = request.form.getlist('seq')
		userid = request.form['userid']
		priority = request.form.getlist('priority')
		title = request.form.getlist('title')
		contain = request.form.getlist('contents')
		deadline = request.form.getlist('deadline')
		isDone = request.form.getlist('isDone')
		modi = []
		for i in range(len(seq)):
			data = [priority[i], title[i], contain[i], deadline[i], isDone[i], int(seq[i])]
			modi.append(data)
		db.modifySchedule(modi)
		return redirect(url_for('main', userid=userid))

	except Exception as e:
			return redirect(url_for('main', userid=userid))

@app.route('/main/<userid>')
def main(userid):
	todo = db.getScheduler(userid)
	todo = sorted(todo, key=lambda do: do["priority"])
	for do in todo:
			do["deadline"] = [str(do["deadline"]), datetime.now().strftime("%Y-%m-%d")]
	return render_template('index.html', data=todo, userid=userid)


 
