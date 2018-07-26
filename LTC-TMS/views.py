from flask import render_template, request, jsonify, redirect,url_for, flash, session, json

from app import app
from DSsetting.LTCTMSforms import CreateAccount,CreateSupervisor, EditSenior, EditSuper, AddUser, AssignUser, \
    CreateTaskForm, LoginForm, TaskAssignmentForm
from Function import UserMgmt,  TaskHelper, Update, Login, Library, TaskAssignmentHelper, Api, Reports
from database import *
from flask_login import current_user, login_required, logout_user
from DBsetting.LTCTMSmodels import Task, Patient, Staff, Request
from datetime import datetime, timedelta
from flask_weasyprint import HTML, render_pdf
import weasyprint
from flask_mail import Message
import pygal

@app.route('/', methods = ['GET'])
def index():
    return redirect("login", cide=302)

@app.route('/api/user/login', methods=['POST'])
def api_login():
    ID = request.form.get('ID')
    password = request.form.get('password')
    if success is False:
        return jsonify({'d': 'sign in failed'})
    else:
        return jsonify({'d': 'sign in success'})

@app.route('/api/user/GetByUser/<uname>', method=['GET'])
def api_getbyuser(uname):
    r = Api.getByUser(uname)
    return jsonify([r])