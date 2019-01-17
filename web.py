from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return '<span class="box">Hello World!!!!</span><link rel="stylesheet" href="/static/css/index.css" /><img style="width:100px" src="/static/image/python.jpg"/><script src="/static/js/index.js"></script>'


@app.route('/test')
def test():
    posts = [
        {'title': 'fdafdsafdsaf1', 'abs': 'fdasfdsa......'},
        {'title': 'fdafdsafdsaf2', 'abs': 'fdasfdsa......'},
        {'title': 'fdafdsafdsaf', 'abs': 'fdasfdsa......'},
        {'title': 'fdafdsafdsaf', 'abs': 'fdasfdsa......'},
        {'title': 'fdafdsafdsaf', 'abs': 'fdasfdsa......'},
        {'title': 'fdafdsafdsaf', 'abs': 'fdasfdsa......'},
        {'title': 'fdafdsafdsaf', 'abs': 'fdasfdsa......'},
        {'title': 'fdafdsafdsaf', 'abs': 'fdasfdsa......'}
    ]
    return render_template('index.html', posts=posts)
