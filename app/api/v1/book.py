#! /bin/usr/python3

from flask import Blueprint

book = Blueprint('book', __name__)


@book.route('/v1/book/get')
def get_book():
    return 'I am book.'
