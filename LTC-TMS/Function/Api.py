import bcrypt
from datetime import datetime
from database import *
from Forms.models import Staff
from flask import jsonify


def userLogin(staffID, password):

    if staffID is None or password is None:
        return False
    usr = getHash(staffID)
    if usr is not None:
        try:
            if usr.password.encode('utf-8') == bcrypt.hashpw(password.encode('utf-8'), usr.password.encode('utf-8')):
                return True
        except ValueError:
            # Once bcrypt is enable on all passwords this can be removed, at the time of development
            # clear text passwords still existed
            if usr.password.encode('utf-8') == password.encode('utf-8'):
                return True
            return False
    else:
        return False


def getHash(staffID):
    """
    Description: Returns email associated by account in the database
    Parameters: email - (string) email associated with the account
    Return Value: p - (string) result of the query, otherwise none
    Author: Patrick Earl
    """
    p = None
    p = (Staff.query.filter_by(staffID=staffID).first())
    return p if p else None
