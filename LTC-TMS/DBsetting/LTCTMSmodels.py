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
    email = Column("email", String(255), unique=True, index=True)
    phone = Column("phone", Integer, index=True)
    fname = Column("fname", String(255), index=True)
    lname = Column("lname", String(255), index=True)
    gender = Column("gender", String(255), index=True)
    birthday = Column("birthday", Date, index=True)
    nationalID = Column("nationID", String(255), index=True)
    bloodType = Column("bloodtype", String(255), index=True)
    contactno = Column("contactno", String(255), index=True)
    active = Column("active", Boolean, index=True)
    isLoggedIn = Column("isLoggedIn", Boolean, index=True)
    dateCreated = Column("dateCreated", DateTime, index=True)
    picture = Column("picture", DateTime, index=True)
    password = Column("password", String(255), index=True)

    def __init__(self):
        pass

# User account class. Child of Base
class Patient(Base, db.Model):
    """User that is a child of base"""
    __tablename__ = "patients"
    roomno = Column("roomNo.", String(255), index=True)
    cnaID = Column("cnaID", Integer, index=True)
    appointmentRecord = Column("appointmentRecord", String(255), index=True)
    medicalRecord = Column("medicalRecord", DateTime, index=True)
    description = Column("description", String(255), index=True)
    lastActive = Column("lastActive", DateTime, index=True)
    patientID = Column("patientID", Integer, primary_key=True)
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
    staffID = Column("staffID", Integer, primary_key=True)
    position = Column("staffPosition", String(255), index=True)
    cv = Column("CV", DateTime, index=True)
    license= Column("License", DateTime, index=True)

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
    requestID=Column('requestID', Integer, primary_key=True)
    patientID=Column('patientID', Integer, index=True)
    staffID=Column('staffID', Integer, index=True)
    taskID=Column('taskID', Integer, index=True)
    requestDescription=Column('requestDescription', String(255), index=True)
    isApproved=Column('isApproved', Boolean, index=True)
    dateRequested=Column('dateRequested', Date, index=True)

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
    taskID = Column('taskID', Integer, primary_key=True)
    staffID = Column('supervisorID', Integer)
    title = Column('title', String(255))
    description = Column('description', String(255))
    activated = Column('activated', String(255))
    dateCreated = Column('dateCreated', Date)
    dateModified = Column('dateModified', Date)
    lastUsed = Column('lastUsed', DateTime)
    published = Column('published', Boolean)
    image = Column('image', String(255))

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
    mainStepID = Column('mainStepID', Integer, primary_key=True)
    taskID = Column('taskID', Integer)
    title = Column('title', String(255))
    requiredInfo = Column('requiredInfo', String(255))
    listOrder = Column('listOrder', Integer)
    requiredItem = Column('requiredItem', String(255))
    stepText = Column('stepText', String(255))
    audio = Column('audio', String(255))
    image = Column('image', String(255))
    video = Column('video', String(255))

    def __init__(self, title=None):
        super(MainStep, self).__init__()
        self.title = title


class DetailedStep(db.Model):
    """
    Author: David Schaeffer, March 2018 <dscha959@live.kutztown.edu>
    """
    __tablename__ = 'detailedSteps'
    detailedStepID = Column('detailedStepID', Integer, primary_key=True)
    mainStepID = Column('mainStepID', Integer)
    title = Column('title', String(255))
    stepText = Column('stepText', String(255))
    listOrder = Column('listOrder', Integer)
    image = Column('image', String(255))

    def __init__(self, title=None):
        super(DetailedStep, self).__init__()
        self.title = title


class Keyword(db.Model):
    """
    Author: David Schaeffer, March 2018 <dscha959@live.kutztown.edu>
    """
    __tablename__ = 'keywords'
    keywordID = Column('keywordID', Integer, primary_key=True)
    taskID = Column('taskID', Integer)
    word = Column(String(255))

    def __init__(self, task_id, word):
        self.taskID = task_id
        self.word = word

    def __init__(self, formTitle=None, surv_quest=None):
        super(SurveyQuest, self).__init__()
        self.formTitle = formTitle
        survey_quest = surv_quest
