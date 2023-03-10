"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config
import logging
from mypymongo import brevet_insert, brevet_fetch

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    start_time = request.args.get('date', type=str)
    brevet_length = request.args.get('length',type=float)
    app.logger.debug("km={}".format(km))
    app.logger.debug("start_time={}".format(start_time))
    app.logger.debug("brevet_length={}".format(brevet_length))
    # FIXME!
    # Right now, only the current time is passed as the start time
    # and control distance is fixed to 200
    # You should get these from the webpage!
    open_time = acp_times.open_time(km, brevet_length, arrow.get(start_time)).format('YYYY-MM-DDTHH:mm')
    close_time = acp_times.close_time(km, brevet_length, arrow.get(start_time)).format('YYYY-MM-DDTHH:mm')
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)

@app.route("/_insert", methods=["POST"])
def _insert():
    # start = request.args.get('start', type=str),
    # brevet= request.args.get('brevet_dist_km', type=str),
    # km = request.args.getlist('kmlist', type=str),
    # open = request.args.getlist('openlist',type=str),
    # close = request.args.getlist('closelist',type=str)
    # app.logger.debug("kmlist={}".format(km))
    app.logger.debug("hit insert")
    app.logger.debug(request.args.get('start', type=str))

    input_json = flask.request.json

    return flask.jsonify(result=
    brevet_insert(
    input_json["start"],
    #request.args.get('brevet_dist_km', type=str),
    input_json["brevet_dist_km"],
    #request.args.getlist('kmlist', type=str),
    input_json["controllist"]
    #request.args.getlist('openlist',type=str),
    #request.args.getlist('closelist',type=str)
    ))

@app.route("/_fetch")
def _fetch():
    fetched = brevet_fetch()
    return flask.jsonify(result=fetched)
#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")