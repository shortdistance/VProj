from flask import session, redirect, url_for, render_template, jsonify, request
from . import main


@main.route('/')
def index():
    return 'hello world'
