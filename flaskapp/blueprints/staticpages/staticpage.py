#-*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


static_page = Blueprint('static_page', __name__)

@static_page.route('/p', defaults={'page': 'index'})
@static_page.route('/p/<page>')
def show(page):
  try:
    render_template('html/%s.html' % page)
  except TemplateNotFound:
    abort(404)
