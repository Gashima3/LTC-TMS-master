from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from database import db

Base = declarative_base()

class Only(Base):
    """Class that represents a basic person"""
    email = db.Column("email", db.String(255), unique=True, index=True)
    fname = db.Column("fname", db.String(255), index=True)
    lname = db.Column("lname", db.String(255), index=True)
    gender = db.Column("gender", db.String(255), index=True)
    birthday = db.Column("birthday", db.Date, index=True)
    nationalID = db.Column("nationalID", db.String(255), index=True)
    bloodType = db.Column("bloodType", db.String(255), index=True)
    contactno = db.Column("contactno", db.String(255), index=True)
    active = db.Column("active", db.Boolean, index=True)
    isLoggedIn = db.Column("isLoggedIn", db.Boolean, index=True)
    dateCreated = db.Column("dateCreated", db.DateTime, index=True)
    picture = db.Column("picture", db.DateTime, index=True)
    password = db.Column("password", db.String(255), index=True)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqlconnector://root:icac104104@localhost:3306/LTCTMS')
    Base.metadata.create_all(bind=engine)
