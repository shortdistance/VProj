from flask import session, redirect, url_for, render_template, jsonify, request, g
from . import bplogin


@bplogin.route('/login')
def login():
    return render_template("login.html")


@bplogin.route('/login_jump')
def login_jump():
    return render_template("login_jump.html")


@bplogin.route('/logout')
def logout():
    session['accessToken'] = None
    return redirect(url_for('bplogin.login'))
