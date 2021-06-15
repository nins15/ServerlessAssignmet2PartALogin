from flask import Blueprint, render_template,request,url_for,redirect

#from flask_login import current_user, login_user, logout_user, login_required

views=Blueprint('views',__name__)
@views.route('/Login')
def home():

    return render_template("Logout.html")