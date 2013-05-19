#-*- coding: utf-8 -*-
import os

from gevent.pywsgi import WSGIServer
from flask import (Flask, request, session, g, redirect, url_for, abort,
        render_template, jsonify)
import yaml
from blueprints import blueprint_list


class Application(object):
    """No real need for this class, just a try to implement it this way.
    """
    def __init__(self, config):
        self.app = Flask(__name__)
        if config is not None:
            self.app.config.update(config)
        for blueprint in blueprint_list:
            if isinstance(blueprint, tuple):
                self.app.register_blueprint(blueprint[0],
                        url_prefix=blueprint[1])
            else:
                self.app.register_blueprint(blueprint)

    def __call__(self):
        return self.app

    def run(self, host="0.0.0.0", port=5000, **kwargs):
        """Run a testing server in debug mode using gevent's wsgi server.
        """
        # overwrite debug to True when running the app this way
        self.app.debug = True
        httpserver = WSGIServer((host, port), self.app)
        print "starting gevent.WSGIServer server on http://%s:%d" % (host, port)
        httpserver.serve_forever()


if __name__ == "__main__":
    curdir = os.path.abspath(os.path.dirname(__file__))
    confpath = os.path.join(curdir, '../config.yaml')
    with open(confpath) as f:
        config = yaml.load(f)

    app = Application(config)
    app.run()
