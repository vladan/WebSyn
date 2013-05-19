#-*- coding: utf-8 -*-

from gevent import monkey
monkey.patch_all()

from models import Company
from flask import (Flask, request, session, g, redirect, url_for, abort,
        render_template, jsonify, Blueprint, current_app)
from couchdbkit import Consumer, Database
import yaml



couch_forum = Blueprint('couch_forum', __name__, template_folder='templates')



def connect_db():
    return Database(current_app.config['db']['url'])


@couch_forum.route('/i')
def show_industries():
    db = connect_db()
    all_industries = db.view("company/industries", schema=Company, group=True).all()
    return render_template('list.html', industries=all_industries)


@couch_forum.route('/poll', methods=["GET", "POST"])
def poll_changes():
    db = connect_db()
    last_change = db.info()["update_seq"]
    c = Consumer(db, backend='gevent')
    changes = c.wait_once(since=last_change, feed='longpoll',
            include_docs='true', filter="app/posts")
    return jsonify(changes)


@couch_forum.route('/poll/i', methods=["GET", "POST"])
def poll_changes():
    db = connect_db()
    last_change = db.info()["update_seq"]
    c = Consumer(db, backend='gevent')
    changes = c.wait_once(since=last_change, feed='longpoll',
            include_docs='true', filter="app/posts")
    return jsonify(changes)


@couch_forum.route('/c')
def show_companies():
    db = connect_db()
    query = db.view("company/all", schema=Company, reduce='false')
    all_companies = query.all()
    return render_template('index.html', entries=all_companies)
