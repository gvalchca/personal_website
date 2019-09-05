""" blog """
import sys
from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
# FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

static_path = '/Users/agorska/ania/code/blog/static'
app = Flask(__name__, static_url_path=static_path)
flatpages = FlatPages(app)
freezer = Freezer(app)
app.config.from_object(__name__)


# Routes
@app.route('/')
def index():
    return render_template("index.html")


@app.route("/projects")
def projects():
    """ home """
    return render_template("projects.html")


@app.route("/contact")
def contact():
    """ home """
    return render_template("contact.html")


@app.route("/contact_results")
def contact_results():
    return render_template('contact_results.html')


@app.route("/blog/")
def blog():
    posts = [p for p in flatpages if p.path.startswith(POST_DIR)]
    posts.sort(key=lambda item: item['date'], reverse=False)
    return render_template('blog.html', posts=posts)


@app.route('/blog/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)