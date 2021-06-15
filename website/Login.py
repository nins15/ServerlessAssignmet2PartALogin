from flask import Blueprint, render_template
from flask import Blueprint, render_template, flash, redirect,url_for,request,session
from flask_login import current_user, logout_user, login_required

from . import db

import flask_wtf
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField

Login = Blueprint('Login', __name__)


@Login.route('/',methods=['GET','POST'])
def login():
    print("HI")
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        mycursor = db.cursor()

        mycursor.execute("SELECT password FROM user where email='"+email+"';")

        user = mycursor.fetchone()
        #print(user[0])
        if user[0]:
            if user[0]== password:
                session['user']=email
                mycursor = db.cursor()
                mycursor.execute("UPDATE LoginInfo SET status = 'online' WHERE email = '"+email+"';")
                db.commit()
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.')

    return render_template("Login.html")

@Login.route('/Logout')
def Logout():
    #logout_user()
    mycursor = db.cursor()
    user=session.pop('user')
    mycursor.execute("UPDATE LoginInfo SET status = 'offline' WHERE email = '" + user + "';")
    db.commit()
    return redirect(url_for('Login.login'))
