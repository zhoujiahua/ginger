#! /bin/usr/python3

from flask import Blueprint

user = Blueprint('user', __name__)


@user.route('/v1/user/get')
def get_user():
    return 'i am jerry'
