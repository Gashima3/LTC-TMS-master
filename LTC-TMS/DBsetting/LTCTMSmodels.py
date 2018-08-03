#
# Database Models
# author: Mason Hoffman, Nathaniel Yost, Gama F. Ahimsa
# created: 7/23/2018
# latest:
# purpose: Model classes for interaction with SQLAlchemy
#

from database import db
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import Boolean, DateTime, Column, Integer, \
                       String, ForeignKey, Date
from sqlalchemy.orm import relationship

# Base class inherited by Supervisor and User class
class Base(UserMixin, object):
    """Class that represents a basic person"""
    email = db.Column( db.String(255), unique=True, index=True)
    phone = db.Column(db.Integer, index=True)
    fname = db.Column( db.String(255), index=True)
    lname = db.Column( db.String(255), index=True)
    gender = db.Column( db.String(255), index=True)
    birthday = db.Column( db.Date, index=True)
    nationalID = db.Column( db.String(255), index=True)
    bloodType = db.Column( db.String(255), index=True)
    contactno = db.Column( db.String(255), index=True)
    active = db.Column( db.Boolean, index=True)
    isLoggedIn = db.Column( db.Boolean, index=True)
    dateCreated = db.Column( db.DateTime, index=True)
    picture = db.Column( db.DateTime, index=True)
    password = db.Column(db.String(255), index=True)

    def __init__(self):
        pass

# User account class. Child of Base
class Patient(Base, db.Model):
    """User that is a child of base"""
    __tablename__ = "patients"
    roomno = db.Column( db.String(255), index=True)
    cnaID = db.Column(db.Integer, index=True)
    appointmentRecord = db.Column( db.String(255), index=True)
    medicalRecord = db.Column(db.DateTime, index=True)
    description = db.Column(db.String(255), index=True)
    lastActive = db.Column(db.DateTime, index=True)
    patientID = db.Column(db.Integer, primary_key=True)
    role = "patient"

    # patients constructor
    def __init__(self, patientID=None, password=None):
        # Call parent constructor
        super(Patients, self).__init__()
        self.patientID = patientID
        self.password = password
        self.dateCreated = datetime.utcnow()
        self.lastActive = datetime.utcnow()

    # get_id override for userID
    def get_id(self):
        return str(self.patientID)

    # the informal string representation of a user object
    def __repr__(self):
        return '<User %r>' % (self.patientID)

# Stuff class. Child of Base
class Staff(Base, db.Model):
    """Staff that is a child of base"""
    __tablename__ = "staff"
    staffID = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(255), index=True)
    cv = db.Column(db.DateTime, index=True)
    license= db.Column(db.DateTime, index=True)

    if position == "director":
        role = "director"
    elif position == "CNO":
        role = "CNO"
    else:
        role = "CNA"

    # get_id override for supervisorID
    def get_id(self):
        return str(self.staffID)

    def __init__(self, staffID=None, password=None):
        # Call parent constructor
        super(Staff, self).__init__()
        self.staffID = staffID
        self.password = password
        self.dateCreated = datetime.utcnow()
        self.lastActive = datetime.utcnow()

    def __repr__(self):
        return "<Staff %r>" % (self.staffID)



class Request(db.Model):
    __tablename__="request"
    requestID=db.Column(db.Integer, primary_key=True)
    patientID=db.Column(db.Integer, index=True)
    staffID=db.Column(db.Integer, index=True)
    taskID=db.Column(db.Integer, index=True)
    requestDescription=db.Column(db.String(255), index=True)
    isApproved=Column(db.Boolean, index=True)
    dateRequested=Column(db.Date, index=True)

    def __init__(self):
        pass

    def __repr__(self):
        return "<Request taskID:%r>" % (self.taskID)


class Task(db.Model):
    """
    Author: David Schaeffer, March 2018 <dscha959@live.kutztown.edu>
    Basic task fields that are used for the Task, Main Steps, and Detailed
    Steps"""
    __tablename__ = 'task'
    taskID = db.Column(db.Integer, primary_key=True)
    staffID = db.Column(db.Integer)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    activated = db.Column(db.String(255))
    dateCreated = db.Column(db.Date)
    dateModified = db.Column(db.Date)
    lastUsed = db.Column(db.DateTime)
    published = db.Column(db.Boolean)
    image = db.Column(db.String(255))

    def __init__(self, title=None):
        super(Task, self).__init__()
        self.title = title
        self.dateCreated = datetime.utcnow()
        self.dateModified = datetime.utcnow()
        self.lastUsed = datetime.utcnow()


class MainStep(db.Model):
    """
    Author: David Schaeffer, March 2018 <dscha959@live.kutztown.edu>
    """
    __tablename__ = 'mainSteps'
    mainStepID = db.db.Column(db.Integer, primary_key=True)
    taskID = db.Column(db.Integer)
    title = db.Column(db.String(255))
    requiredInfo = db.db.Column(db.String(255))
    listOrder = db.db.Column(db.Integer)
    requiredItem = db.db.Column(db.String(255))
    stepText = db.db.Column(db.String(255))
    audio = db.db.Column(db.String(255))
    image = db.db.Column(db.String(255))
    video = db.db.Column(db.String(255))

    def __init__(self, title=None):
        super(MainStep, self).__init__()
        self.title = title


class DetailedStep(db.Model):
    """
    Author: David Schaeffer, March 2018 <dscha959@live.kutztown.edu>
    """
    __tablename__ = 'detailedSteps'
    detailedStepID = db.Column(db.Integer, primary_key=True)
    mainStepID = db.Column(db.Integer)
    title = db.Column(db.String(255))
    stepText = db.Column(db.String(255))
    listOrder = db.Column(db.Integer)
    image =db.Column(db.String(255))

    def __init__(self, title=None):
        super(DetailedStep, self).__init__()
        self.title = title


class Keyword(db.Model):
    """
    Author: David Schaeffer, March 2018 <dscha959@live.kutztown.edu>
    """
    __tablename__ = 'keywords'
    keywordID = db.Column(db.Integer, primary_key=True)
    taskID = db.Column(db.Integer)
    word =db.Column(db.String(255))

    def __init__(self, task_id, word):
        self.taskID = task_id
        self.word = word

    def __init__(self, formTitle=None, surv_quest=None):
        super(SurveyQuest, self).__init__()
        self.formTitle = formTitle
        survey_quest = surv_quest
