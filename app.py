# -*- mode: python; coding: utf-8-unix -*-
#
# Time-stamp: <2020-12-09 20:26:49 norim>
#

# @note usage
#
# set FLASK_APP=app
# set FLASK_ENV=development
# flask run
#
import csv
from flask import Flask, render_template, request, redirect, url_for
import requests
from pager import Pager


# @breif csv loader into the table hash.
#
#
def read_table(url):
    """Return a list of dict"""
    # r = requests.get(url)
    with open(url) as f:
        return [row for row in csv.DictReader(f.readlines())]


APPNAME = "PrettyGalaxies"
STATIC_FOLDER = 'example'
TABLE_FILE = "example/fakecatalog.csv"

table = read_table(TABLE_FILE)
pager = Pager(len(table))


app = Flask(__name__, static_folder=STATIC_FOLDER)
app.config.update(
    APPNAME=APPNAME,
    )


# [template connstraction]
# layout.html
#  +-- 404.html
#  +-- imageview.html
#        +-- links.html
#        +-- table.html
#


# @breif home redirector
#
#
@app.route('/')
def index():
    return redirect('/0')

# @breif page handler
#
#
@app.route('/<int:ind>/')
def image_view(ind=None):
    if ind >= pager.count:
        return render_template("404.html"), 404
    else:
        pager.current = ind
        return render_template(
            'imageview.html',
            index=ind,
            pager=pager,
            data=table[ind])


# @breif processs goto form requests 
#
#
@app.route('/goto', methods=['POST', 'GET'])    
def goto():
    return redirect('/' + request.form['index'])


if __name__ == '__main__':
    app.run(debug=True)
