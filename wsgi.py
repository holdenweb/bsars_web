import os
from flask import (Flask, Response, abort, render_template)
from logging import getLogger
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown import Markdown
from mongoengine import connect
from models import Article, Writings

connect('bsars')

appfile_dir = os.path.dirname(__file__)
app = Flask(__name__)


env = Environment(
    loader=FileSystemLoader('%s/templates/' % appfile_dir),
    autoescape=select_autoescape(['html', 'xml'])
)
logger = getLogger(__name__)


@app.route("/favicon.ico")
@app.route("/static/<anything>")
def html_page(anything="images/favicon.ico"):
    try:
        with open(
            os.path.join(appfile_dir, "static", anything),
            "rb"
        ) as f:
            return Response(f.read())
    except FileNotFoundError:
        abort(404)

@app.route("/blog/<int:article_no>")
def blog_page(article_no):
    art = Article.objects.get(article_no=article_no)
    return render_template("blog_post.html", art=art)

@app.route("/article/<int:article_no>")
def page_from_markdown(article_no):
    art = Writings.objects.get(article_no=article_no)
    md = Markdown()
    art.content = md.convert(art.content)
    return render_template("blog_post.html", art=art)


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
    app.run(host='0.0.0.0', port=2400)
