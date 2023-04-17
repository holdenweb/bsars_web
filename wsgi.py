import os
import io
import sys
from io import BytesIO
from flask import (Blueprint, Flask, Response, abort, render_template, flash,
                   send_file, redirect, request, url_for)
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, StringField
from wtforms.validators import DataRequired
from zipfile import ZipFile
from logging import getLogger
from jinja2 import Environment, FileSystemLoader, select_autoescape
import markdown
from mongoengine import connect

connect('bsars')

appfile_dir = os.path.dirname(__file__)
app = Flask(__name__)


env = Environment(
    loader=FileSystemLoader('%s/templates/' % appfile_dir),
    autoescape=select_autoescape(['html', 'xml'])
)
logger = getLogger(__name__)


@app.route("/static/<anything>")
def html_page(name):
    try:
        with open(
            os.path.join(appfile_dir, "static", anything)
        ) as f:
            return Response(f.read())
    except FileNotFoundError:
        abort(404)

@app.route("/")
@app.route("/<name>")
def page_from_html(name="index"):
    return render_template(f"{name}.html")

@app.errorhandler(404)
def page_not_found(error):
    return f"That's a 404. Sorry, Dave: {error.description}."
    # return render_template('404.html', title = '404'), 404


app.config['SECRET_KEY'] = "lkjahskdflkjad[pouaerpoiuqt"
application = app.wsgi_app

if __name__ == '__main__':
    app.run(port=2400)
